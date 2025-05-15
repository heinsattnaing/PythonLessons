# Closure is a function having access to the scope of its parent function, after the function has return.
def parent_function(person, coins): # we can do this like this in the para and the same rule apply
    #coins = 3 we can do this like this or above

#The parent function return the play_game function and then the play_game funcion have access to the scope of that parent function every time we call play_game and they have different value
    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        else: 
            print("\n" + person + " is out of coins.")

    return play_game # We are not calling the function becaue we dont include (), we just returning the nested function

tommy = parent_function("Tommy", 3)
jenny = parent_function("Jenny", 5)

tommy()
tommy()
tommy()

jenny()