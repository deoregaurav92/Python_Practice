def main():
	print('Enter the string:');
	my_str = str(input());
	print('Enter the number of character you want to remove:');
	rm_char = int(input());
	print(f'The orignal string is {my_str}');
#	out_str = [];
	out_str = remove_char(my_str, rm_char);
	print(f'The string after {out_str}');

def remove_char(my_str, rm_char):
	out_str = my_str[rm_char:];
	return out_str;

#	length = len(my_str);
#	my_list = [];
#	for i in range(rm_char, length):
#		my_list = my_str[i];
#	return my_list;

if __name__ == '__main__': main();
