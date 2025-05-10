# Functions are reusable block of codes and when we call a function it runs the block of code inside the function
# We use "def" because we are defining a function
# Naming convension is to use all lower case letters, if we want one or more words we use _

def hello_world():
    print("Hello World!")

# This is the call of function to make that function to work
hello_world()

def sum(num1, num2):
    print(num1 + num2)

sum(2, 3)
sum(4, 8)
sum(100, 3)

# We can also use return keyword too
def sum(num1, num2):
    return num1 + num2

total = sum(2, 3)
print(total)

def sum(num1 = 0, num2 = 0 ): #We can do this if users forgot to put arguments so we will get the out put 0
    if(type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2# If we do this the line will never executed because we return early

total = sum("a", 2)
print(total)

def multiple_items(*args): # We do * when we dont know how many arguments are added to the parameters(We can use any words we want in "args")
    print(args)
    print(type(args))

multiple_items("Dave", "Sara", "John") #This is output and these are tuples

def mult_named_items(**kwargs): #kwargs = key word arguments
    print(kwargs)
    print(type(kwargs))

# kwargs are used to name the unknow arguments
mult_named_items(first = "Dave", last = "Mustaine") #This output is dictionaries