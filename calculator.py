# Calculator using functions and class

class Calculator:
    def __init__(self):
        self.Ans = 0

    def home(self):
        print('''
        My Calculator
        1. Addition
        2. Subtraction
        3. Division
        4. Multiplication
        #. Exit
        ''')

        self.user = input('option: ')
        self.first_value = float(input ('First Value: '))
        self.second_value = float(input ('Second Value: '))
    
        if self.user == '1':
            self.Ans = self.addition()
        elif self.user == '2':
            self.Ans = self.subtraction()
        elif self.user == '3':
            self.Ans = self.division()
        elif self.user == '4':
            self.Ans = self.multiplication()
        else:
            print('Invalid option. Try again.')
            self.home()

        print(f'Answer = {self.Ans}')
        self.decision()
            
        if self.user == '#':
            exit()     

    def addition(self):
        return self.first_value + self.second_value
                   
    def subtraction(self):
        return self.first_value - self.second_value
                   
    def division(self):
        return self.first_value / self.second_value
    
    def multiplication(self):
        return self.first_value * self.second_value
         
    def decision(self):
        self.user = input('Press 1 to home or # to exit')
        if self.user == '1':
            self.home()
        else:
            exit
        
calculator = Calculator()
calculator.home()
