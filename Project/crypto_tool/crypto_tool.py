from cryptography.fernet import Fernet
import argparse
import os

#load the encryption key
def load_key(key_file):
    try:
        with open(key_file, 'rb') as key_f:
            key = key_f.read()
            print(f"Key loaded from '{key_file}'")
            return key
    except FileNotFoundError:
        print(f"Error: The key '{key_file}' was not found.")
    except Exception as e:
        print(f"Error loading key file '{key_file}': {e}")

#encrypt the specified file and save results. Loading key from main()
def encrypt_file(key, file_name, save_file):
    try:
        cipher_suite = Fernet(key)

        with open(file_name, 'r') as file:
            message = file.read().encode()
        
        cipher_text = cipher_suite.encrypt(message)

        with open(save_file, 'wb') as encrypted_f:
            encrypted_f.write(cipher_text)
    
        print(f"The file '{file_name}' has been encrypted and saved to '{save_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"Error during encryption of '{file_name}': {e}")

#decrypt the specified file and save results. Loading key from main()
def decrypt_file(key, file_name, save_file):
    try:
        cipher_suite = Fernet(key)

        with open (file_name, 'rb') as encrypted_f:
            cipher_text = encrypted_f.read()

        decrypted_message = cipher_suite.decrypt(cipher_text)

        with open(save_file, 'w') as decrypted_f:
            decrypted_f.write(decrypted_message.decode())
        
        print(f"The file '{file_name}' has been decrypted and saved to '{save_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"Error during decryption of '{file_name}': {e}")


def main():
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

    #Validate if files exists
    if not os.path.isfile(args.key_file):
        print(f"Error: The key file '{args.key_file}' does not exist.")
        return
    if not os.path.isfile(args.file_name):
        print(f"Error: The file '{args.file_name}' does not exist.")

    #loading the key
    key = load_key(args.key_file)
    if key is None:
        print("Failed to load the encryption key. Exiting...")
        return
    
    #run "encrypt" or "decrypt" mode
    if args.mode == "encrypt":
        encrypt_file(key, args.file_name, args.save_file)
    elif args.mode == "decrypt":
        decrypt_file(key, args.file_name, args.save_file)

if __name__ == "__main__":
    main()