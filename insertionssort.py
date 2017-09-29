

def insert(inpu,array):
	if len(array) > 0 :
		for i in range(len(array)):	
			if inpu < array[i]:
				first = array[0:i]
				second = array[i:]
				first = [inpu] + first
				array = first + second
				break
			else : 
				target.append(inpu)
				break

	else : array.append(inpu)
	print(array)
	return array

target = []
a = True
while a:
	inp = input()
	if inp == "exi":
		a = False
		print(target)
	else:
		target = insert(int(inp),target)