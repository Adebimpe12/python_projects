print('''
    My Set Calculator
    1. Union
    2. Intersection
    3. Difference
      ''')
user = input('option: ')
SetA = {}
SetA.update(input ('SetA: '))
SetB = {} 
SetB.update(input ('SetB: '))


if user == '1':
    print(SetA.union(SetB))
    
elif user == '2':
    print(SetA.intersection(SetB))

elif user == '3':
    print(SetA.difference(SetB))

elif user == '*':
    exit()
else :
    print('Invalid Option')

    
