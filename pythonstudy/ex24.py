# print simple string
print "Let's practice everything."
# print string with escaped ', \, new line, and tab
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

# assign multiline string with escaped symbols to poem. Some lines are
# additionaly splitted by \n sequence
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# print the poem
print "--------------"
print poem
print "--------------"


# store formula result in five variable
five = 10 - 2 + 3 - 6
# print formula result
print "This should be five: %s" % five


# function evals some secret formula and returns a tuple of values
def secret_formula(started):
    # store product in local variable jelly_beans
    jelly_beans = started * 500
    # store ratio in local variable jars
    jars = jelly_beans / 1000
    # store ratio in local variable crates
    crates = jars / 100
    # return tuple
    return jelly_beans, jars, crates


# initialize start_point
start_point = 10000
# eval secret formula by calling function and assign tuple entries to tree
# variables
beans, jars, crates = secret_formula(start_point)

# print start point as integer
print "With a starting point of: %d" % start_point
# print formula result supplying it as tuple to print
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# reassing start point
start_point = start_point / 10

print "We can also do that this way:"
# evalute secret formula and print result tuple
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
