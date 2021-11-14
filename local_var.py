def spam():
	egg = 100;
	egg=ham();
	print(egg);

def ham():
	h = 101;
	egg = 0;
	return egg;
spam();

a = 22;
b = 33;
def fun_a():
	print('The value of a inside function are:',a,b);
fun_a();
print('The value of a outside are:',a,b);
