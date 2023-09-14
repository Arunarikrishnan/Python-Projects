import random

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_char, additional_chars):
    # Define character sets
    lowercase_chars = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digit_chars = '0123456789'
    special_chars = '!@#$%^&*()_+[]{}|;:,.<>?'
    
    # Add user-defined characters to the character set
    character_sets = []
    if use_lowercase:
        character_sets.append(lowercase_chars)
    if use_uppercase:
        character_sets.append(uppercase_chars)
    if use_digits:
        character_sets.append(digit_chars)
    if use_special_char:
        character_sets.append(special_chars)
    if additional_chars:
        character_sets.append(additional_chars)
      
    # Generate the password
    password = ''
    for _ in range(length):
        char_set = random.choice(character_sets)
        password += random.choice(char_set)

    return password

# Get user preferences
while True:
    length_str = input("Enter the length of the password: ").strip()
    if length_str.isdigit():
        length = int(length_str)
        break
    else:
        print("Invalid input. Please enter a valid integer for the password length.")

use_lowercase = input("Use lowercase letters? (yes/no): ").lower() == 'yes'
use_uppercase = input("Use uppercase letters? (yes/no): ").lower() == 'yes'
use_digits = input("Use digits? (yes/no): ").lower() == 'yes'
use_special_char = input("Use special characters? (yes/no): ").lower() == 'yes'
additional_chars = input("Enter additional characters to include (leave empty for none): ")

# Generate and print the password
password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_char, additional_chars)
if password:
    print("Generated Password:", password)
