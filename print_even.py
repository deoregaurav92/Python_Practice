def main():
	print('Enter the string');
	my_str = str(input());
	print(f'The origanl string is {my_str}');
	print('Printing only even index chara');

	length = len(my_str);
	for i in range (0, length-1,2):
		print(my_str[i]);

if __name__ == '__main__': main();
