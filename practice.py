import re
import csv

file_name = 'potential-contacts.txt'

try:
    with open(file_name, 'r') as potential_contacts:
        contents = potential_contacts.read()
        # print(contents)
        print(type(contents))
        contents.split(' ')
        # for x in contents.split(' '):
        #     if x[0] == 's':
        #         print('i found a number!: ', x)
        phones = re.findall(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', contents)

        # for phone in phones:
        #     print('Phone:', phone)
        

except FileNotFoundError as err:
    print('i found an error\n', err)


def csvs():

    file_name = 'test_propellers.csv'

    try:
        with open(file_name) as info:
            contents = csv.reader(info, delimiter=',')
            line = 0
            for row in contents:
                if line == 0:
                    print(f'headers are: {row}')
                    line += 1
                else:
                    print(f'data is {row}')
            # print(type(contents))
            # for i in contents[:10]:
            #     print(i)
    except FileNotFoundError as err:
        print("Went to exeption, err= \n", err)

csvs()