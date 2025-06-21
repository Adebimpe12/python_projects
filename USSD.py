user_ussd = input('USSD Code: ')
if user_ussd == '*312#':
    print('''
    1. Data Plan
    2. Check balance
    ''')

    option = input('option:') 
    if option == '1':
        print('''
            DATA PLAN
            1. Daily Plan
            2. Weekly Plan
            3. Monthly Plan
            ''')
        
        choice = input('Choice: ')
        if choice == '1':
            print('Daily Plan')
        elif choice == '2':
            print(' Weekly Plan')
        elif choice == '3':
            print('Monthly Plan')
        else:
            print('Invalid Service Code')

        user = input ('autorenew, yes or no?')
        if user == 'yes':
            print('autorenew successful')
        elif user == 'no':
            print('autorenew declined')
        else:
            exit()

    elif option == '2':
        print('Your main balance is N54.56')
    else:
        print('Invalid Service Code')
        exit()







