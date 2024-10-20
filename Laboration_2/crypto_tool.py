from cryptography.fernet import Fernet
import argparse

parser = argparse.ArgumentParser(description="""Tool for encrypting and decrypting a file using a symmetric key.
\n|| To generate a new symmetric key, use the script 'generate_key.py'.
\n|| Requirement: mode('encrypt' or 'decrypt') + 'key_file' + 'file_name' + 'save_file' .
\n|| Example to encrypt:\n crypto_tool.py encrypt --key_file secret.key --file_name message.txt --save_file encrypted_message.enc
\n|| Example to decrypt:\n crypto_tool.py decrypt --key_file secret.key --file_name encrypted_message.enc --save_file decrypted_message.txt
""")
parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Modes possible: 'encrypt' or 'decrypt'.\n To encrypt a file use 'encrypt'. To decrypt a file use 'decrypt'.")
parser.add_argument("--key_file", help="The name of the file containing the key for encrypting or decrypting.")
parser.add_argument("--file_name", help="The name of the file to encrypt or decrypt.")
parser.add_argument("--save_file", help="The name of the file to save the encrypted or decrypted file.")

args = parser.parse_args()

if args.mode == "encrypt":
    with open(args.key_file, 'rb') as key_f:
        key = key_f.read()
    cipher_suite = Fernet(key)

    with open(args.file_name, 'r') as file:
        message = file.read().encode()
    cipher_text = cipher_suite.encrypt(message)

    with open(args.save_file, 'wb') as encrypted_f:
        encrypted_f.write(cipher_text)
    
    print(f"The file '{args.file_name}' has been encrypted and saved to '{args.save_file}'.")


elif args.mode == "decrypt":
    with open(args.key_file) as key_f:
        key = key_f.read()
    cipher_suite = Fernet(key)

    with open (args.file_name, 'rb') as encrypted_f:
        cipher_text = encrypted_f.read()
    decrypted_message = cipher_suite.decrypt(cipher_text)

    with open(args.save_file, 'w') as decrypted_f:
        decrypted_f.write(decrypted_message.decode())
    
    print(f"The file '{args.file_name}' has been decrypted and saved to '{args.save_file}'.")