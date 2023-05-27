name= input("Please enter your full name ")

if not name:
    print ("You haven't entered anything. Please enter your full name")
elif len(name) < 5:
    print("You have entered less than 4 characters. Please make sure you have entered your first name and surname.")
elif len (name)> 25:
    print ("You have entered more than 25 characters. Please make sure you have only entered your full name")
else: 
    print("Thank you for entering your full name.")

