def main():
	print('Enter the first list');
	first_list = [];
	first_list = input();
	print('Enter the second list');
	second_list = [];
	second_list = input();
	print('');
	print(first_list);
	print(second_list);
	new_list = [];

	for i in first_list:
		if i%2 != 0:
			new_list.append(i);
	for j in second_list:
		if j%2 == 0:
			new_list.append(j);

	print(new_list);

if __name__ == '__main__': main();
