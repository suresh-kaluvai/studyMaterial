################### Python ##################

#### Function delcaration

def functionName():
""" doc string"""

"""
    if the function ever executes a return statement, it will return that value, otherwise it will return None,
    the Python null  value.
"""

"""
    In Python, variables are never explicitly typed. Python figures out what type a variable is and keeps track of it
    internally.
"""

"""
    print buildConnectionString.__doc__, __doc__ will return the doc strings of the python function. It will return only
    one doc string i.e immediate to the def delcaration
"""


##### Native Data Types

################ Dictionaries

"""
    Dictionaries are like objects in PHP, JS other languages, which will store the values in key value format.
    keys are case senstive
    A key can store any data type, i.e string, int, other dictionary
"""

d = {"keyA": "ValueA", "keyB": "ValueB", "keyC": "ValueC"}

del d['keyA']           # To delete a key from a dictonary
del d                   # To delete a dictionary
d.clear()               # To clear the all indexes

d["keyA"]               # To Access the keyA value
d["keyA"] = "ValueX"    # To modify/ create new index

################ Lists

"""
    Lists are like Numeric Arrays in PHP kind of languages
"""

li = ["a", "b", "mpilgrim", "z", "example"]

li                      # Result ['a', 'b', 'mpilgrim', 'z', 'example']
li[0]                   # Result 'a'
li[4]                   # Result 'example'
li[-1]                  # Result 'example', its works like this li[len(li) - n]

#### Slicing of the lists
li[0:3]                 # Result ['a', 'b', 'mpilgrim']
li[1:-2]                # Result ['b', 'mpilgrim']
li[fromIndex:uptoIndex] # Result will create new list with the values from fromInex to uptoIndex(not incluede
                        # uptoIndexVal)

li.append("AppededText1")   # append is an in-built fn, which appends the value to the end of list(Only one param)
li                      # Result ['a', 'b', 'mpilgrim', 'z', 'example', 'AppededText1']

li.insert(2, 'insertedtext')    # Insert in an in-built fn, which add values to a specifc index
                                # Insert will take 2 arguments, and the first argument should be int
                                # Insert 

li                      # Result ['a', 'b', 'insertedtext', 'mpilgrim', 'z', 'example', 'AppededText1']
anotherLi = ['av1', 'av2']      # Another list
li.extend(anotherLi)    # Adding two lists

li.remove('a')          # Remove the a from the list, if multiple are there, first occurence will be removed
li.pop()                # Remove the last element in the list

li.index('a')           # Search the list and return the index

### List Operators
li = ['a', 'b', 'mpilgrim']
li = li + ['example', 'new']            # ['a', 'b', 'mpilgrim', 'example', 'new']
li += ['two']                           # ['a', 'b', 'mpilgrim', 'example', 'new', 'two']
li = [1, 2] * 3                         # [1, 2, 1, 2, 1, 2]

################# Tuples

"""
    A tuple is an immutable list. A tuple can not be changed in any way once it is created.
"""
"""
    You can't add elements to a tuple. Tuples have no append or extend method.
    You can't remove elements from a tuple. Tuples have no remove or pop method.
    You can't find elements in a tuple. Tuples have no index method.
    You can, however, use in to see if an element exists in the tuple.
"""
"""
So what are tuples good for?
    •   Tuples are faster than lists. If you're defining a constant set of values and all you're ever going to do with
        it is iterate through it, use a tuple instead of a list.
    •   It makes your code safer if you "write−protect" data that does not need to be changed. Using a tuple instead of
        a list is like having an implied assert statement that shows this data is constant, and that special thought
        (and a specific function) is required to override that.
    •   Remember that I said that dictionary keys can be integers, strings, and "a few other types"? Tuples are one of
        those types. Tuples can be used as keys in a dictionary, but lists can't be used this way.Actually, it's more
        complicated than that. Dictionary keys must be immutable. Tuples themselves are immutable, but if you have
        a tuple of lists, that counts as mutable and isn't safe to use as a dictionary key. Only tuples of strings,
        numbers, or other dictionary−safe tuples can be used as dictionary keys.
    •   Tuples are used in string formatting, as you'll see shortly.
        Tuples can be converted into lists, and vice−versa. The built−in tuple function takes a list and returns a
        tuple with the same elements, and the list function takes a tuple and returns a list. In effect, tuple freezes
        a list, and list thaws a tuple.
"""


### Formatting

uid = "sa"
pwd = "secret"
print pwd + " is not a good password for " + uid    # secret is not a good password for sa
print "%s is not a good password for %s" % (pwd, uid) #secret is not a good password for sa with format inbuilt fn
userCount = 6
print "Users connected: %d" % (userCount, )     # Users connected: 6

#### fomrat method needs to use when formatting multiple data types


################################
"""
    Python functions allow to use default value parameters
    You can specify these values by name
"""

def info(object, spacing=10, collapse=1):

# you can use default values like this
info(odbchelper)
info(odbchelper, 12)
info(odbchelper, collapse=0)
info(spacing=15, object=odbchelper)

### type function

"""
    type takes anything −− and I mean anything −− and returns its datatype. Integers, strings, lists,
    dictionaries, tuples, functions, classes, modules, even types are acceptable.
"""

### string function

"""
    The str coerces data into a string. Every datatype can be coerced into a string.
"""

### dir function
"""
    dir returns a list of the attributes and methods of any
    object: modules, functions, strings, lists, dictionaries... pretty much anything
"""

d = {}
dir(d)          ### ['clear', 'copy', 'get', 'has_key', 'items', 'keys', 'setdefault', 'update', 'values']

### callable function
""" the callable function takes any object and returns True if the object can be called, or False otherwise."""

### getattr
"""
    getattr is an incredibly useful built−in function that returns any attribute of any object
    getattr isn't just for built−in datatypes. It also works on modules.
"""

### hasattr()
""" hasattr is a complementary function that checks whether an object has a particular attribute """

#### and, or

a = "first"
b = "second"

### Ternary operator in python using and, or
1 and a or b        # Results 'first'
0 and a or b        # Results 'second'

### lambda functions

""" lambda functions allows you to define one−line mini−functions on the fly """

### from module import syntax
from module import *    # to import all attributes and methods

### Python uses try...except to handle exceptions and raise to generate them.
"""
    • Accessing a non−existent dictionary key will raise a KeyError exception.
    • Searching a list for a non−existent value will raise a ValueError exception.
    • Calling a non−existent method will raise an AttributeError exception.
    • Referencing a non−existent variable will raise a NameError exception.
    • Mixing datatypes without coercion will raise a TypeError exception.
"""

### for loop

li = ['a', 'b', 'e']
for s in li:
    print s

### glob module
"""
The glob module, on the other hand, takes a wildcard and returns the full path of all files and
directories matching the wildcard."""


### Regular expressions

s = '100 BROAD'
re.sub('ROAD$', 'RD.', s)               # '100 BRD.'
re.sub('\\bROAD$', 'RD.', s)            # '100 BROAD'
re.sub(r'\bROAD$', 'RD.', s)            # '100 BROAD'

s = '100 BROAD ROAD APT. 3'
re.sub(r'\bROAD$', 'RD.', s)            # '100 BROAD ROAD APT. 3'
re.sub(r'\bROAD\b', 'RD.', s)           # '100 BROAD RD. APT 3'

"""
    \b means "a word boundary must occur right here.
    Also use raw string in regular expression in order escape the strings from python
"""

### Regex for validating phone number US
phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
phonePattern.search('work 1−(800) 555.1212 #1234').groups()


#######
"""
    • ^ matches the beginning of a string.
    • $ matches the end of a string.
    • \b matches a word boundary.
    • \d matches any numeric digit.
    • \D matches any non−numeric character.
    • x? matches an optional x character (in other words, it matches an x zero or one times).
    • x* matches x zero or more times.
    • x+ matches x one or more times.
    • x{n,m} matches an x character at least n times, but not more than m times.
    • (a|b|c) matches either a or b or c.
    • (x) in general is a remembered group. You can get the value of what matched by using the groups() 
        method of the object returned by re.search.

"""
