from csv import DictWriter

with open('details.csv', 'w') as details:
    writer = DictWriter(details, fieldnames=['user_name', 'password', 'status'])
    writer.writeheader()