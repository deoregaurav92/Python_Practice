def main():
	print('Enter the Row value:');
	row = int(input());
	print('Enter the Column Value:');
	col = int(input());
	print('');

	for i in range(row+1):
		for j in range(i):
			print(i,end='');
		print('');

if __name__ == '__main__': main();
