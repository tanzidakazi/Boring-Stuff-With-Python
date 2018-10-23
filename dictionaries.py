'''# keys() values() items() Method
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
'''
# setdefault() Method

