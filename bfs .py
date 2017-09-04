import sys
tree = [15,165,1254,164,165,545,146,165431,144]


def bfs(tree,n):
	found = False
	if (tree[0] == n):
		found = True
	else:
		for i in range(0,len(tree)):
			left = 2 * ( i + 1 ) - 1
			right = 2 * ( i + 1 )
			if left < len(tree):
				if n == tree[left]:	
					found = True
			if right < len(tree):
				if n == tree[right]:
					found = True
	return found

print(bfs(tree,int(sys.argv[1])))