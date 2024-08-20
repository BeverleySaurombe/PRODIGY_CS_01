def caesar_cipher(message, shift, mode):
    result = ""
    
    # Adjust the shift for decryption
    if mode == "decrypt":
        shift = -shift
    
    # Loop through each character in the message
    for char in message:
        # Check if character is an uppercase letter
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If it's not a letter, leave it unchanged
            result += char
            
    return result

def main():
    # Get the user input for the message, shift, and mode
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    
    if mode in ["encrypt", "decrypt"]:
        result = caesar_cipher(message, shift, mode)
        print(f"The {mode}ed message is: {result}")
    else:
        print("Invalid mode selected. Please choose either 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
