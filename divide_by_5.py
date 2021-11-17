def main():
	print('Enter the list:');
	my_list = [];
	my_list = input();
	print(f'The given list is {my_list}');

	for i in my_list:
		if i % 5 == 0:
			print(i);

if __name__ == '__main__': main();
