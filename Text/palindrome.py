def main():
	print "Enter a string"
	thestring = raw_input("> ")
	revd = thestring[::-1]
	if thestring == revd:
		print "Yes, this can be reversed and look the same!"
	else:
		print "No, this string cannot be reversed and look the same."

again = 'y'
while again.lower() == 'y' or again.lower() == 'yes':
	main()
	print "Do you want to test another?"
	again = raw_input("Y/N: ")