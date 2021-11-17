def main():
	print('Enter the number:');
	num = int(input());
	orignal_num = num;

	rev_num = 0;
	while num > 0:
		remainder = num % 10;
		rev_num = rev_num*10 + remainder;
		num  = num //10;

	if rev_num == orignal_num:
		print(f'The {orignal_num} number is palindrome');
	else:
		print(f'The {orignal_num} number is not palindrome');

if __name__ == '__main__': main();
