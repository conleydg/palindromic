import re

def is_palindrome(string):
    pattern = r'[^A-Za-z]'
    user_input = re.sub(pattern, "", string).lower()
    while len(user_input) > 2:
        if user_input[0] == user_input[-1]:
            return user_input[0:-1]
        return False


def main():
    user_input = input('Please enter a word or sentence to check if it is a palindrome: ')
    if is_palindrome(user_input):
        print('is a palindrome')
    else:
        print('is not a palindrome')


if __name__ == "__main__":
    main()
