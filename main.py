import random
import string
import subprocess

def copy_to_clipboard(password):
    subprocess.run(['pbcopy'], input=password.encode('utf-8'))

def generate_password(length, use_uppercase, use_number, use_symbols):
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    digit_chars = string.digits if use_number else ''
    symbol_chars = string.punctuation if use_symbols else ''

    # Make sure at least one character type is included
    required_chars = ''.join(random.choice(chars) for chars in [uppercase_chars, digit_chars, symbol_chars] if chars)

    # Calculate how many characters are remaining to reach the desired length
    remaining_length = length - len(required_chars)

    # Combine all character sets for password generation
    all_chars = lowercase_chars + uppercase_chars + digit_chars + symbol_chars

    # Generate the remaining characters randomly
    random_chars = ''.join(random.choice(all_chars) for _ in range(remaining_length))

    # Combine required and random characters and shuffle them
    password = required_chars + random_chars
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def main():
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include at least one uppercase character? (yes/no): ").lower() == 'yes'
    use_number = input("Include at least one number? (yes/no): ").lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    password = generate_password(length, use_uppercase, use_number, use_symbols)
    print("Generated Password:", password)

    copy_to_clipboard(password)
    print("Password copied to the clipboard.")

if __name__ == "__main__":
    main()
