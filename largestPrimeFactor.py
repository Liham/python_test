num = 600851475143
numTest = 13195

import math 

def is_prime(n):
    if (n == 2):
        return True
    if (n % 2 == 0 or n <= 1):
        return False

    sqr = int(math.sqrt(n)) + 1

    for i in range(3, sqr, 2):
        if (n % i == 0):
            return False
    return True

divisor = []
for i in range(2,100000):
		if (is_prime(i) == True):
			if (num % i == 0):
				divisor.append(i)

largestPrimeFactor = max(divisor)

print ('The largest prime factor of ' + str(num) + ' is ' + 
	str(largestPrimeFactor))

