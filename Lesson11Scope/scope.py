#There are different kinds of scope, the first we learn is global scope
name = "Dave" # This is like the global scope because it is avaliable to everything in this file
count = 1

def another(): # Nested functions
    color = "blue"
    #count += 1 # This is modifying the golbal count which cannot do, we can do count = 2(This is making a new variable, which can do)
    #If we want to use the global count we can do like this
    # global count += 1 we cant do like this directly tho
    global count
    count += 1
    print(count)
    
    def greeting(name):
        # In nested functions if we want to use the variable from parent fun, we have to use this keyword
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Dave")

another()
