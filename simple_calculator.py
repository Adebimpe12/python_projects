print('''
    My ALATA Calculator
    1. Addition
    2. Subtraction
    3. Division
    4. Multiplication
      ''')
user = input('option: ')
first_value = float(input ('First Value: '))
second_value = float(input ('Second Value: '))

if user == '1':
    res = first_value + second_value
    print(f'Answer: {res}')
elif user == '2':
    res = first_value - second_value
    print(f'Answer: {res}')
elif user == '3':
    res = first_value / second_value
    print(f'Answer: {res}')
elif user == '4':
    res = first_value * second_value
    print(f'Answer: {res}')
elif user == '*':
    exit()
else :
    print('Invalid Option')
