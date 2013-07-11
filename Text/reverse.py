def main():
	print "Please enter a string to reverse"
	string = raw_input("> ")
	print string[::-1]



again = 'y'
while again.lower() == 'y' or again.lower() == 'yes':
	main()
	print "Do you want to reverse another?"
	again = raw_input("Y/N: ")