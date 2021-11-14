import random

def getanswer(num):
	if num == 1:
		return 'It is certain';
	elif num == 2:
		return 'It is decidely so';
	elif num == 3:
		return 'Yes';
	elif num == 4:
		return 'Reply Hazy try again';
	elif num == 5:
		return 'Ask again later';
	elif num == 6:
		return 'Concentrate and ask again';
	elif num == 7:
		return 'My reply is no';
	elif num == 8:
		return 'Outlook not so good';
	elif num == 9:
		return 'Very doubutful';
	else:
		return 'Wrong Choice';

n = random.randint(1,9);
return_str = str(getanswer(n));
print(return_str);
