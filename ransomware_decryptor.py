import os
from cryptography.fernet import Fernet

def load_key(key_file='secret.key'):
    """
    Loads the Fernet key from the given key file.
    """
    with open(key_file, 'rb') as f:
        return f.read()

def decrypt_file(file_path, key):
    """
    Decrypts a file using the provided key and writes the decrypted
    data to a new file with the '.encrypted' extension removed.
    """
    fernet = Fernet(key)
    
    # Read the encrypted file data
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    
    # Decrypt the data
    decrypted_data = fernet.decrypt(encrypted_data)
    
    # Generate the original filename by removing the '.encrypt' extension
    if file_path.endswith('.encrypted'):
        original_file_path = file_path[:-len('.encrypted')]
    else:
        # Fallback: append '.decrypted' if the extension isn't found (shouldn't happen)
        original_file_path = file_path + '.decrypted'
    
    # Write the decrypted data to the new file
    with open(original_file_path, 'wb') as file:
        file.write(decrypted_data)
    
    print(f"Decrypted file saved as: {original_file_path}")

def decrypt_files_in_directory(directory, key):
    """
    Recursively decrypts all files ending with '.encrypted' in the given directory.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.encrypted'):
                full_path = os.path.join(root, file)
                decrypt_file(full_path, key)

if __name__ == '__main__':
    # Load the Fernet key from secret.key
    key = load_key('secret.key')
    
    # Decrypt all files ending with '.encrypt' in the current directory and subdirectories
    decrypt_files_in_directory('.', key)
