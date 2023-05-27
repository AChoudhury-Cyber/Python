first = "Atif"
last = "Choudhury"
#concatinated the string by placing the " ", this puts a space in between
full = first + " " + last 
print (full)
#not putting " ", there is no space in between and it prints out AtifChoudhury
full2 = first + last 
print (full2)

#Alternatively, you can write it using f function and curly braces
first = "Atif"
last = "Choudhury"
full3= f"{first} {last}"
#using the f function, we can use len to find the length of the first variable
full3= f"{len(first)}"
full3= f"{len(first)} {2+2}"
full3= f"{len(first)} {len(last)}"
print (full3)