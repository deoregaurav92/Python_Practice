import time, sys
indent = 0
indentincr = True

try:
	while True:
		print(' ' * indent, end='');
		print('*******');
		time.sleep(0.1)

		if indentincr:
			indent = indent +1;
			if indent == 5:
				indentincr = False
		else:
			indent = indent - 1;
			if indent == 0:
				indentincr = True
except Keywordintrrupt:
	sys.exit();

