# File Organizer 📁

Automatically organize your messy downloads folder by categorizing files into neat folders.

## Features
- 🗂️ **Auto-Categorization** - Organizes files into 12+ categories
- 👀 **Dry Run Mode** - Preview changes before organizing
- ↩️ **Undo Function** - Reverse last organization
- 📊 **Statistics** - View file distribution and sizes
- 🧹 **Clean Empty Folders** - Remove unused category folders
- 📝 **Detailed Logging** - Track all operations
- 🎯 **Custom Directory** - Organize any folder, not just Downloads
- 🔄 **Smart Duplicate Handling** - Prevents file overwriting

## File Categories

The organizer sorts files into these categories:

| Category | File Types |
|----------|------------|
| **Images** | .jpg, .png, .gif, .bmp, .svg, .webp, etc. |
| **Videos** | .mp4, .avi, .mkv, .mov, .wmv, etc. |
| **Audio** | .mp3, .wav, .flac, .aac, .ogg, etc. |
| **Documents** | .pdf, .doc, .docx, .txt, .rtf, etc. |
| **Spreadsheets** | .xls, .xlsx, .csv, .ods |
| **Presentations** | .ppt, .pptx, .odp |
| **Archives** | .zip, .rar, .7z, .tar, .gz |
| **Code** | .py, .java, .js, .html, .css, etc. |
| **Executables** | .exe, .msi, .dmg, .app |
| **Books** | .epub, .mobi, .azw |
| **Design** | .psd, .ai, .sketch, .xd, .fig |
| **Data** | .json, .xml, .yaml, .sql, .db |

Files not matching any category go to **Others** folder.

## Requirements
```bash
# No external packages required - uses built-in Python libraries
```

## Usage
```bash
python file_organizer.py
```

## Menu Options

### 1. Organize Files
Automatically sorts all files in the target directory into categorized folders.

### 2. Preview Organization (Dry Run)
Shows what would happen without actually moving files. Perfect for testing!

### 3. Undo Last Organization
Restores files to their original locations before the last organization.

### 4. Show Statistics
Displays:
- Number of files per category
- Total file count
- Total directory size

### 5. Clean Empty Folders
Removes empty category folders to keep directory clean.

### 6. Change Target Directory
Organize any folder, not just Downloads.

## How It Works

**Before:**
```
Downloads/
├── vacation.jpg
├── report.pdf
├── song.mp3
├── video.mp4
└── archive.zip
```

**After:**
```
Downloads/
├── Images/
│   └── vacation.jpg
├── Documents/
│   └── report.pdf
├── Audio/
│   └── song.mp3
├── Videos/
│   └── video.mp4
└── Archives/
    └── archive.zip
```

## Example Session
```
📁 FILE ORGANIZER 📁

Current directory: /home/user/Downloads

1. Organize Files
2. Preview Organization (Dry Run)

Enter your choice: 2

[PREVIEW] vacation.jpg → Images/
[PREVIEW] report.pdf → Documents/
[PREVIEW] song.mp3 → Audio/

SUMMARY
Images: 1 file(s)
Documents: 1 file(s)
Audio: 1 file(s)

Total files previewed: 3
```

## Safety Features
- ✅ **Dry run mode** to preview changes
- ✅ **Undo functionality** to reverse changes
- ✅ **Duplicate handling** - never overwrites files
- ✅ **Detailed logging** of all operations
- ✅ **Skips system/hidden files**

## Files Created
- `organization_history.json` - History for undo function
- `file_organizer.log` - Detailed operation logs

## Tips
- 💡 Always run **dry run** first to preview changes
- 🔄 Use **undo** if you're not happy with results
- 📊 Check **statistics** regularly to see file distribution
- 🧹 Run **clean empty folders** to maintain tidiness
- 💾 Backup important files before organizing

## Customization
You can easily add custom categories by editing the `file_categories` dictionary in the code.

## Use Cases
- 🗂️ Organize messy Downloads folder
- 📚 Sort project files
- 🎨 Organize design assets
- 💼 Manage work documents
- 🎵 Sort media collections
