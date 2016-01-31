# function evals sum of to integers
def add(a, b):
    # print operation, use format %d to treat a and b as integers
    print "ADDING %d + %d" % (a, b)
    # return sum of function arguments
    return a + b


# function evals substraction of to integers
def subtract(a, b):
    # print operation, use format %d to treat a and b as integers
    print "SUBTRACTING %d - %d" % (a, b)
    # return substraction of function arguments
    return a - b


# function evals product of to integers
def multiply(a, b):
    # print operation, use format %d to treat a and b as integers
    print "MULTIPLYING %d * %d" % (a, b)
    # return product of function arguments
    return a * b


# function evals ratio of to integers
def divide(a, b):
    # print operation, use format %d to treat a and b as integers
    print "DIVIDING %d / %d" % (a, b)
    # return ratio of function arguments
    return a / b


# function evals 'what' from puzzle part of task
def puzzle(age, height, weight, iq):
    # print operation, use format %d to treat a and b as integers
    print "PUZZLE %d + %d - %d * %d / 2" % (age, height, weight, iq)
    # return formula value
    return age + height - weight * iq / 2


# print following string
print "Let's do some math with just functions!"

# call add function to eval sum of two integers, store result in age variable
age = add(30, 5)
# call substract function to eval substract of two integers, store result in
# height variable
height = subtract(78, 4)
# call multiply function to eval product of two integers, store result in
# weight variable
weight = multiply(90, 2)
# call deivide function to eval ratio of two integers, store result in iq variable
iq = divide(100, 2)

# print variables as integers
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

# age + height - weight * iq / 2
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

what2 = puzzle(age, height, weight, iq)
print "Yes, I can. What from puzzle is: ", what2, "Its equal to ", what
