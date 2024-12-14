import csv
import base64

def encode(string: str):
    string_to_byte = string.encode('utf-8')
    base64_encoded = base64.b64encode(string_to_byte)
    return base64_encoded.decode('utf-8')

def decode(string: str):
    string_to_byte = string.encode('utf-8')
    base64_decoded = base64.b64decode(string_to_byte)
    return base64_decoded.decode('utf-8')

def check_username(username: str, file: list):
    if len(username) == 0:
        return False, "The length should be greater than 0"
    if ' '  in username:
        return False, "You cannot use spaces in username"
    if username[0].isnumeric():
        return False, "First character cannot be a number"
    if username in file:
        return False, "The username already exists"
    return True, "Success"

def check_password(password: str):
    if len(password) < 8:
        return False, "The length of the password should be more than eight letters"
    return True, "Success"

def find_username(user_name, file):
    for line in file:
        if decode(line['user_name']) == user_name:
            return [decode(line['user_name']), decode(line['password']), line['status']]
    return None

login = False
while True:
    if login is False:
        print("Hello there!, Would you like to login or Sign-up.")
        print("1 for login")
        print("2 for signup")
        print("3 to exit")
    else:
        print("Press 1 to logout!")

    user_inp = int(input())
    if user_inp == 1:
        if login:
            print("Signing out! Hope to see you soon!")
            login = False
        else:
            with open('details.csv' , 'r') as details:
                reader = csv.DictReader(details)
                user_name = input("Please enter your username: ")
                user = None
                while True:
                    if user_name == '':
                        print("Please enter a valid username: ")
                    else:
                        file = list()
                        for line in reader:
                            file.append({'user_name': line['user_name'], 'password': line['password'], 'status': line['status']})
                        user = find_username((user_name), file)
                        break
                password = input("Please enter your password: ")

                if (user is not None and user[0] == user_name and user[1] == password):
                    login = True
                    print(f"Welcome {user_name}!")
                else:
                    print("Invalid Credentials!")
    elif user_inp == 2 and not login:
        l = list()
        with open('details.csv', 'r') as det:
            reader = csv.DictReader(det)
            for line in reader:
                l.append(decode(line['user_name']))


        with open('details.csv', 'a+') as details:
            writer = csv.DictWriter(details, fieldnames=['user_name', 'password', 'status'])
            while True:
                user_name = input("Please enter your username: ")
                suc, mess = check_username(user_name, l)
                if suc:
                    break
                else:
                    print(mess)


            while True:
                password = input("Please enter your password: ")
                suc, msg = check_password(password)
                if suc:
                    break
                else:
                    print(msg)

            confirm_password = input("Please confirm your password: ")

            while True:
                if password == confirm_password:
                    status = input("Please enter a status: ")
                    dic = dict()
                    dic['user_name'] = encode(user_name)
                    dic['password'] = encode(password)
                    dic['status'] = status
                    writer.writerow(dic)
                    break
                else:
                    print("Wrong password!!!")

    elif (user_inp == 3 and not login):
        break
    else:
        print("Please enter a valid value: ")