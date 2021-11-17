def main():
	num = 5;
	for row in range(num+1):
		for col in range(num-row):
			print('*', end = ' ');
		print(' ');

if __name__ == '__main__': main();
