#(Command / to comment all)
print('Age Calculator!')
#Current Year:
c_year = input('What is the current year? ')
while not c_year.isdigit():
    print('Please enter a valid year...')
    c_year = input('What is the current year? ')
    c_year = c_year
for response in c_year:
    #Birth Year:
    b_year = input('In what year were you born? ')
    while not b_year.isdigit():
        print('Please enter a valid year...')
        b_year = input('In what year were you born? ')
        b_year = b_year
    for response in b_year:
        #Calculations:
        c_year = int(c_year)
        b_year = int(b_year)
        calc = print('Thank you for your response!\nYou are', c_year - b_year, 'years old.')
        exit()
