# initilize variables
people = 30
cars = 40
trucks = 15


# compare people with cars, True if cars greater
if cars > people:
    print "We should take the cars."
# compare people with cars, True if people greater
# evaluted if first comaparison failed
elif cars < people:
    print "We should not take the cars."
# equivalent to equal people and cars
else:
    print "We can't decide."

# compare trucks with cars, True if trucks greater
if trucks > cars:
    print "That's too many trucks."
# Otherwise compare cars with trucks once more again, True if cars greater
elif trucks < cars:
    print "Maybe we could take the trucks."
# equivalent to equal trucks and cars
else:
    print "We still can't decide."

# compare people with trucks, True if people greater
if people > trucks:
    print "Alright, let's just take the trucks."
#  otherwise, True if people are less or equal than truck
else:
    print "Fine, let's stay home then."
