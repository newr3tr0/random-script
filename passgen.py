import random
import argparse
import string

def generate_password(length, uppercase, lowercase, digits, special_chars):
    """
    This function generates a random password based on the specified criteria.
    """
    all_chars = ''
    if uppercase:
        all_chars += string.ascii_uppercase
    if lowercase:
        all_chars += string.ascii_lowercase
    if digits:
        all_chars += string.digits
    if special_chars:
        all_chars += string.punctuation

    password = ''.join(random.choice(all_chars) for i in range(length))
    return password

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a random password.')
    parser.add_argument('length', help='the length of the password', type=int)
    parser.add_argument('--no-uppercase', dest='uppercase', help='do not include uppercase letters', action='store_false')
    parser.add_argument('--no-lowercase', dest='lowercase', help='do not include lowercase letters', action='store_false')
    parser.add_argument('--no-digits', dest='digits', help='do not include digits', action='store_false')
    parser.add_argument('--no-special-chars', dest='special_chars', help='do not include special characters', action='store_false')
    args = parser.parse_args()

    length = args.length
    uppercase = args.uppercase
    lowercase = args.lowercase
    digits = args.digits
    special_chars = args.special_chars

    password = generate_password(length, uppercase, lowercase, digits, special_chars)
    print(password)
