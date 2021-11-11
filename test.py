
passwd = 'swordfish';
count = 0;
total = 3;

for count in range(3):
	print('Whats your name');
	myname = input();
	if myname == 'Dev':
		print('Hello Dev');
		print('Attempt' ' ' + str(int(count))+ '' 'Enter the password Dev:');
		in_passwd = input();
		if in_passwd == passwd:
			print('Access Granted');
		else:
			print('Access Denied');
	else:
		print('Who are you?' ' ' +str(int(total-count-1))+ ' '  'attempt remaining');
		if (count == 2):
			print('Try after sometime');

