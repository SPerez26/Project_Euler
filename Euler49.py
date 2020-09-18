#Problem 49

import math

def sumfactorial(number):

	sumfact = 0

	for i in str(number):
		sumfact += math.factorial(int(i))

	if sumfact == number:
		return True
	else:
		return False

count = 0
sumnumb = 0

for i in range(3,99999):
	if sumfactorial(i) == True:
		#print(i)
		count +=1
		sumnumb += i

print(f"Numbers found: {count}")
print(f"Sum of number found: {sumnumb}")