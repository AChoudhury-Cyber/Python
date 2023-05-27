#all these variables are strings but output a integer so int added. 
swimming_time = int(input("Enter time taken for swimming (in minutes): "))
cycling_time = int(input("Enter time taken for cycling (in minutes): "))
running_time = int(input("Enter time taken for running (in minutes): "))

#determining total_time
total_time = swimming_time + cycling_time + running_time

if total_time <= 100: #less than 100 minutes
    award = "Provincial Colours" #Provincial colours
elif total_time <= 105:
    award = "Provincial half Colours" #provincial half colours
elif total_time <= 110:
    award = "Provincial Scroll" #provincial scroll
else:
    award = "No award"
print(f"Total time taken:{total_time}") #{} used because I am inputting the variable total_time in the middle of a code
print(f"Award received:{award}")