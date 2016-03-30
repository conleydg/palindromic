import re
import sys

file_name = sys.argv[1]

with open(file_name, 'r') as f:
    content = f.readlines()


def is_palindrome(string):
    pattern = r'[^A-Za-z]'
    user_input = re.sub(pattern, "", string).lower()
    if len(user_input) < 2:
        return True
    elif user_input[0] == user_input[-1]:
        return is_palindrome(user_input[1:-1])
    return False

def main():
    for string in content:
        if is_palindrome(string):
            print(string,  ': is a palindrome')
        else:
            print(string, ': is not a palindrome')



if __name__ == "__main__":
    main()






# for line in argv(1):
#     print(line)
