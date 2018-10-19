'''# Local Scopes Cannot use variable in other local scopes
def spam():
    eggs=99
    bacon()
    print(eggs)

def bacon():
    ham=101
    eggs=0
    print(eggs)

spam()

#Gloabal variable can be read from a local scope
def spam():
    print(eggs)
eggs =42
spam()
print(eggs)

# Local and Global variable with the same Name
def spam():
    eggs= 'spam local'
    print(eggs)
def bacon():
    eggs= 'bacon local'
    print(eggs)
    spam()
    print(eggs)

eggs= 'global'
bacon()
print(eggs)
'''
# the global statement
def spam():
    global eggs
    eggs ='spam'
eggs ='global'
spam()
print(eggs)




