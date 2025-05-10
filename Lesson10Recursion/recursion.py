# A recursion in python when the function calls itself. And it would be a recrisive funciton.
def add_one(num):

    if(num >= 9):
        return num + 1 #After it is greater or equal to 9 it will return this num + 1 here
    
    total = num + 1
    print(total)

    return add_one(total) #This will call itself over and over again until it is greater than or equal to 9

# add_one(0)# This will only printed to 9 because it is added to the 9 at the first return

mynewtotal = add_one(0) #This will added 10 to the output
print(mynewtotal)