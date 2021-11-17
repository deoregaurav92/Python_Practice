def main():
	print('Enter the base');
	base = int(input());
	print('Enter the exponent');
	expo = int(input());
	print(f'{base} raise to the power of {expo} is {exponent(base,expo)}');

def exponent(base, expo):
	return base**expo;

if __name__ == '__main__': main();
