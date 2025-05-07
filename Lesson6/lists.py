users = ['Dave', 'John', 'Sarah'] #valid list

data = ['Dave', 32, True] #valid list

emptylist = [] #can also do empty list

print('Dave' in emptylist) #The output is True meaning we can check Is Dave present in the users list
print(users[0]) #The output is Dave we can check the data output like this
print(users[-1]) #The output is Sarah show the last value of the list

print(users.index('Dave')) #This

print(users[0:2]) #The output is Dave and Sarah in the list form
print(users[1:0]) #The output is start from John and to the end of the list
print(users[-3:-1]) #The output is the same as the first one this is showing the list handle negative too

print(len(users)) #This is the method for knowing the length for the list output is 3
users.append('Elsa') #This add more vaue to the existing list
print(users)
