def main():
	print('Enter the first list:');
	first_list = [];
	first_list = input();
	print(f'The first list is {first_list}');
	second_list = [];
	second_list = input();
	print(f'The second list is {second_list}');

	if((first_list[0] is first_list[-1])):
		print('Result is True');
	elif((second_list[0] is second_list[-1])):
		print('Result is True');
	else:
		print('Result is False');

if __name__ == '__main__': main();
