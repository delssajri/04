# import argv to access command arguments
from sys import argv

# assign script name and filename from command line arguments
script, filename = argv

# open file and asign its object to txt
txt = open(filename)

# print filename
print "Here's your file %r:" % filename
# print entire file content
print txt.read()

# query another file name and assign it to variable
print "Type the filename again:"
file_again = raw_input("> ")

# open this file and store its object
txt_again = open(file_again)

# print all content of this file
print txt_again.read()

# we dont need to close files because OS will do it for us
# But normaly its better to close such objects`
