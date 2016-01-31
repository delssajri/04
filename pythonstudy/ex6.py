# assign string to x. String is fromated with %d - integer
x = "There are %d types of people." % 10
# assign string value to variable binary
binary = "binary"
# assign string value to variable do_not
do_not = "don't"
# assign string to y. String is formated with to substrings
y = "Those who know %s and those who %s." % (binary, do_not)

# print value of x
print x
# print value of y
print y

# print string with universal format specifier
print "I said: %r." % x
# print string with string format specifier
print "I also said: '%s'." % y

# assign boolean value to variable
hilarious = False
# assing string its format
joke_evaluation = "Isn't that joke so funny?! %r"

# print string with previously assigned format and value
print joke_evaluation % hilarious

# assing string value to w
w = "This is the left side of..."
# assign string value to e
e = "a string with a right side."

# print new string evaluted as sum of w and e
print w + e
