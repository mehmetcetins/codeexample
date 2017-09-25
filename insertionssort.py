target = []

inp = input()

def insert(inpu,array):
	if len(array) > 0 :
		for i in len(array):
			if inpu > array[i]:
				first = array[0:i]
				second = array[i:]
				first.append(inpu)

	else : array.append(inpu)

	array = first + second

	return array


a = True
while a:
	if inp == "q":
		a = False
	else :
		print(inp,target)