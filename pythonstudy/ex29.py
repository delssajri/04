# initialize variables
people = 20
cats = 30
dogs = 15


# compare people with cats counts, True if cats greater
if people < cats:
    print "Too many cats! The world is doomed!"

# compare people with cat counts, True if people greater
if people > cats:
    print "Not many cats! The world is saved!"

# compare people with dogs counts, True if dogs greater
if people < dogs:
    print "The world is drooled on!"

# compare people with dogs counts, True if people greater
if people > dogs:
    print "The world is dry!"


# increase dogs count by 5
dogs += 5

# compare people with dogs counts, True if people greater or equal
if people >= dogs:
    print "People are greater than or equal to dogs."

# compare people with dogs counts, True if people less or equal
if people <= dogs:
    print "People are less than or equal to dogs."


# compare people with dogs counts, True if equal
if people == dogs:
    print "People are dogs."
