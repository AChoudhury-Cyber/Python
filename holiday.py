#an argument is a value that is passed to a function or method when it is called or invoked. 
#It is used to provide input or information to the function, which the function can then process 
#and use to perform its tasks.

#define a function called hotel_cost that takes one parameter: num_nights
def hotel_cost(num_nights):
    nightly_rate = 50  # Cost per night for the hotel
    total_cost = num_nights * nightly_rate
#This line returns the calculated total_cost as the output of the function.
    return total_cost

#define a function called hotel_cost that takes one parameter: city_flights
def plane_cost(city_flight):
    #if,elif else statement for options on where to go
    if city_flight == "New York":
        return 500
    elif city_flight == "Venice":
        return 800
    elif city_flight == "Dubai":
        return 1200
    elif city_flight == "Istanbul":
        return 700
    elif city_flight == "Lisbon":
        return 600
    elif city_flight == "Athens":
        return 750
    else:
        return 0

#define a function called car_rental that takes one parameter: rental_days
def car_rental(rental_days):
    daily_rate = 25  # Cost per day for car rental
    total_cost = rental_days * daily_rate
    return total_cost


def holiday_cost(city_flight, num_nights, rental_days):
    #This line calls the plane_cost function, passing the city_flight as an argument. 
    # It assigns the returned flight cost to the variable total_flight_cost
    total_flight_cost = plane_cost(city_flight)
    total_hotel_cost = hotel_cost(num_nights)
    total_car_rental_cost = car_rental(rental_days)
    total_cost = total_flight_cost + total_hotel_cost + total_car_rental_cost
    return total_cost

# Getting user inputs by first defining a list called city_flights that contains the names of different cities.
city_flights = ["New York", "Venice", "Dubai", "Istanbul", "Lisbon", "Athens"]
print("Available City Flights:")
#This line starts a loop that iterates over the city_flights list. 
# The enumerate() function is used to associate an index with each city in the list. 
# The start=1 parameter specifies that the index should start from 1 instead of the default value of 0.
for index, city in enumerate(city_flights, start=1):
    # The f-string formatting is used to format the output string with the index and city name.
    print(f"{index}. {city}")

choice = int(input("Enter the number corresponding to the City you will be flying to: "))
city_flight = city_flights[choice - 1]

num_nights = int(input("Enter the number of nights you will be staying in the hotel: "))
rental_days = int(input("Enter the number of days you will be hiring a car for: "))

# Calculate and print the holiday cost
total_cost = holiday_cost(city_flight, num_nights, rental_days)
print("\nHoliday Details:")
print("------------------------------")
print(f"City Flight: {city_flight}")
print(f"Hotel Cost: ${hotel_cost(num_nights)}")
print(f"Plane Cost: ${plane_cost(city_flight)}")
print(f"Car Rental Cost: ${car_rental(rental_days)}")
print(f"Total Cost: ${total_cost}")
