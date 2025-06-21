import re


def check_for_password(password):

    pattern = r'[a-z][A-Z}{8}'
   
    matches = re.match(pattern, password)
    # print(matches)

    if matches:
        print("Valid Password")
    else:
        print('Invalid Password')

inp = input('Password: ')


check_for_password(inp)