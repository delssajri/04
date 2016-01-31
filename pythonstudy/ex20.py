# import argv to access launch arguments
from sys import argv

# assign first argument (script name) to script variable, assign filename to
# second argument
script, input_file = argv


# def to print entire file
def print_all(f):
    # read file from current position to end and print content
    print f.read()


# def to move position to file begin
def rewind(f):
    # call seek to set position to file begin
    f.seek(0)


# def to print one line with its number in the file
def print_a_line(line_count, f):
    # read one line than print its number and content
    print line_count, f.readline()

# open input_file (first script argument) and store its object in current_file
# variable
current_file = open(input_file)

# print info string with addition carrage return
print "First let's print the whole file:\n"

# print the entire file
print_all(current_file)

# print line to separate entire file content from its line by line print
print "Now let's rewind, kind of like a tape."

# set current position to file begin to be able to read this file once more
rewind(current_file)

# print that we are going to print three lines
print "Let's print three lines:"

# initialize current_line variable with 1
current_line = 1

# call function to print one line from current_file object with line number 1
print_a_line(current_line, current_file)

# increase current line by one
current_line += 1

# print once more line from the current_file object with line number 2
print_a_line(current_line, current_file)

# increase current line number by one once more
current_line += 1

# print third line from current_file object with line number 3
print_a_line(current_line, current_file)
