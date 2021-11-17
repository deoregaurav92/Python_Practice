def main():
	print('Enter the number:');
	num = int(input());
	sum = 0;
	print(f'Printing current and previous number sum in range({num})');

	for i in range(num):
		sum = (i) + (i-1);
		if i == 0:
			print(f'Current Number 0 Previous Number 0 Sum: 0');
		else:
			print(f'Current Number {i} Previous Number {i-1} Sum: {sum}')

if __name__ == '__main__': main();

