# keys() values() items() Method
spam ={'color': 'black',
       'age': '24'}
for v in spam.values():
    print('Values inside keys: ' + v)

for k in spam.keys():
    print('Keys or Indexes: ' + k)

print('Items = Keys + Values')

for i in spam.items():
    print(i)

print(spam.keys())
print(list(spam.keys()))

for k, v in spam.items():
    print('Key: '+ k + ' Value: ' + str(v))

# get() Method
picnicItems ={'apples': 5,
              'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs')

# setdefault() Method
spam = {'name': 'Tanzida',
        'age': 24}
spam.setdefault('color', 'black')
print(spam)
print("No change in color")
spam.setdefault('color', 'white')
print(spam)

#characterCount. A short program that counts the number of occurrences of each letter in a string. Pretty Printing
import pprint
message= 'It was a bright cold day in April, and the clocks were striking thirteen.'
countCharacter ={}

for character in message:
    countCharacter.setdefault(character, 0)
    countCharacter[character]= countCharacter[character]+ 1
print(countCharacter)
pprint.pprint(countCharacter)
#pprint(pprint.pformat(countCharacter))
