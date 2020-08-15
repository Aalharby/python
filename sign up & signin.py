def main():
    print('this is sign up/signin page\n')
    user_name= input('Enter the user name: ')
    password=input('Enter the password: ')
    verify_password=input('Enter the password again: ')
    if verify_password == password:
        print('successfully sign up')
        print('\nsignin\n')
        current_user_name = input('Enter the user name: ')
        current_password = input('Enter the password: ')
        if current_user_name == user_name and current_password == password:
            print('successfully sign in')
        else:
            print('fail in signin, user name or password wrong please try again')
    else:
        print('fail in sign up, user name or password wrong please try again')

if __name__ =='__main__':main()
