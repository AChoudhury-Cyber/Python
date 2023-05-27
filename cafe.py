#Menu
#Tropical Mango Bubble Frappé
#Blueberry Bubble Frappé & Light Whip
#Popcorn Frappé & Light Whip
#Chocolate Fudge Brownie Frappé

#dictionary 1= stock
#stock value for item1
#stock value for item2
#stock value for item3
#stock value for item4

# my_tuple= (8, 'banana')
# key, value = my_tuple
# print (key) #prints 9
# print (value) #prints banana

# Create a dictionary for the menu with item numbers and names
#In the code below, the curly braces {} are used to define the dictionary literal for the menu dictionary. 
#Each key-value pair is separated by a colon :. The keys (item numbers) are integers,
#and the values are strings (item names). The resulting dictionary is assigned to the variable menu
LittleNova_Boba_Menu = {
    1: 'Tropical Mango Bubble Frappe',
    2: 'Blueberry Bubble Frappe & Light Whip',
    3: 'Popcorn Frappe & Light Whip',
    4: 'Chocolate Fudge Brownie Frappe'
}

# Create a dictionary for the stock with item names and stock values
LittleNova_Boba_stock = {
    'Tropical Mango Bubble Frappe': 40,
    'Blueberry Bubble Frappe & Light Whip': 40,
    'Popcorn Frappe & Light Whip': 10,
    'Chocolate Fudge Brownie Frappe': 5
}
# Create a dictionary for the price with item names and their respective prices
LittleNova_Boba_price = {
    'Tropical Mango Bubble Frappe': 4.99,
    'Blueberry Bubble Frappe & Light Whip': 4.99,
    'Popcorn Frappe & Light Whip': 4.99,
    'Chocolate Fudge Brownie Frappe': 4.99
}

# By setting total_stock_worth to 0 initially, we start with an empty total. 
# As we iterate through the stock dictionary and calculate the worth of each item, 
# we will add the calculated worth to this variable, effectively accumulating the total 
# worth of all the items in stock.
total_stock_worth = 0

#The 'for' loop is a way to iterate or go through each
# item in a collection (such as a list, dictionary, or string) and perform a set of instructions for each item.
for item, stock_value in LittleNova_Boba_stock.items():
    item_price = LittleNova_Boba_price[item]
    #multiplying the stock value of the item by its price. 
    # This multiplication calculates the value or worth of the item in terms of its quantity and price.
    item_value = stock_value * item_price
    total_stock_worth += item_value

# Display the total stock worth
print("Total Stock Worth: $", total_stock_worth)


#dictionary2=prices
#price value for item1
#price value for item2
#price value for item3
#price value for item4

#total stock value of all items
#loop through all the lists and dictionaries

#when I loop through the menu list, the items can be set as keys to access the corresponding 'stock'
#and 'price' values. Each 'item_value', is calculated by multplying stock value by the price value. 
#for example: 
#item_value= (stock[items] *price [items])

#print out the result of the calculations


