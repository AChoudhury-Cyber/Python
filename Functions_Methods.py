#the len variable, tells you how many characters the varibale has 
variable= "Python programme"
print (len(variable))
#the square brackets and the number determines the element in the variable. Here 0 is the 1st element so it's
#p
print(variable [0])
#You can use a negative index to print the last characters in the variable
print(variable [-1])
#slice the variable. So this will return the first three elements in the variable 'pyt'
print(variable [0:3])
#slice the variable. So this will return the entire elements in the variable
print(variable [0: ])
#slice the variable. So this will return the first three elements in the variable 'pyt'
#python puts by default the first 0 index
print(variable [:3])
#slice the variable. So this will return the entire elements in the variable
print(variable [:])

#Methods

#adds an element to to a list
list.append
#Adds all elements of a list to the another list
list.extend 
#insets an item at the defined index
list.insert
#Removes an item from the list
list.remove
#Removes and returns an element at the given index
list.pop
#Returns the index of the first matched item
list.index
#Returns the count of number of items passed as an argument
list.count
#sorts items in a list in asceding order
list.sort
#reverses the order of items in the list
list.reverse