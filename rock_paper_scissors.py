import random,sys

def main():
	count = 0;
	guess = 3;
	win = 0;	loss = 0; 	tie = 0;

	print('Welcome to Rock, Paper, Scissor');
	while True:
		print('Win Loss Tie', win, loss, tie);
		while True:
			print('Enter your move: (r)ock, (p)aper, (s)cissor, (q)uit');
			choice =  input();

			if(choice == 'q'):
				sys.exit();
			if(choice == 'r' or choice == 'p' or choice == 's'):
				break;
			print('Type one of r, p, s, q');

		# Display user choices  of user
		if (choice == 'r'):
			print('Rock Versus ...');
		elif (choice == 'p'):
			print('Paper Versus ...');
		elif (choice == 's'):
			print('Scissor Versus ...');
		else:
			print('Enter the right choice');

		#Display computer choice 
		read_ch = random.randint(1,3);
		if (read_ch == 1):
			computer_ch = 'r';
			print('Rock');
		elif(read_ch == 2):
			computer_ch = 'p';
			print('Paper');
		elif(read_ch == 3):
			computer_ch = 's';
			print('Scissor');

		#Display & record the win/loss/tie
		if(choice == computer_ch):
			print('Its a Tie');
			tie = tie + 1;
		elif (choice == 'r' and computer_ch == 's'):
			print('You Win!');
			win = win + 1;
		elif (choice == 'p' and computer_ch == 'r'):
			print('You Win!');
			win = win + 1;
		elif (choice == 's' and computer_ch == 'p'):
			print('You Win!');
			win = win + 1;
		elif (choice == 'r' and computer_ch == 'p'):
			print('You Loss!');
			loss = loss + 1;
		elif (choice == 'p' and computer_ch == 's'):
			print('You Loss!');
			loss = loss + 1;
		elif (choice == 's' and computer_ch == 'r'):
			print('You Loss!');
			loss = loss + 1;

if __name__ == '__main__': main();
