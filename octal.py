def main():
	n1 = 0;
	print('Enter the number: ');
	num = int(input());
	print(f'The given number in decimal is {num}');
	result = dec_oct(num);
	while (result > 0):
		n = result%10;
		n1 = n1*10 + n;
		result = result//10;
	print(f'The octal representation of number is {n1}');

def dec_oct(num):
	result = 0;
	quo = num;

	while (quo > 0):
		rem = int(quo%8);
		result = result*10 +rem;
		quo = int(quo//8);

	return result;

if __name__ == '__main__': main();
