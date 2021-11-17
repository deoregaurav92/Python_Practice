def main():
	print('Enter the string:');
	my_str = str(input());
	print(f'The origanl string is {my_str}');
	my_list = [];
	my_list = my_str.split();
	count = 0;

	for i in my_list:
		if i.upper() == 'EMMA' or i.lower() == 'emma':
			count = count + 1;
	print(f'The Emma appears {count}');

if __name__ == '__main__': main();
