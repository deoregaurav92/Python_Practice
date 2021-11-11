import sys

def main():
	while True:
		print('Enter your responese:');
		res = input();
		if (res == 'exit'):
			print('Good Bye!');
			sys.exit();

if __name__ == '__main__': main();

