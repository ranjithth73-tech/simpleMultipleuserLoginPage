users = {}

while True:
    print('Enter Your Details')
    print('===================')
    name = input('What Is Your Name : ')
    email = (input('What Is your Email : '))
    place = input('Enter Your Place : ')
    phone = (input('Enter Your Phone Number : '))
    username = input('Create A User Name : ')
    password = input('Create A Password : ')

    if username not in users:
        users[username] = {
            'password': password,
            'name': name,
            'email': email,
            'place': place,
            'phone': phone
        }

    print('Registration Completed Successfully')
    choice = input('Do You Want To Login Now? Yes/No : ')
    if choice.lower() not in ['no']:
        break
    else:
        continue
print('================================')
print('             LOG IN             ')
print('================================')
logsuccess = False

while not logsuccess:
    logusr = input('Enter Your Username : ')
    logpass = input('Enter Your Password : ')
    print('---------------------------------')
    if logusr in users and users[logusr]['password'] == logpass:
        print('!!!Login Completed Successfully!!')
        print('Welcome\n Mr.', users[logusr]['name'])
        print('Email :', users[logusr]['email'])
        print('Phone :', users[logusr]['phone'])
        print('Place :', users[logusr]['place'])
        break
    else:
        print('Enter Correct Details, Try again!')
