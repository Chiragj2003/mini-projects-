"""
Password Manager - Store encrypted passwords securely
Features:
- Add new passwords with encryption
- View stored passwords (decrypted)
- Search for passwords by account name
- Delete passwords
- Master password protection
- Data stored in encrypted format
"""

import json
import os
from cryptography.fernet import Fernet
import getpass
import hashlib
from pathlib import Path

class PasswordManager:
    def __init__(self):
        self.data_file = "passwords.json"
        self.key_file = "key.key"
        self.master_hash_file = "master.hash"
        self.cipher = None
        
    def generate_key(self):
        """Generate encryption key"""
        key = Fernet.generate_key()
        with open(self.key_file, 'wb') as key_file:
            key_file.write(key)
        return key
    
    def load_key(self):
        """Load encryption key"""
        if not os.path.exists(self.key_file):
            return self.generate_key()
        with open(self.key_file, 'rb') as key_file:
            return key_file.read()
    
    def hash_master_password(self, password):
        """Hash the master password"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def setup_master_password(self):
        """Setup master password for first time"""
        print("\n=== First Time Setup ===")
        while True:
            master_pass = getpass.getpass("Create a master password: ")
            confirm_pass = getpass.getpass("Confirm master password: ")
            
            if master_pass == confirm_pass:
                hashed = self.hash_master_password(master_pass)
                with open(self.master_hash_file, 'w') as f:
                    f.write(hashed)
                print("✓ Master password set successfully!")
                return True
            else:
                print("✗ Passwords don't match. Try again.")
    
    def verify_master_password(self):
        """Verify master password"""
        if not os.path.exists(self.master_hash_file):
            return self.setup_master_password()
        
        with open(self.master_hash_file, 'r') as f:
            stored_hash = f.read()
        
        attempts = 3
        while attempts > 0:
            master_pass = getpass.getpass("\nEnter master password: ")
            if self.hash_master_password(master_pass) == stored_hash:
                print("✓ Access granted!")
                return True
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"✗ Incorrect password. {attempts} attempts remaining.")
                else:
                    print("✗ Too many failed attempts. Exiting.")
                    return False
        return False
    
    def encrypt_password(self, password):
        """Encrypt a password"""
        return self.cipher.encrypt(password.encode()).decode()
    
    def decrypt_password(self, encrypted_password):
        """Decrypt a password"""
        return self.cipher.decrypt(encrypted_password.encode()).decode()
    
    def load_passwords(self):
        """Load passwords from file"""
        if not os.path.exists(self.data_file):
            return {}
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    
    def save_passwords(self, passwords):
        """Save passwords to file"""
        with open(self.data_file, 'w') as f:
            json.dump(passwords, f, indent=4)
    
    def add_password(self):
        """Add a new password"""
        print("\n=== Add New Password ===")
        account = input("Account/Website name: ").strip()
        username = input("Username/Email: ").strip()
        password = getpass.getpass("Password: ")
        
        passwords = self.load_passwords()
        
        if account in passwords:
            overwrite = input(f"Account '{account}' already exists. Overwrite? (y/n): ")
            if overwrite.lower() != 'y':
                print("✗ Cancelled.")
                return
        
        passwords[account] = {
            'username': username,
            'password': self.encrypt_password(password)
        }
        
        self.save_passwords(passwords)
        print(f"✓ Password for '{account}' saved successfully!")
    
    def view_passwords(self):
        """View all stored passwords"""
        passwords = self.load_passwords()
        
        if not passwords:
            print("\n✗ No passwords stored yet.")
            return
        
        print("\n" + "="*70)
        print("STORED PASSWORDS".center(70))
        print("="*70)
        
        for account, data in passwords.items():
            decrypted_pass = self.decrypt_password(data['password'])
            print(f"\n🔐 Account: {account}")
            print(f"   Username: {data['username']}")
            print(f"   Password: {decrypted_pass}")
        
        print("\n" + "="*70)
    
    def search_password(self):
        """Search for a specific password"""
        print("\n=== Search Password ===")
        search_term = input("Enter account name: ").strip()
        
        passwords = self.load_passwords()
        
        # Case-insensitive search
        found = False
        for account, data in passwords.items():
            if search_term.lower() in account.lower():
                decrypted_pass = self.decrypt_password(data['password'])
                print(f"\n🔐 Account: {account}")
                print(f"   Username: {data['username']}")
                print(f"   Password: {decrypted_pass}")
                found = True
        
        if not found:
            print(f"✗ No account found matching '{search_term}'")
    
    def delete_password(self):
        """Delete a password"""
        print("\n=== Delete Password ===")
        passwords = self.load_passwords()
        
        if not passwords:
            print("✗ No passwords stored.")
            return
        
        print("\nStored accounts:")
        for idx, account in enumerate(passwords.keys(), 1):
            print(f"{idx}. {account}")
        
        account = input("\nEnter account name to delete: ").strip()
        
        if account in passwords:
            confirm = input(f"Are you sure you want to delete '{account}'? (y/n): ")
            if confirm.lower() == 'y':
                del passwords[account]
                self.save_passwords(passwords)
                print(f"✓ Password for '{account}' deleted successfully!")
            else:
                print("✗ Cancelled.")
        else:
            print(f"✗ Account '{account}' not found.")
    
    def show_menu(self):
        """Display main menu"""
        print("\n" + "="*50)
        print("PASSWORD MANAGER".center(50))
        print("="*50)
        print("1. Add New Password")
        print("2. View All Passwords")
        print("3. Search Password")
        print("4. Delete Password")
        print("5. Exit")
        print("="*50)
    
    def run(self):
        """Main program loop"""
        print("="*50)
        print("🔐 SECURE PASSWORD MANAGER 🔐".center(50))
        print("="*50)
        
        # Verify master password
        if not self.verify_master_password():
            return
        
        # Load encryption key
        key = self.load_key()
        self.cipher = Fernet(key)
        
        while True:
            self.show_menu()
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                self.add_password()
            elif choice == '2':
                self.view_passwords()
            elif choice == '3':
                self.search_password()
            elif choice == '4':
                self.delete_password()
            elif choice == '5':
                print("\n👋 Goodbye! Your passwords are secure.")
                break
            else:
                print("✗ Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = PasswordManager()
    manager.run()
