'''target=[1,2,3,4,5,6]
print(target[0:4],target[3:])

def insert(inpu,array):
	if len(array) > 0 :
		for i in range(len(array)):	
			if inpu > array[i]:
				first = array[0:i+1]
				second = array[i+1:]
				first.append(inpu)
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

'''

from exampleClass import example


target=[33 , 44 , 21 , 83 , 56 , 73 , 22]


print(example.insertsort(target))




































