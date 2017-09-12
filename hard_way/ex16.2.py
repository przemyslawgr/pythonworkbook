from sys import argv

script, filename = argv

print "Opening the file..."
target = open(filename, 'w')

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I,m going to write these to the file."



target.close()

txt = open("hello.txt")

print txt.read()