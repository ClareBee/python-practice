type(2)
# integer
type(2.2)
# float

one, two, three = 1, 'two', 3.0
print(one)

import keyword
keyword.kwlist

def myFunction:
    # do something

print(2 + 5.0)
# 7.0

# exponent
print(2**5)

print(10/2)
# python3 will return float automatically eg print(20/3) whereas previous versions round down to nearest integer

# order of operations: (),  **, *, /, %, +, -

# binary number manipulation
print(1 << 3)

# basic string manipulation
string1 = "hello"
len(string1)
string1[0]
string1[-1]

print("Today I had {0} cups of {1}".format(3, 'coffee'))
print('prices: ({x}, {y}, {z})'.format(x = 2.0, y = 1.5, z = 9.2))
print('The {vehicle} had {0} crashes in {2} months'.format(1, 5, vehicle = 'car'))

# right alignment
print('{:>20}'.format('text'))
# binary format
print('{:b}'.format(21))

# conditional statements
not
and
or

# elif
if answer == "yes":
    print("ok")
elif answer == "maybe":
    print("me too")
else:
    print("no")

# ternary operator
answer = "yes"
myAnswer = "ok" if answer == "yes" or answer == "maybe" else "no"
print(myAnswer)

# ranges
range(start, stop, step)

for i in range(1, 10):
    print(i)
