from cryptography.fernet import Fernet
import unittest

def generate_key() -> bytes:
    return Fernet.generate_key()

def load_key() -> bytes:
    return generate_key()

def aes_encrypt(text: str, key: bytes) -> str:
    
    fernet = Fernet(key)
    return fernet.encrypt(text.encode()).decode()

def aes_decrypt(text: str, key: bytes) -> str:
    
    fernet = Fernet(key)
    return fernet.decrypt(text.encode()).decode()

# Unit Tests
class TestEncryptionProgram(unittest.TestCase):
    def setUp(self):
         
        self.key = load_key()
        self.text = "Hello, World!"
        self.encrypted_text = aes_encrypt(self.text, self.key)

    def test_aes_encrypt(self):
        
        encrypted = aes_encrypt(self.text, self.key)
        self.assertNotEqual(encrypted, self.text)
        self.assertIsInstance(encrypted, str)

    def test_aes_decrypt(self):
        
        decrypted = aes_decrypt(self.encrypted_text, self.key)
        self.assertEqual(decrypted, self.text)

    def test_round_trip(self):
         
        encrypted = aes_encrypt(self.text, self.key)
        decrypted = aes_decrypt(encrypted, self.key)
        self.assertEqual(decrypted, self.text)

def main():
    key = load_key()
    print("=== Data Encryption Program ===")
    while True:
        print("\nOptions:")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == "1":
            text = input("Enter text to encrypt: ")
            encrypted_text = aes_encrypt(text, key)
            print(f"Encrypted Text: {encrypted_text}")
        
        elif choice == "2":
            text = input("Enter text to decrypt: ")
            try:
                decrypted_text = aes_decrypt(text, key)
                print(f"Decrypted Text: {decrypted_text}")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    unittest.main(exit=False)
    main()
