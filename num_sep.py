def main():
	print('Enter the number:');
	num = int(input());
#	print(f'The reverse number is {rev_num(num)}');
	rev_num(num);

def rev_num(n):
	while n > 0:
		remainder = n%10;
		n = n // 10;
		rev_str.append(remainder);
		print(remainder, end=' ');

if __name__ == '__main__': main()
