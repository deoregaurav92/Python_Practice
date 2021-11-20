def main():
	for i in incl_range(0,11,2):
		print(i, end=' ');
	print('');

def incl_range(*args):
	numrange = len(args);
	start = 0;
	step = 1;

	if numrange < 1:
		raise TypeError ('Too many less argument');
	elif numrange == 1:
		stop = args[0];
	elif numrange == 2:
		start = args[0];
		stop = args [1];
	elif numrange == 3:
		start = args[0];
		stop = args [1];
		step = args[2];
	else:
		raise TypeError('Too many argument');

	#Generator
	i = start;
	while i <= stop:
		yield i;
		i += step;

if __name__ == '__main__': main();
