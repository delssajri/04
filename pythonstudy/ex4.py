# assign to cars integer value
cars = 100
# assign to space in the car floating point value
space_in_a_car = 4.0
# assign to drivers integer value
drivers = 30
# assign to passangers integer value
passengers = 90
# evalute substraction and assign its result to cars_not_driven
cars_not_driven = cars - drivers
# assign drivers value to cars_driven variable
cars_driven = drivers
# evalute entire capacity and assign it as a floating point value to
# carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# evalute passengers to cars_driven ratio and assign it to
# average_passengers_per_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
