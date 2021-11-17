def main():
	print('Enter the number:');
	num = int(input());
	table(num);

def table(num):
	for col in range(1,num+1):
		for row in range(1,11):
			print(row*col, end= ' ');
		print('\t\t');

if __name__ == '__main__': main();
