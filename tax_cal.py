def main():
	print('Enter the total amount');
	amount = int(input());
	tax = tax_cal(amount);
	print(f'The total tax is {tax}');

def tax_cal(num):
	count = 3;
	tax = 0;

	while(count > 0):
		if (count == 3):
			tax = tax + 10000*0;
			num = num - 10000;
		elif (count == 2):
			tax = tax + 10000*0.1;
			num = num - 10000;
		else:
			tax = tax + num*0.2;
		count = count - 1;
	return tax;

if __name__ == '__main__': main();
