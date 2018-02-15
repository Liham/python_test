value = 1
previousValue = 1
printValue = 0 

while (value <= 4000000):
	value = value + previousValue
	value2 = value - previousValue
	if (value % 2 == 0):
		printValue = printValue + value

print ('The sum of the even Fibonacci numbers under 4 million is ' + 
	str(printValue))