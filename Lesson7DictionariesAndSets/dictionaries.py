# Dictionaries (Looks alot more like objects in other language)
# Dictionaries are used to store data values that are in key value pairs 
# *** Dictionaries use {}

# Can use any data types not only stirng
band = {
    "vocals" : "Dave Mustaine",
    "guitar" : "Marty Friedman"
}

# This is making a dictionaries but using constructor
band2 = dict(vocals = "Dave Mustaine", guitar = "Marty Friedman")

print(band)
print(band2)
print(type(band))
print(type(band2))

# Access items in the Dictionaries
print(band["vocals"])
print(band.get("guitar"))

#lists all keys
print(band.keys())

#lists all values
print(band.values())

#list of key/value pair as tuples
print(band.items())

#verify a key exists 
print("guitar" in band)
print("Triangle" in band)

#Change values
band['vocals'] = "Paul Stanley" #Change values
band.update({"bass" : "Gene Simmons"}) # This add the new item in dict
print(band)

#Remove items
print(band.pop("bass")) #pop retrun the value of the item not tuple so in this case output is Gene Simmons
print(band)

band['drum'] = "Peter Criss" # This add new item to the Dict
print(band)

print(band.popitem()) # This remove the last thing added but it will show that on "Tuple"
print(band)

# Delete and clear 
band["drum"] = "Peter Criss"
del band["drum"]
print(band)

band2.clear()
print(band2)

del band2 #This delete the whole dict

#Copy dictionaries

# If you do it like this when you add or remove the items in the band2 it will also remove the same things in the band
#*band2 = band* #This create a reference not a copy(means they both referring to the same place in the memory for the same dictionaries)
#We don't want to do this like above(bad copy)

# This is how you actually copy
band2 = band.copy()
band2["drum"] = "Peter Criss"
print(band)
print(band2)

# Or use the dict() constructor function
band3 = dict(band) # This also make a copy not a reference
print("Good copy!")
print(band3)

#Nested dictionaries
#means value of a key value for a key value pair can be in another dictionaries

member1 = {
    "name" : "Plant",
    "instrument" : "vocals"
}

member2 = {
    "name" : "Page",
    "instrument" : "guitar"
}

band = {
    "member1" : member1, #member1 left is the key and right is the value
    "member2" : member2
}
print(band)
print(band["member1"]["name"]) #This show the name of the member1

# Sets (The fourth and final data collection type)

#create a set ( uses {})
nums = { 1, 2, 3, 4 }

#create a set using constructor
nums2 = set(( 1, 2, 3, 4 ))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# ** No duplicates are allowed in Sets
nums = { 1, 2, 2, 3 } #Didn't create a error but it ignore the duplicate so it will only show one 2 in the output
print(nums)

# True value is a dupe of 1 and False is a dupe of 0
nums = { 1, True, 2, False, 3, 4, 0 }
print(nums)

# check is a value is in the set
print(2 in nums)

# but you cannot refer to an element in the set with an index  positon of a key

# Adding a new element to a set
nums.add(8)
print(nums)