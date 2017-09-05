import sys
results = []
def fibonacci(n):
	if n == 1:
		return 1
	elif n == 2:
		return 1
	else :
		return fibonacci( n - 1 ) + fibonacci( n - 2 )


if len(sys.argv) > 1:
	inp = sys.argv[1]
else : inp = "asdas"
try :
	int(inp)
except ValueError :
	inp = input("sayı gir lan : ")

print(fibonacci(int(inp)))
