import csv
import base64
from fileinput import close


def encode(string: str):
    string_to_byte = string.encode('utf-8')
    base64_encoded = base64.b64encode(string_to_byte)
    return base64_encoded.decode('utf-8')

def decode(string: str):
    string_to_byte = string.encode('utf-8')
    base64_decoded = base64.b64decode(string_to_byte)
    return base64_decoded.decode('utf-8')

while True:
    print("Hello there!, Would you like to login or Sign-up.")
    print("1 for login")
    print("2 for signup")

    user_inp = int(input())
    if user_inp == 1:
        with open('details.csv' , 'r') as details:
            reader = csv.DictReader(details)

    elif user_inp == 2:
        with open('details.csv', 'a') as details:
            writer = csv.DictWriter(details, fieldnames=['user_name', 'password', 'status'])

            user_name = input("Please enter your username: ")
            password = input("Please enter your password: ")
            confirm_password = input("Please confirm your password: ")

            if (password == confirm_password):
                status = input("Please enter a status: ")
                dic = dict()
                dic['user_name'] = encode(user_name)
                dic['password'] = encode(password)
                dic['status'] = status
                writer.writerow(dic)
            else:
                print("Wrong password!!!")



    else:
        print("Please enter a valid value: ")