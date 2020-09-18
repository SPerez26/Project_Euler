#Problem 48

total_sum = 0

for i in range(1,1001):
	total_sum += i**i

print(str(total_sum)[-10:])