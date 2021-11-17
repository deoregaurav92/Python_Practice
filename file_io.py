def main():
#	out_file = open('out_file.txt', 'wt');

#	for i in range(11):
#		out_file.writelines(f'Line {i} \n');
#	out_file.close();
#	print('---Done---');

	in_file = open('out_file.txt', 'rt');
	out2_file = open('out2_file.txt', 'wt');
	count = 0;

	for i in in_file:
		if count == 5:
			continue;
		count = count + 1;
		out2_file.writelines(i);
	out2_file.close();
	print('------Done------');

if __name__ == '__main__': main();
