import string
import random
LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation
# print(string.printable)

def password_generator(length):
    printable = f"{LETTERS}{NUMBERS}{PUNCTUATION}"
    printable = list(printable)
    random.shuffle(printable)
    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    return random_password

def password_length():
    password_length = input("How long do you want your password: ")
    return int(password_length)

def main():
    password = password_generator(password_length())
    print(password)

if __name__ == "__main__":
    main()