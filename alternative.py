#the first variable 
helloString1 = "Hello World"
# initialize as empty string
helloString2 = ""

# For loop -This loops over the total length of the variable called (hellostring1).
#len means the length of the variable
#we have i as this is the index as it incrementally increases everytime it goes over the loop
for i in range (len(helloString1)):
    #this if code asks if i (modulo) goes over an element and then halfs it, finding the even number
    #therefore this if statement runs on an even number
    #if I had written if(i% 3==0)
    if(i % 2 == 0):
#now the strings are added together and we use the square brackets to access the index of the (hellostring1 variable)
       #and then we use the upper function
       helloString2 += helloString1[i].upper()
    #or else we use the lower function
    else:
        helloString2 += helloString1[i].lower()

print (helloString2)


# task 2. 

helloString3 = []
#I am using the split method to split the words in the string
splitString = "I am learning to code".split()

#then I am using the for function to find the length of the variable so that I can find the even numbers on the string
for i in range (len(splitString)):
    if(i % 2 == 0):
        #then I am using append to add items to the list and then choosing either upper or lower 
        helloString3.append(splitString[i].upper())
    else:
        helloString3.append(splitString[i].lower())

print('helloString3', " ".join(helloString3))








