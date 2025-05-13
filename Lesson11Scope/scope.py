#There are different kinds of scope, the first we learn is global scope
name = "Dave" # This is like the global scope because it is avaliable to everything in this file

def another(): # Nested functions
    def greeting(name):
        color = "blue"
        print(color)
        print(name)

    greeting("Dave")

another()
