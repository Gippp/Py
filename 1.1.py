left = ('(', '[', '{', '<')
right = (')', ']', '}', '>')
stack = []
str = "(())([<>])"

for c in str:
	if c in left:
		stack.append(c)
	else:
		i = right.index(c)
		if stack[-1] == left[i]:
			stack.pop(-1)
		else:
			print("Not correct")
			exit(-1)
print("Correct")
