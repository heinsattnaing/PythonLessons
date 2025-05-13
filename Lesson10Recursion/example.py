# value = True

# while value:
#     print(value)
#     value = False
#     #value = 0 # This do the same because 0 is considered False in python, 1 is True

# What he trying to tell is in value it can be anything. whether it is true or y or anything. In while it is set to be existed nor it is true or string.
value = "y"
count = 0

while value:
    count += 1
    print(count)
    if(count == 5):
        break
    else:
        value = False
        continue #This continue keyword check the while loop part still