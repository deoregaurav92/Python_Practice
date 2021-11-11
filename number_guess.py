import random

def main():
	print('I am thinking number between 1 to 20');
	count = 0;
	orignal = int(random.randint(1,20));
	for i in range(1,5):
		print('Take a guess:');
		count = count + 1;
		num = int(input());
		if (num < orignal):
			print('Your guess is too low', num);
			continue;
		elif (num > orignal):
			print('Your guess is too high', num);
			continue;
		else:
			break;
	if (num == orignal):
		print('Good Job! YOu guessed the number in ', count);
	else:
		print('Sorry! the number was : ',orignal);

if __name__ == '__main__': main();
