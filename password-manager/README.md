# Password Manager

A secure command-line password manager that encrypts and stores your passwords safely.

## Features
- 🔐 **Master Password Protection** - Secure access with a master password
- 🔒 **Military-Grade Encryption** - Uses Fernet symmetric encryption
- ➕ **Add Passwords** - Store passwords for different accounts
- 👀 **View Passwords** - View all stored passwords (decrypted)
- 🔍 **Search Functionality** - Quickly find passwords by account name
- 🗑️ **Delete Passwords** - Remove passwords you no longer need
- 💾 **Persistent Storage** - Data saved in encrypted JSON format

## Requirements
```bash
pip install cryptography
```

## Usage
```bash
python password_manager.py
```

### First Time Setup
1. Run the program
2. Create a master password (you'll need this every time)
3. Start adding your passwords

### Menu Options
1. **Add New Password** - Store a new account password
2. **View All Passwords** - Display all stored passwords
3. **Search Password** - Find a specific password
4. **Delete Password** - Remove a password entry
5. **Exit** - Close the program

## Security Features
- Master password hashed with SHA-256
- Passwords encrypted with Fernet (symmetric encryption)
- Password input hidden (not displayed on screen)
- Encryption key stored separately
- 3 attempts limit for master password

## Files Created
- `passwords.json` - Encrypted password storage
- `key.key` - Encryption key (keep this safe!)
- `master.hash` - Hashed master password

## ⚠️ Important Notes
- **Never share your master password**
- **Backup `key.key` file** - Without it, passwords cannot be decrypted
- **Keep files secure** - Don't commit these files to public repositories

## Example Usage
```
Enter master password: ****
✓ Access granted!

=== Add New Password ===
Account/Website name: Gmail
Username/Email: user@gmail.com
Password: ****
✓ Password for 'Gmail' saved successfully!
```
