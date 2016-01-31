def while_loop(limit, increment=1):
    i = 0
    numbers = []
    while i < limit:
        print "At the top i is %d" % i
        numbers.append(i)

        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers


def for_loop(limit, increment=1):
    numbers = []
    for i in range(0, limit, increment):
        print "At the top i is %d" % i
        numbers.append(i)

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers

print "Build numbers with while loop def"
numbers = while_loop(6)
print "The numbers: "
for num in numbers:
    print num

print "Build numbers with for loop def"
numbers = for_loop(4, 2)
print "The numbers: "
for num in numbers:
    print num
