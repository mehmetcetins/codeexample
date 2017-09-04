alf = ["m","e","h","t","ç","i","n"]
key = ["f","a","g","o","s","l","t"]
frq = [2,3,1,2,1,1,1]

name = "mehmet çetin"
crypted = ""
uncrypted = ""
for char in name :
	if char == " ":
		crypted += " "
	else : crypted += key[alf.index(char)]
