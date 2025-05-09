# value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break # This will stop the loop when the value is equal to 5 
#     value += 1

# What this continue do is it skip the whole loop when it see so its skip the whole loop so we need to keep the increment before going to the next loop so we added the increment above the continue if not it will be in the infinite loop so becareful
# This added the 1 so it started at 2, and it didn't include no 5 because it skip the continue statement 
# value = 1
# while value <= 10:
#     value += 1
#     if value == 5:
#         continue 
#     print(value)
# else:
#     print("Now the value is equal to " + str(value))

names = [ "Dave", "Mustaine", "John" ]
# for x in names: # We can use anything in "x", is to represent each value in the list as it iterates through the loop
#     print(x)
# for x in "Mississippi": # The output show one letter of the letter Mississippi each time the loop iterates
#     print(x)

# for x in names:
#     if x == "Mustaine":
#         break
#     print(x)

# for x in names: 
#     if x == "Mustaine":
#         continue
#     print(x)

# For loop that iterates through the ranges
# Starts at 0
# for x in range(4):
#     print(x)

# for x in range(2, 4): # This make start at 2 and stop at 4
#     print(x)

#This is how to increment
for x in range(5, 101, 5): #start and end and increment by how much. If we want to include the 100 make sure to higher like 101 or something to include the 100
    print(x)
else:
    print("Glad that\'s over!")

names = ["Dave", "Sarah", "John"]
actions = ["codes", "eats", "sleeps"]

# # Nested loops
# for name in names: # This gives dave codes, dave eats, dave sleeps
#     for action in actions:
#         print(name + " " + action + ".")

# Nested loops
for action in actions: # This gives dave codes, sarah codes, john codes
    for name in names:
        print(name + " " + action + ".")