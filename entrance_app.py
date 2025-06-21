# Entrance app at school gate
# Are you a staff/visitor/student
# visitor will go to the front desk, enter
# student database, if name found, enter
# payment status, fully paid say enter,
# half payment say pay soon,
# no payment

student_db = [
    ('Tolu', 'paid')
    ('Maimunat', 'half-paid')
    ('Habeeb', 'not-paid')
]

staff_db = [
    ('Femi', '21')
    ('Yemi', '02')
]

user = input('''
            Welcome to SQI College of ICT
    
    Kindly clarify your identity
    1. Staff
    2. Student
    3. Visitor
    4. None of the above
      
    option: 
''').strip()




if user == '1' or user.capitalize() == 'Staff':
    staff_id = input('ID: ').strip()
    staff_fname = input('First name: ').strip().capitalize()

    fnames = []
    IDs = []

    for fname, id in staff_db:
        fnames.append(fname)
        IDs.append(id)

    if staff_fname in fnames and staff_id in IDs:
        print('Acess granted 😁')
    else:
        print('Acess denied')

elif user == '2' or user.capitalize() == 'Student':
    student_fname = input('First name: ').strip().capitalize()

    student_firstnames = []
    payment_status = []

    for stud, status in status_db:
        student_firstnames.append(stud)
        payment_status.append(status)

    if student_fname in student_firstnames:
        print(f'Welcome {student_fname}, Kindly wait, lets verify your payment status')

        _index = student_firstnames.index(student_fname)
        _status = payment_status[_index]
        print(status)

        if _status == 'Paid':
            print(f'Great, Welcome to class {student_fname}')
        else:
            print(f"{student_fname}, Your payment status is '{_status}', Kindly visit the frontdesk for clarification.")










user = input('Are you a student, yes or no? ').strip().lower()
if user == 'yes':
    input('Have you paid your fees, yes or no or half? ').strip().lower()
    if user == 'yes':
        print('Enter')
    elif user == 'half':
        print('Pay your fees soon')
    else user == 'no':
        print('Pay your fees soon')
else:
    exit()

user = input('Are you a visitor, yes or no? ').strip().lower()
if user == 'yes':
    print('Proceed to the front desk')
else:
    exit()

user = input('Are you a staff, yes or no? ').strip().lower()
if user == 'yes':
    input('Enter staff id: ')
    print('Enter')
else:
    exit()