#String data type

#literal assignment
first = "Dave"
last = "Mustaine"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

#constructor function
pizza = str("Pepperroni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str)) 

#concentation 
fullname = first + " " + last
print(fullname)

fullname += "!" #we can also use this to concat the string
print(fullname)

#Casting a number to a string
decade = str(1980)
print(decade)
print(type(decade))

statement = "I like rock mucic from " + decade +"s."
print(statement)

#Multiple lines
multiline = '''
Hey, how are you?                       

I was just checkin in

                     All good?

'''
print(multiline)

#Escaping special characters
sentence = 'I\'m back at work!\t Hey!\n\nWhere\'s this at\\located?'
print(sentence) 

#String Methods( Methods are functions )
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title()) #This method will turn everything to a proper case. Capitalizing every first word in that sentence.
print(multiline.replace("good", "ok")) #This method change "good" with "ok". If you want to chagne the letter put it in the first one
print(multiline)

print(len(multiline)) #Show the length of the multiline 
multiline += "                               "
multiline = "                     " + multiline
print(len(multiline))

print(len(multiline.strip())) #Remove the white spaces and we put len so we also checked the length of the lines
print(len(multiline.lstrip())) #Only remove the white space from the left side
print(len(multiline.rstrip())) #Only remove the white space from the right side

#Build a menu
title = "menu".upper() #Can also use directly like this
print(title.center(20, "=")) #The output is like this ========MENU========
print("Coffee".ljust(16, ".") + "$1".rjust(4)) #Left justify and right justiry the output is Coffee..........  $1
print("Muffin".ljust(16, ".") + "$2".rjust(4)) 
print("Cheesecake".ljust(16, ".") + "$5".rjust(4)) 

print("")

#String index values
print(first[1])
print(first[-1]) #Show the last character of the Index for this case its "e"
print(first[1:-1]) #Wants to start at the index and ends at index -1 bacically its between 1 and -1 the out put is av in dave
print(first[1:]) #if we don't provide the end value it will just igonre and use all the output is ave in dave

print("")

#Some methods return Boolean values
print(first.startswith("D"))
print(first.endswith("Z"))

#Boolean data types
myvalue = True #True needs to be capital T also False needs to be capital F too
x = bool(False) #bool = constructor function
print(type(x))
print(isinstance(myvalue, bool))

print("")

#Numeric data types

#Integer types
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

#float types
