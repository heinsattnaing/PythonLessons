users = ['Dave', 'John', 'Sarah'] #valid list

data = ['Dave', 32, True] #valid list

emptylist = [] #can also do empty list

print('Dave' in emptylist) #The output is True meaning we can check Is Dave present in the users list
print(users[0]) #The output is Dave we can check the data output like this
print(users[-1]) #The output is Sarah show the last value of the list

print(users.index('Dave')) #This show the item index

print(users[0:2]) #The output is Dave and Sarah in the list form
print(users[1:0]) #The output is start from John and to the end of the list
print(users[-3:-1]) #The output is the same as the first one this is showing the list handle negative too

print(len(users)) #This is the method for knowing the length for the list output is 3
users.append('Elsa') #This add more vaue to the existing list
print(users)

users += ['Jason'] #Can also add like this to the list
print(users)

users.extend(['Robert', 'Jimmy']) #Can also add like this method
print(users)

users.extend(data) #Can also add the existing list to the list 
print(users)

users.insert(0, 'Bob') #This can add the list anywhere you want called "Insert" method
print(users)

users[2:2] = ['Alex', 'Eddie'] #This can add between index 2 like that
print(users)

users[1:3] = ['Robert', 'JPJ'] #This replace start from 1 and ends at 3 like a replacement thing
print(users)

users.remove(32) #This is the remove method
print(users)

print(users.pop()) #This method remove the last item of the list. Even tho that is removed it gives the value
print(users)

del users[0] #This is the delete method will delete the index in the bracket
print(users)

#del data #This delete the whole list
#print(data) #This will show error because the list is already deleted

data.clear() #This won't delete the list but it will empty out the list.
print(data)
 
users[1:2] = ['dave'] #if we do that and sort the lower case it will show at the last item on the list
users.sort() #This sort the list alphabetical
print(users)

users.sort(key=str.lower) #This will include the lower case letter to alphabetical sorting
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse() #This is the method to reverse the whole list
print(nums)

# nums.sort(reverse=True) #This method will sort the reverse list like in here start form 78 and ends at 1 
# print(nums)

print(sorted(nums, reverse=True)) #This method does not modified the list
print(nums)

#Three ways to make a copy

numscopy = nums.copy() 
mynums = list(nums)
mycopy = nums[:] #This modify the end and starting point, since we don't have to do that we copy the all item and make a copy

print(numscopy)
print(mynums)
print(mycopy)
print(nums)

print(type(nums)) #This check the type of the nums which is list
 
mylist = list([1, 'Neil', False]) #This creating list using constructor
print(mylist)

###Tuples
#Tuples are much like list but the data inside the tuples will not change and the order inside of the list will not change
#Tuple use () and list use []
#Tuple can be copied

mytuple = tuple(('Dave', 42, True)) #Create Tuple using constructor

anothertuple = (1,3,5,6,3,3,3) #This is also tuple not using constructor

print(mytuple)
print(type(mytuple))
print(anothertuple)
print(type(anothertuple))

#This is copy and added tuple

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)
print(type(newtuple))

#unpacking a tuple

(one, two, *hey) = anothertuple # "*" makes the hey hold list of 2 items in here
print(one)
print(two)
print(hey)

print(anothertuple.count(3)) #This count how many three are in the tuples