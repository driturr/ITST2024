# Crypto Tool
Crypto Tool is a Python-based tool for file encryption and decryption using a symmetric encryption key generated with Fernet. The toolkit includes two scripts:  
- `generate_key.py` to create and store a symmetric key
- `crypto_tool.py` to encrypt or decrypt a file using a specified key  

**`generate_key.py`**  
Generates a new Fernet encrytion key and saves it to a specified file. This key is used to both encrypt and decrypt files.

**`crypto_tool.py`**  
Encrypts or decrypts a specified file using a key provided in the `key_file`. The tool verifies that all in put files exist before proceeding to perform encryption or decryption, and displays error messages for any missing files.

## Installation
### Required Python Packages
This script runs in Python3, therefore make sure you have Python installed. You will need the `cryptography` package. You can install the required package using pip:
```bash
pip3 install cryptography
```

### Clone the repository  
1. Clone this repo to your local machine
`git clone https://github.com/dirturr/ITST2024/Project/crypto_tool.git`  

2. Install the required libraries:  
`pip3 install -r requirements.txt`

3. Run the script: 
`python3 crypto_tool.py <mode> --key_file <key_file> --file_name <file_name> --save_file <save_file>`

You need a key to run the script. You can generate a key using the script `generate_key.py`  

## Usage
### 1. Generating an Encryption Key

Use `generate_key.py` to generate and save a new encryption key.  

The key is saved to a file specified by the user, which can then be used for both encryption and decryption.

**Command**  
```bash
python3 generate_key.py <key_file>
```
**Arguments**  
- <key_file>: The file to save the generated key (e.g. `secret.key`)

Example: `python3 generate_key.py secret.key`  


### 2. Encrypting and Decrypting Files

Use crypto_tool.py to encrypt or decrypt files with a key.

**Command**  
```bash
python3 crypto_tool.py <mode> --key_file <key_file> --file_name <file_name> --save_file <save_file>
```

**Arguments**
- <mode>: Choose `encrypt` or `decrypt`.
- `--key_file`: Path to the key file containing the encryption key.
- `--file_name`: Path to the file to be encrypted or decrypted.
- `--save_file`: Path to save the encrypted ro decrypted ouput.

Examples:
- **Encrypting a file**:
```bash
python3 crypto_tool.py encrypt --key_file secret.key --file_name message.txt --save_file encrypted_message.enc
```
This command encrypts `message.txt` and saves the encrypted file as `encrypted_message.enc`.  


- **Decrypting a file**:
```bash
python3 crypto_tool.py decrypt --key_file secret.key --file_name encrypted_message.enc --save_file decrypted_message.txt
```
This command decrypts `encrypted_message.enc` and saves the decrypted content as `decrypted_message.txt`.

## Error Handling
- Checks if the specified key file or file to encrypt/decrypt exists before running.
- Print clear error messages if files are not found or if there are issues during the encryption/decryption process.
- If the key cannot be loaded, the tool will exit.

## Known Limitations
- It only supports symmetric encryption with Fernet.
- It does not support encrypting directories or non-text file formats.

## Contributing
To contribute:

1. Fork the repository.
2. Create a new branch for your feature.
3. Submit a pull request when done.

Contributions welcome!