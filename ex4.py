cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
#cars without drivers
cars_not_driven = cars - drivers
#cars driven have drivers 
cars_driven = drivers
#the total number of seats on driven cars
carpool_capacity = cars_driven * space_in_a_car
#total passangers divided by cars driven
average_passengers_per_car = passengers // cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
