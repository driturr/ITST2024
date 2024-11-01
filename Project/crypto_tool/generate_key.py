from cryptography.fernet import Fernet
import argparse

parser = argparse.ArgumentParser(description="""Generate and save an encryption key.\n
Requirement: 'file_name.key'\n 

(Example: generate_key.py secret.key)""")
parser.add_argument("file_name", help="The name of the file for the generated key (e.g.'secret.key').")
args = parser.parse_args()

def main():
    key = Fernet.generate_key()
    print(f"Key: {key}")

    with open(args.file_name, "wb") as key_file:
        key_file.write(key)
    print(f"A key has been saved to '{args.file_name}'.")

if __name__ == "__main__":
    main()