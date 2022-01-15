#Global Variables
SPECIAL= '@%!$*'
YEAR=[1900,2020]
PASSWD_LENGHT=(12,25)

def main():
    user={'VINNIEG@YMAIL.COM': 'trains2000',
          'ENZOG@GMAIL.COM': 'Zootopia1234',
          'MATINZAK@YMAIL.GOV': 'tails1234',
          'RECEIVERFRED@QMAIL.EDU': 'Starplatinum1234',
          'GUIGUIGUI@ZMAIL.GOV': 'dark1234'}     #dictionary with 5 users and passwords
    user_data=[['VINNIE ESCOBAR', '03/11/1982', '517 748 9955', '300', 'trains2000', 'VINNIEG@YMAIL.COM'],
['ENZO ESCOBAR', '07/19/1992', '517 839 8877', '400', 'Zootopia1234', 'ENZOG@GMAIL.COM'],
['MARTIN ZAK', '12/11/1977', '919 245 7658', '1000', 'tails1234', 'MATINZAK@YMAIL.GOV'],
['FRANCIS FLORENS', '05/19/2012', '414 183 5726', '4000', 'Starplatinum1234', 'RECEIVERFRED@QMAIL.EDU'],
['YODA KENOBI', '10/23/1966', '999 999 9999', '100', 'dark1234', 'GUIGUIGUI@ZMAIL.GOV']] # list with 5 user data
    print_users(user)
    print_user_data_table(user_data)
    system=input('Use system? Y/N: ') # asks to use system
    while system=='Y' or system=='y':
        select=input('A) Add User B.) Access User: ')
        if select=='A' or select=='a':
            key=get_userid().upper()
            while key in user:
                print('User ID already in Use.')
                key=get_userid().upper()
            userdata=Add_user()
            password=get_password()
            userdata.append(password)
            userdata.append(key)
            user[key]=password
            user_data.append(userdata)
        elif select=='B' or select=='b':
            ID=input('Enter User ID: ')
            if ID in user:
                passcode=input('Enter password: ')
                if passcode==user[ID.upper()]: # asks for user name and password to access user data
                    print('Welcome!')
                    print('i. Print the data for the user in user_data \nii. Delete a user \niii. Update contact information \niv. Change password')
                    options=input('Enter Selection: ')
                    if options=='i' or options=='I':
                        print_user_data(ID,user_data)
                    elif options=='ii' or options=='II':
                        delete_one_user(user,user_data,ID)
                    elif options=='iii' or options=='III':
                        update_contact(user_data,ID)
                    elif options=='iv' or options=='IV':
                        change_password(user_data,ID,user)
                    exit_or_no=input(str('Exit Access User? Y/N: '))
                    while exit_or_no=='N' or exit_or_no=='n':
                        access_programs(ID,user_data,user) # loops to access programs again until user chooses to exit
                        exit_or_no=input(str('Exit Access User? Y/N: '))
                else:
                    print('Invalid Password.')
            else:
                print('Invalid User ID.')
        system=input('Use system? Y/N: ')
    print_users(user)
    print_user_data_table(user_data)
    print('Ending Program')
####: gives access to rpograms for access user
def access_programs(ID,user_data,user):
    print('i. Print the data for the user in user_data \nii. Delete a user \niii. Update contact information \niv. Change password')
    options=input('Enter Selection: ')
    if options=='i' or options=='I':
        print_user_data(ID,user_data)
    elif options=='ii' or options=='II':
         delete_one_user(user,user_data,ID)
    elif options=='iii' or options=='III':
        update_contact(user_data,ID)
    elif options=='iv' or options=='IV':
         change_password(user_data,ID,user)
####: Prints user data as table
def print_user_data_table(user_data):
    print('Name / DOB / Contact / Winnings / Password / User ID')
    for x in user_data:
        print(x)

####: Prints users as a table
def print_users(user):
    print('User ID / Password')
    for key in user:
            print("{:<10} {:<10}".format(key, user[key]))
####: Deletes one user
def delete_one_user(user,user_data,ID):
    name=input(str('Enter User ID to be deleted: '))
    for values in user_data:
        if name.upper() in values:
            confirm_delete=input('Delete? Y/N: ')
            if confirm_delete=='Y' or confirm_delete=='y':
                user_data.remove(values)
                del user[name.upper()]
                print_users(user)
                print_user_data_table(user_data)
            elif confirm_delete=='N' or confirm_delete=='n':
                print('Ending program')
                return ''
####: updates contact info
def update_contact(user_data,ID):
     name=input(str('Enter name to change contact information: '))
     for values in user_data:
         if name.upper() in values:
             entry=input(str('Enter new contact information: '))
             new_contact=userid(entry)
             values[2]=new_contact
             print(values)

####: Changes password
def change_password(user_data,ID,user):
    for values in user_data:
        if ID.upper() in values:
            new_password=input(str('Enter new password: '))
            values[4]=new_password
            user[ID.upper()]=new_password
            return
                
####: adds user
def Add_user():
    name=input(str('Enter name: '))
    dob=get_DOB()
    contact_info=input(str('Enter an email or phone number different from User ID: '))
    winnings=input('Enter winnnings: ')
    temp_list=[]
    temp_list.append(name.upper())
    temp_list.append(dob)
    temp_list.append(contact_info)
    temp_list.append(winnings)
    return temp_list

####: prints user data
def print_user_data(ID,user_data):
    user=ID.upper()
    for values in user_data:
        if user in values:
            print(values)
        
        

####: prints an information to the user describing what is a valid password
def print_passwordinfo():
    print(f'A valid password is between {PASSWD_LENGHT} characters \nConsists of letters, digits or any {SPECIAL}')
    print(f'It does not start with a digit or {SPECIAL} \nHas at least one uppercase letter and at least one digit')

####: returns True if strg is a valid password and False otherwise
def ispassword(strg):
    special_chars=tuple(SPECIAL)
    if len(strg) not in list(range(12,25+1)) or strg.startswith('0') or strg.startswith(special_chars):
        return False
    else:
        for x in strg:
            if howmanyupper(strg)>=1 and howmanydigit(strg)>=1:
                return True
            else:
                return False
    
def howmanyupper(strg):   ####: counts how many uppercase letters. I used this to help with ispassword()
    count=0
    for x in strg:
        if x.isupper():
            count+=1
    return count

def howmanydigit(strg):   ####: counts how many digits. I used this to help with ispassword()
    count=0
    for x in strg:
        if x.isdigit():
            count+=1
    return count

        
####: Reads password from keyboard and asks for a valid password
def get_password():
    print_passwordinfo()
    password=input(str('Enter a password: '))
    validation=ispassword(password)
    while validation is False:
        password=input('Invalid Password. Enter again: ')
        validation=ispassword(password)
    else:
        return password

####: Checks if strg is a valid date in the format MM/DD/YYYY
def isdate(strg):
    months_with_31_days=['01','03','05','07','08','10','12']
    months_with_30_days=['04','06','09','11']
    feb='02'
    month=strg[0:2]
    days=strg[3:5]
    year=strg[6:9+1]
    if int(year) not in range(1900,2020+1):
        return False
    if len(strg)<10 or len(strg)>10:
        return False
    if month in months_with_31_days:
        if is31days(days)==True:
            return True
        else:
            return False
    elif month in months_with_30_days:
        if is30days(days)==True:
            return True
        else:
            return False
    elif month==feb:
        if isleapyear(year)==True:
            if is29days(days)==True:
                return True
            else:
                return False
        elif isleapyear(year)==False:
            if is28days(days)==True:
                return True
            else:
                return False
    
def is31days(days): #### Checks if the amount of days is correct
    dates=['{:02d}'.format(x) for x in range(1,31+1)]
    if days in dates:
        return True
    else:
        return False
def is30days(days): #### Checks if the amount of days is correct
    dates=['{:02d}'.format(x) for x in range(1,30+1)]
    if days in dates:
        return True
    else:
        return False
def is29days(days): #### Checks if the amount of days is correct
    dates=['{:02d}'.format(x) for x in range(1,29+1)]
    if days in dates:
        return True
    else:
        return False
def is28days(days): #### Checks if the amount of days is correct
    dates=['{:02d}'.format(x) for x in range(1,28+1)]
    if days in dates:
        return True
    else:
        return False
def isleapyear(year): #####: Checks if a leap year
    if (int(year) % 4) == 0:  
       if (int(year) % 100) == 0:  
           if (int(year) % 400) == 0:  
               return True 
           else:  
               return False
       else:  
           return True
    else:  
       return False
####: Reads birth date from keyboard
def get_DOB():
    print('Enter DOB in MM/DD/YYYY format.')
    date=input(str('Enter your date of birth: '))
    validation=isdate(date)
    while validation is False:
        date=input(str('Invalid Date. Enter again: '))
        validation=isdate(date)
    else:
        return date

####: Checks if strg is email address
def email(strg):
    domains=['.edu','.com','.gov','.org']
    domain_start=strg.find('.')
    domain_stop=len(strg)
    att_count=strg.count('@')
    domain=strg[domain_start:domain_stop]
    end=strg.find('@')
    letters=strg[:end]
    if len(strg)<7 or strg.startswith('@') or strg.startswith('_') or att_count!=1 or domain not in domains or letters.isalnum()==False:
        return ''
    else:
        return strg.upper()
    
####: checks if strg is a phone number
def phone(strg):
    if len(strg)<10:
        return ''
    phone_number=''
    phone_list=list(strg)
    while ' ' in phone_list:
        phone_list.remove(' ')
    if '-' in phone_list:
        phone_list.remove('-')
    if '(' in phone_list:
        phone_list.remove('(')
    if ')' in phone_list:
        phone_list.remove(')')
    for x in phone_list:
        phone_number+=x
    if phone_number.isdigit()==False:
        return ''
    else:
        return phone_number
####: prints the information stating what is a valid user id.
def print_useridinfo():
    print('A valid user id is an email address or phone number.')
    print('An email consist of letters, digits and underscores. \nIt must be at least 7 characters long.')
    print('It must contain @ and _ but not start with them and ends in .edu, .com, .gov or .org')
    print('A phone number is looks like (D represents a number) \n(DDD)DDD-DDDD \nDDDDDD-DDDD \n(DDD)DDDDDDD \nDDDDDDDDDD.')

####: check if string is a valid user id.
def userid(strg):
    if strg.count('@')>=1:
        return email(strg)
    else:
        return phone(strg)

####: gets user id from keyboard
def get_userid():
    print_useridinfo()
    entry=input(str('Enter a valid User ID: '))
    validation=userid(entry)
    while validation=='':
        entry=input(str('Invalid ID. Enter a valid User ID: '))
        validation=userid(entry)
    return validation
    
main()