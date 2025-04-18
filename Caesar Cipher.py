def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    if mode == 'decrypt':
        shift = -shift  # Reverse the shift for decryption

    for char in text:
        if char.isalpha():
            # Shift within alphabet range
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char  # Keep non-alphabetic characters unchanged

    return result

if __name__ == "__main__":
    print("=== Caesar Cipher Tool ===")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))
    action = input("Type 'encrypt' or 'decrypt': ").strip().lower()

    if action in ['encrypt', 'decrypt']:
        output = caesar_cipher(message, shift, mode=action)
        print(f"\nResult ({action}ed): {output}")
    else:
        print("Invalid action. Please type 'encrypt' or 'decrypt'.")
