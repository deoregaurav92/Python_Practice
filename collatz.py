import sys

def main():
	print('Welcome to Collatz Program');
	print('Enter your number');
	num = int(input());
	try:
		val = collatz(num);
		while (val != 1):
			val = collatz(val);
	except input_error:
		print('This is a string input');
		sys.exit();

def collatz(n):
	if n%2 == 0:
		print(int(n/2));
		return int(n/2);
	elif n%2 == 1:
		print(int(3*n+1));
		return int(3*n + 1);

if __name__ =='__main__': main()
