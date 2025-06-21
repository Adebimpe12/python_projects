print(name.center())
name = input('Your name: ')
user = input("Press enter to start the test or '1' to exit")
score = 0

if user == '1':
    exit()
else:
    print('Who is the president of nigeria\na.) buhari b.) BAT')
    user = input('Answer: ').strip().capitalize()
    if user == 'B':
        print('correct')
        score +=5
    else:
        print('Olodo ni e jor')

print('2. Capital of france\na.) Paris b.) London')
user = input('Answer: ').strip().capitalize()
if user == 'A':
    print('correct')
    score += 5

print(f'Thanks for taking the test {name}, your total score is {score}')

