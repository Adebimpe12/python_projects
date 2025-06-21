class GuessGame:
    def __init__(self):
        self.myset = {1, 5, 9, 3, 8, 2, 4, 7, 6, 10}
        self.score = 0
    def home(self):        
        x = 0
        while x < 5:
            guess = int(input('guess a number from 1-10: '))
            chosen_number = self.myset.pop()
            self.myset.add(chosen_number)
            print(chosen_number)
            if guess == chosen_number:
                print('You guessed right. ')
                self.score += 5
            else:
                print(f'wrong')
                self.score -= 5
            x += 1
            print(f'Your score is {self.score}')
        user = input('press 1 to replay or # to exit')
        if user == '#':
            exit()
        elif user == '1':
            self.home()
        else:
            print('Game over!')
        
        

guess_game = GuessGame()
guess_game.home()