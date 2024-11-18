# Terminal-Based-Password-Manager

## IMPLEMENTATION

### 1. CONFIGURE

- **Master Password**:  
  The first input during configuration; its hash will be saved in a file.

- **Device Secret Key (SALT)**:  
  Generated and stored in a file.

- **Master Key**:  
  - Combine the master password and salt.  
  - Pass through the hash function (PBKDF) to create a valid key for AES-256.

- **Encryption**:  
  The master key is used to encrypt/decrypt new entries.

- **Encrypted Fields**:  
  - Email  
  - Username  
  - Password  

- **Plain Fields**:  
  - Site Name  
  - URL  

---

### 2. ADD NEW ENTRIES

- **Master Password**: Ask for the master password.  
- **Validation**: Validate the master password by hashing and checking against the existing hash.  
- **Master Key**: Create a master key by hashing (DEVICE SECRET + MASTER PASSWORD).  
- **Input Fields**:  
  - Site name  
  - Site URL  
  - Email  
  - Username  
  - Password  
- **Encryption**: Encrypt email, username, and password with the master key and save to the database.

---

### 3. GET ENTRY

- **Search**: Input field to search by username, site name, URL, or email.  
- **Display**: Show all matching results (password hidden by default).  
- **Password Retrieval** (using the `-p` flag):  
  - Ask for the master password.  
  - Validate the master password by hashing and checking against the existing hash.  
  - Create the master key by hashing (DEVICE SECRET + MASTER PASSWORD).  
  - Decrypt the password and copy it to the clipboard.

---

## TASKS

- Create a SQL database.  
- Develop a basic terminal interface.  
- Implement a hash function.  
- Implement encryption and decryption using AES.  
- Add functionality to generate password suggestions.

---

## ADDITIONAL FEATURES

- Implement auto-copy functionality for passwords.  
- Require a master password to access the manager.  
- CLI for managing entries.  
- Generate random passwords (including alphabets, numbers, special characters).

---

## REQUIREMENTS

- Accept input for text, URL, or number.  
- Generate password suggestions.  
- Store passwords and site name/address in an SQL database.  
- Retrieve passwords and site name/address from the SQL database.  
- Implement auto-copy functionality for passwords using a library like `pyperclip`.

---

## TECHNOLOGIES USED

- **SQL**: SQLite3 (no installation required)  
- **Python**: Python 3.11.7  
- **Hash Function**: SHA-256  
- **Encryption**: AES-256  
- **Clipboard Management**: pyperclip  
- **Command-Line Interface**: argparse  
