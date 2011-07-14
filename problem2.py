def main():
	prev = 1
	curr = 1
	sum = 0
	while (curr < 4000000):
		temp = curr
		curr += prev
		prev = temp
		if curr % 2 == 0:
			sum += curr
	print sum
main()
