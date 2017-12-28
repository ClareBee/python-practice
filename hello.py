# python is a typed language
# needs casting to make types compatible eg str(), int(), float()

print 'Content-type: text/html'
print ''
print 'hello world'

age = 33
print age

pi = 3.14
print pi

name = 'bob'
print name

phrase = 'hi my name is bob'
print phrase[0]
print phrase[0:5]
# print phrase + name concatenation
# python array = 'list'
myList = ['bob', 'bill', 3]
print myList
print myList[1]
print myList[1:3]
# python tuple = a read-only list
myTuple = (1, 2, 3, 4)
print myTuple[2]
#python dictionary = two-dimensional array
dictionary = {}
dictionary['manager'] = "bob"
dictionary['secretary'] = "bill"
print dictionary.keys()
print dictionary.values()

# python for loops
for i in range(11):
    print i
    # prints 0 to 10, critical indentation

favouriteFoods = ['pizza', 'icecream', 'spaghetti']
for food in favouriteFoods:
    print "I like eating " + food + "."

# python while loops
x = 0
while x <= 10:
    print x
    x = x + 1
    # x+=1

# python if statements
if name == "bob" or name == "bill":
    print "hello" + name
else:
    print "I don't know you!"

# python functions
def sayHello():
    print 'hello'

# python3 = print('hello')

sayHello()

def saySomething(something):
    print something

saySomething("hello")

def multiplyTwoNums(x, y):
    return x * y

print multiplyTwoNums(4,6)
