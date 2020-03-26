# Напишите скрипт, позволяющий определить надежность вводимого
# пользователем пароля. Это задание является творческим: алгоритм
# определения надежности разработайте самостоятельно.
flag = True
while(flag):
    password = input('Enter your password: ')
    if len(password) <= 6:
        print("Password Strength is very low. Please try again")
    else:
        if len(password) <= 10:
            print("Password Strength is average.Please try again")
        else:
            if len(password) > 10:
                if password.isdigit():
                    print("pass should contain a-z, A-Z. Try again")
                else:
                    if password.isalpha():
                        print("pass should contain 0-9. Try again")
                    else:
                        if password.islower():
                            print("pass should contain A-Z. Try again")
                        else:
                            if password.isupper():
                                print("pass should contain a-z. Try again")
                            else:
                                flag = False
                            print("Password Strength is high")