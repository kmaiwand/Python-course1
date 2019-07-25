##~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Variables
##myVar = 7
##print( myVar)	# 7
##name = input( 'What is your name? ')
##print( name)
##
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Numbers
##number = 1 + 2 * 3 / 4.0
##print( number)	# 2.5
##
##fahrenheit = 86
##print( (fahrenheit - 32) * 5/9)
##
##fahrenheit = int( input( 'Degrees in fahrenheit: '))
##print( 'Celsius =', (fahrenheit - 32) * 5/9)
##
##year = 2008
##print( year % 400 == 0 or ( year % 4 == 0 and year % 100 != 0))
##
##year = int( input( 'Enter the year: '))
##print('Leap year: ', year % 400 == 0 or ( year % 4 == 0 and year % 100 != 0))
##
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Strings
##sentence = "The quick brown FOX"
##sentence = sentence + ' jumps'
##print( '~' * 20)	#~~~~~~~~~~~~~~~~~~~~
##
##name = input("What is your name? ")
##print( 'Hello ' + name)
##
##print( sentence.upper(), '|', sentence.lower())	#THE QUICK BROWN FOX JUMPS the quick brown fox jumps
##print( 'length:', len( sentence))	#25
##
##print( sentence[4])	#q
##print( sentence[ 2:8])	#e quic
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Conditions
##num = int( input( 'Enter a numbr: '))
##if( num % 2 == 0):
##	print('Even')
##else:
##	print('Odd')
##	if num % 3 != 0:
##		print( 'And not divisible by 3')
##
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Collections
##myList = [12.5, 4, 102, -35]
##print( myList)
##print( '2nd:', myList[1])
##print( 'last:', myList[-1])
##for element in myList:
##	print( '\t', element)
##
##Find all divisors of a number
##num = int( input( 'enter a number: '))
##divisors = []
##for i in range( 1, num):
##	if num % i == 0:
##		divisors.append( i)
##print( 'Divisors:', divisors)
##
#Create a string consisting of list elements separated by '_'
##myList = [ 'spam', 'eggs', 'rice']
##print( myList)
##str = ''	# initialize the string
##for el in myList:
##	str += el + '_'
##str = str[0:-1]	# remove the trailing underscore
##print( 'Combined:', str)
##print( 'Better: ', "_".join( myList))
##
###Reverse the order of elements 
##myList = [12.5, 4, 102, -35]
##print( myList)
##rev = []
##for index in range( len(myList), 0, -1):
##	rev.append( myList[index-1])
##print( 'upsideDown:', rev)
##myList.reverse()
##print( 'Better reverse:', myList)
##
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Sort elements
##def bubble_sort( lst):
##	for last in range( len(lst)-1, 0, -1):
##		for i in range( last):
##			if lst[i] > lst[i+1]:
##				lst[i], lst[i+1] = lst[i+1], lst[i]	# swap
##	return lst
##
##print( bubble_sort( [34.0, -56, 0.001]))
##print( 'Better sort:', sorted( [34.0, -56, 0.001]))
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Functions
##def great( name):
##	print( "Hello", name)
##great( 'Mark')
##
##def avg( lst):
##	result = 0
##	for el in lst:
##		result += el
##	return result/len(lst)
##print( avg( [12, 34, 65]))
##
##def sq_root( N, eps):
##	""" Approximate square root of N within +/- eps (a positive float). """
##	root = N/2     # initail guess
##	while( abs( root**2 - N) > eps):
##		print( '\tcurrent root', root)
##		root = (root + N/root)/2
##	return root
##num = float( input( 'Enter a number: '))
##print( 'root:', sq_root( num, 0.001))
##import math
##print( 'Better root:', math.sqrt( num))

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Modules
##def area( radius):
##	return 3.14 * radius**2
##print( area(2.0))
##import random
##
##def gamble():
##	min, max = 1, 6
##	roll_again = "y"
##	while roll_again == "y":
##		print( "Rolling the dices...", random.randint(min, max), ',', random.randint(min, max))
##		roll_again = input("Roll the dice again (y/n)? ")
##gamble()
##
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Working with Files
##import os
##def rename( dir, name, ext):
##	""" Rename each file in 'dir' to 'name' with a sequential number and '.ext' """
##	if not name:    # if no name given use directory's name
##		name = os.path.split( dir)[1]
##	print( "\n" + dir)
##	for nr, old in enumerate( os.listdir( dir)):
##		new = '{}-{:0>2d}.{}'.format( name, nr, ext)
##		os.rename( os.path.join( dir, old), os.path.join( dir, new))
##		print( "{:<20} -> {}".format( old, new))
##rename( '../Test', 'spam', 'txt')
##
##import os
##def search_all( dir, pattern, ext):
##	""" look for pattern in dir in files whose extension is in ext """
##	print( "\nLooking in '{}' for '{}' in files with extension '{}'".format( dir, pattern, ext))
##	for file in os.listdir( dir):
##		path_file = os.path.join( dir, file)
##		if os.path.splitext( file)[1] in ext:
##			for nr, line in enumerate( open( path_file, 'r').readlines()):
##				if line.find( pattern) >= 0:
##					print( "In {} line {}".format( file, nr+1))
##
##search_all( '../Test', 'Hotel', ['.txt'])
##
