# function of two arguments printing ammounts of your goods
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print amount of cheese as format with integer
    print "You have %d cheeses!" % cheese_count
    # print amount of crackers as format with integer
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # print some garbage strings
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


def juce_and_coca(juce, coca):
    print "There are %d boxes of juce" % juce
    print "And %d bootles of coca" % coca

print "We can just give the function numbers directly:"
# Calling function with constant argumetns
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# calling function and passing variable values as its arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# call function and eval its arguments
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
# call function and eval its arguments based on variables
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# separate code
print '.' * 10

juce = 3
coca = 4

juce_and_coca(10, 11)
juce_and_coca(10 + 5, 11 + 4)
juce_and_coca(10 + 5, 11)
juce_and_coca(juce + 5, coca + 4)
juce_and_coca(juce, 11 + 4)
juce_and_coca(10 + 5, coca)
juce_and_coca(juce + 2 + 1, coca)
juce_and_coca(juce + coca - coca, juce - juce + coca)
