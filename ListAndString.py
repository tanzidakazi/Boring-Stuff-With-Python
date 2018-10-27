# index() List Method
# append() List Method
# insert() List Method
# remove() List Method
# sort() List Method
'''import copy
friendList=['Mahmuda', 'Mazdia', 'Samiha', 'Sherin', 'Shegufta', 'abc', 'qwe']

print('Index of Mahmuda is ')
print(friendList.index('Mahmuda'))

for i in range(len(friendList)):
    print('Index: ' + str(i+1) + ', Name: ' + friendList[i])

for i in range(len(friendList)):
    print(friendList.index('Mazdia'))
    print(friendList.index(friendList[i])) # same as str(i)

print('Enter name of new friend: ')
newFriend = input()
friendList.append(newFriend)
print(friendList)

friendList.insert(2, 'Areeba')
print(friendList)

friendList.remove('abc')
print(friendList)

friendList.sort()
print(friendList)
friendList.sort(reverse=True)
print(friendList)
friendList.sort(key=str.lower)
print(friendList)

# copy() Function
# deepcopy() Funtion
familyList = copy.copy(friendList)
#familyList[1]='Nephew'
familyList[1]= ['Mum', 'Dad', 'Brother']
print(familyList)
'''

# upper(), lower() String Method
# isupper(), islower() String Method
# isX String Method
# startswith(), endswith() String Method
# join(), split() String Method
# rjust(), ljust(), center() Justifying Text
# strip(), rstrip(), lstrip() Removing Whitespace
# Copying and Pasting with paperclip module

string1= 'Mahmuda went to London \n'
print(string1)

print('Press 1 for upper()')
print('Press 2 for lower()')
print('Press 3 for isupper()')
print('Press 4 for islower()')
print('Press 5 for isalpha()')
print('Press 6 for isalpha()')
print('Press 7 for isalnum()')
print('Press 8 for isdecimal()')
print('Press 9 for isspace()')
print('Press 10 for istitle()')

def manipulateString(x):
    for i in range(10):
        x=input()
        if x=='1':
            print(string1.upper())
        elif x=='2':
            print(string1.lower())
        elif x=='3':
            print(string1.isupper())
        elif x=='4':
            print(string1.islower())
        
manipulateString(string1)




















    
