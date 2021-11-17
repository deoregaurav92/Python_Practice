def main():
	n = 0;
	number = [];
	while (n < 5):
		print('Enter the floating point number');
		item = float(input());
		number.append(item);
		n = n + 1;

	print(f'The list is {number}');

if __name__ == '__main__': main();

