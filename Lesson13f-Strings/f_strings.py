person = "Dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left." % (person, coins) # %s is where we want to put person and coins
print(message)

message = "\n{} has {} coins left.".format(person, coins) # This is a format method
print(message)

message = "\n{1} has {0} coins left.".format(coins, person) # we can do index to flip things
print(message)

player = { 'person' : "Dave", 'coins' : 3 } # This is using dictnaries
message = "\n{person} has {coins} coins left.".format(**player)
print(message)

# This is the F Strings

message = f"\n{person} has {coins} coins left." #This person and coins are not from dict this is from all the way up top
print(message)

message = f"\n{person} has {2*5} coins left." # We can use like this too
print(message)

message = f"\n{person.lower()} has {2*5} coins left." # We can use methods too
print(message)

message = f"\n{player['person']} has {2*5} coins left." # We can use dict too
print(message)

# You can pass formatting options

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}") #.2 is 2 decimal and f is fixed(22.50)

for num in range(1, 11):
    print(f"\n2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"\n{num} divided by 4.52 is {num / 4.52:.2%}") # This gives %