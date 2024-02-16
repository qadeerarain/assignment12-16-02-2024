#8. Password Guesser:
# 

import random
import string

def generate_password(password_length, include_lowercase, include_uppercase, include_numbers, include_symbols):
    characters = ''
    
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: No character types selected. Please include at least one character type.")
        return None

    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    return generated_password

def main():
    password_criteria = {
        'length': 12,
        'include_lowercase': True,
        'include_uppercase': True,
        'include_numbers': True,
        'include_symbols': True
    }

    generated_password = generate_password(**password_criteria)

    if generated_password:
        print(f"Generated Password: {generated_password}")

if __name__ == "__main__":
    main()
