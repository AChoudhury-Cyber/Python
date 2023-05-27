name = input("Please enter your full name: ")

if not name:
    print("You haven't entered anything. Please enter your full name.")
elif len(name.split()) < 2:
    print("You have entered less than 2 words. Please make sure you have entered your first name and surname.")
else:
    print("Thank you for entering your full name.")

