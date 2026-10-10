def caesar_decrypt(ciphertext, shift):
    """
    Decrypts a Caesar cipher text by shifting characters backward.
    """
    plaintext = ""
    for char in ciphertext:
        # Decrypt uppercase letters
        if char.isupper():
            plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
        # Decrypt lowercase letters
        elif char.islower():
            plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
        # Leave spaces and punctuation as they are
        else:
            plaintext += char
    return plaintext

def brute_force_caesar(ciphertext):
    """
    Prints all 25 possible decryptions for a given ciphertext.
    """
    print("\n--- Running Brute Force Decryption ---")
    for shift in range(1, 26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        print(f"Key {shift:02d}: {decrypted_text}")

# --- Main Program Execution ---
if __name__ == "__main__":
    print("=== Caesar Cipher Solver ===")
    cipher_input = input("Enter the encrypted message: ")
    
    choice = input("Do you know the shift key? (yes/no): ").strip().lower()
    
    if choice in ['yes', 'y']:
        try:
            key = int(input("Enter the shift key (1-25): "))
            result = caesar_decrypt(cipher_input, key)
            print(f"\nDecrypted Message: {result}")
        except ValueError:
            print("Invalid input. Please enter an integer for the key.")
    else:
        brute_force_caesar(cipher_input)