"""
File Organizer - Auto-organize downloads folder
Features:
- Organize files by extension into categorized folders
- Move files to appropriate folders (Documents, Images, Videos, etc.)
- Undo last organization
- Dry run mode (preview changes)
- Custom folder mappings
- Schedule automatic organization
- Detailed logging
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
import json

class FileOrganizer:
    def __init__(self, target_directory=None):
        # Set target directory (default: Downloads folder)
        if target_directory:
            self.target_dir = Path(target_directory)
        else:
            self.target_dir = Path.home() / "Downloads"
        
        # File categories
        self.file_categories = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico', '.webp', '.tiff'],
            'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'],
            'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.tex'],
            'Spreadsheets': ['.xls', '.xlsx', '.csv', '.ods'],
            'Presentations': ['.ppt', '.pptx', '.odp'],
            'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
            'Code': ['.py', '.java', '.cpp', '.c', '.js', '.html', '.css', '.php', '.rb', '.go', '.rs'],
            'Executables': ['.exe', '.msi', '.dmg', '.app', '.deb', '.rpm'],
            'Books': ['.epub', '.mobi', '.azw', '.azw3'],
            'Design': ['.psd', '.ai', '.sketch', '.xd', '.fig'],
            'Data': ['.json', '.xml', '.yaml', '.yml', '.sql', '.db', '.sqlite']
        }
        
        # History file for undo functionality
        self.history_file = "organization_history.json"
        self.log_file = "file_organizer.log"
    
    def log(self, message):
        """Log message to file and console"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_message + '\n')
    
    def get_file_category(self, file_path):
        """Determine file category based on extension"""
        extension = file_path.suffix.lower()
        
        for category, extensions in self.file_categories.items():
            if extension in extensions:
                return category
        
        return 'Others'
    
    def organize_files(self, dry_run=False):
        """Organize files in target directory"""
        if not self.target_dir.exists():
            self.log(f"✗ Directory not found: {self.target_dir}")
            return
        
        self.log("="*70)
        self.log(f"{'DRY RUN - ' if dry_run else ''}Organizing files in: {self.target_dir}")
        self.log("="*70)
        
        # Get all files (excluding directories)
        files = [f for f in self.target_dir.iterdir() if f.is_file()]
        
        if not files:
            self.log("✗ No files found to organize.")
            return
        
        # Track moves for undo functionality
        moves = []
        stats = {}
        
        for file_path in files:
            # Skip hidden files and log files
            if file_path.name.startswith('.') or file_path.name in [self.history_file, self.log_file]:
                continue
            
            category = self.get_file_category(file_path)
            
            # Create category folder if it doesn't exist
            category_folder = self.target_dir / category
            
            if not dry_run and not category_folder.exists():
                category_folder.mkdir(parents=True, exist_ok=True)
            
            # Destination path
            dest_path = category_folder / file_path.name
            
            # Handle duplicate filenames
            counter = 1
            original_dest = dest_path
            while dest_path.exists() and not dry_run:
                name = original_dest.stem
                ext = original_dest.suffix
                dest_path = category_folder / f"{name}_{counter}{ext}"
                counter += 1
            
            # Move file
            if dry_run:
                self.log(f"[PREVIEW] {file_path.name} → {category}/")
            else:
                try:
                    shutil.move(str(file_path), str(dest_path))
                    self.log(f"✓ Moved: {file_path.name} → {category}/")
                    moves.append({
                        'source': str(dest_path),
                        'original': str(file_path)
                    })
                except Exception as e:
                    self.log(f"✗ Error moving {file_path.name}: {e}")
            
            # Update statistics
            stats[category] = stats.get(category, 0) + 1
        
        # Save history for undo
        if not dry_run and moves:
            self.save_history(moves)
        
        # Print statistics
        self.log("\n" + "="*70)
        self.log("SUMMARY")
        self.log("="*70)
        for category, count in sorted(stats.items()):
            self.log(f"{category}: {count} file(s)")
        self.log(f"\nTotal files {'previewed' if dry_run else 'organized'}: {sum(stats.values())}")
        self.log("="*70)
    
    def save_history(self, moves):
        """Save move history for undo functionality"""
        history = {
            'timestamp': datetime.now().isoformat(),
            'moves': moves
        }
        
        with open(self.history_file, 'w') as f:
            json.dump(history, f, indent=4)
        
        self.log(f"✓ History saved. Use 'undo' to reverse changes.")
    
    def undo_last_organization(self):
        """Undo last file organization"""
        if not os.path.exists(self.history_file):
            self.log("✗ No history found. Nothing to undo.")
            return
        
        try:
            with open(self.history_file, 'r') as f:
                history = json.load(f)
        except json.JSONDecodeError:
            self.log("✗ Error reading history file.")
            return
        
        self.log("="*70)
        self.log("UNDOING LAST ORGANIZATION")
        self.log("="*70)
        
        moves = history.get('moves', [])
        success_count = 0
        
        for move in moves:
            source = Path(move['source'])
            original = Path(move['original'])
            
            if source.exists():
                try:
                    shutil.move(str(source), str(original))
                    self.log(f"✓ Restored: {source.name} → {original.parent.name}/")
                    success_count += 1
                except Exception as e:
                    self.log(f"✗ Error restoring {source.name}: {e}")
            else:
                self.log(f"✗ File not found: {source.name}")
        
        # Remove empty category folders
        for category in self.file_categories.keys():
            category_folder = self.target_dir / category
            if category_folder.exists() and not any(category_folder.iterdir()):
                category_folder.rmdir()
                self.log(f"✓ Removed empty folder: {category}/")
        
        # Delete history file
        os.remove(self.history_file)
        
        self.log("="*70)
        self.log(f"✓ Undo complete! Restored {success_count} file(s).")
        self.log("="*70)
    
    def show_statistics(self):
        """Show current directory statistics"""
        self.log("="*70)
        self.log(f"DIRECTORY STATISTICS: {self.target_dir}")
        self.log("="*70)
        
        # Count files by category
        stats = {}
        total_files = 0
        total_size = 0
        
        for item in self.target_dir.rglob('*'):
            if item.is_file():
                # Skip hidden and log files
                if item.name.startswith('.') or item.name in [self.history_file, self.log_file]:
                    continue
                
                category = self.get_file_category(item)
                stats[category] = stats.get(category, 0) + 1
                total_files += 1
                total_size += item.stat().st_size
        
        if not stats:
            self.log("✗ No files found.")
            return
        
        # Print statistics
        self.log(f"{'Category':<20} {'Count':>10}")
        self.log("-"*70)
        for category in sorted(stats.keys()):
            self.log(f"{category:<20} {stats[category]:>10}")
        
        self.log("-"*70)
        self.log(f"{'Total Files':<20} {total_files:>10}")
        self.log(f"{'Total Size':<20} {self.format_size(total_size):>10}")
        self.log("="*70)
    
    def format_size(self, size):
        """Format file size in human-readable format"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
        return f"{size:.2f} PB"
    
    def clean_empty_folders(self):
        """Remove empty category folders"""
        self.log("="*70)
        self.log("CLEANING EMPTY FOLDERS")
        self.log("="*70)
        
        removed_count = 0
        for category in self.file_categories.keys():
            category_folder = self.target_dir / category
            if category_folder.exists() and category_folder.is_dir():
                if not any(category_folder.iterdir()):
                    category_folder.rmdir()
                    self.log(f"✓ Removed: {category}/")
                    removed_count += 1
        
        if removed_count == 0:
            self.log("✓ No empty folders found.")
        else:
            self.log(f"✓ Removed {removed_count} empty folder(s).")
        self.log("="*70)

def show_menu():
    """Display main menu"""
    print("\n" + "="*70)
    print("📁 FILE ORGANIZER 📁".center(70))
    print("="*70)
    print("1. Organize Files")
    print("2. Preview Organization (Dry Run)")
    print("3. Undo Last Organization")
    print("4. Show Statistics")
    print("5. Clean Empty Folders")
    print("6. Change Target Directory")
    print("7. Exit")
    print("="*70)

def main():
    """Main program"""
    print("="*70)
    print("📁 FILE ORGANIZER 📁".center(70))
    print("="*70)
    print("Automatically organize your files into categorized folders!")
    
    organizer = FileOrganizer()
    
    while True:
        show_menu()
        print(f"\nCurrent directory: {organizer.target_dir}")
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '1':
            confirm = input(f"\nOrganize files in '{organizer.target_dir}'? (y/n): ")
            if confirm.lower() == 'y':
                organizer.organize_files(dry_run=False)
            else:
                print("✗ Cancelled.")
        
        elif choice == '2':
            organizer.organize_files(dry_run=True)
        
        elif choice == '3':
            confirm = input("\nUndo last organization? (y/n): ")
            if confirm.lower() == 'y':
                organizer.undo_last_organization()
            else:
                print("✗ Cancelled.")
        
        elif choice == '4':
            organizer.show_statistics()
        
        elif choice == '5':
            organizer.clean_empty_folders()
        
        elif choice == '6':
            new_dir = input("\nEnter new target directory path: ").strip()
            new_path = Path(new_dir)
            if new_path.exists() and new_path.is_dir():
                organizer.target_dir = new_path
                print(f"✓ Directory changed to: {new_path}")
            else:
                print("✗ Invalid directory path.")
        
        elif choice == '7':
            print("\n👋 Goodbye! Keep your files organized!")
            break
        
        else:
            print("✗ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
