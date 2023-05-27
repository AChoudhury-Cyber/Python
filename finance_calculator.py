import math
#This is to ask the user to input the choice of either investment or bond. 
print("Investment - to calculate the amount of interest you'll earn on your investment\nBond - to calculate the amount you'll have to pay on a home loan")
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower ()
#this 'if' function is if the user inputs investment and 
# then the code will ask the user information regarding 
# how much they are investing, interest rate, number of years 
# and this is concactinated either in integer or float depending on the data type. 
if choice == 'investment':
    #float is being used so that the computer can concatinate the output based on decimals
    #.lower is used at the end as a function incase the user inputs any words in capital letters
    amount = float(input("Enter the amount of money that you are depositing: "))
    rate = float(input("Enter the interest rate (as a percentage): "))
    years = int(input("Enter the number of years you plan on investing: "))
    interest = input("Enter 'simple' or 'compound' interest: ").lower()
#A= amount. The chosen variable name
#if, elif and else used in case the user inputs different inputs. 
    if interest == 'simple':
        A = amount * (1 + (rate/100) * years)
    elif interest == 'compound':
        A = amount * math.pow((1 + rate/100), years)
    else:
        print("Invalid choice of interest type.")
       #exit used incase there is an infinite loop. This is optional 
        exit()
        #{:.2f is two decimal point, I found this code online}
    print("Total amount after {} years with {}% {} interest: {:.2f}".format(years, rate, interest, A))
        #this is the second choice given of bond. Again, float or integer added to concatinate the output
elif choice == 'bond':
    house_value = float(input("Enter the present value of the house: "))
    rate = float(input("Enter the interest rate: "))
    months = int(input("Enter the number of months you plan to take to repay the bond: "))
    #interest rate of /100/12
    i = (rate/100) / 12
    repayment = (i * house_value) / (1 - (1 + i)**(-months))
    #I am printing my variable to 2 decimal point and then formating the printed output
    print("Monthly bond repayment: {:.2f}".format(repayment))
    #else print 'Invalid choice of calculation"
else:
    print("Invalid choice of calculation.")
    #optional adding the exit incase the code runs forever
    exit()
