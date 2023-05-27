#This is the count variable that keeps track of the number of entries the user has made 
count = 0
#We need a total and count to calculate the average
total = 0
#The while loop determines whether a code is successful until it becomes false. A loop that keeps on repeating 
#until it becomes false
while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        #because the while loop on line 7, true can never be false, so the while loop will run explicitly 
        #forever until we tell it to break. 
        break
    count += 1
    #The total of the numerical entries is being increased by the user entry. 
    total += num
#if the count is greater than 0, then we will encounter the average of total /count. 
if count > 0:
    average = total / count
    print("The average is:", average)
else:
    print("No numbers were entered.")
