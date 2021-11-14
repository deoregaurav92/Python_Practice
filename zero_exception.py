def spam(num):
	try:
		return 42/num;
	except ZeroDivisionError:
		return 'Error! Can not divide by zero';

print(spam(2));
print(spam(0));
print(spam(1));
