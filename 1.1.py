braces = {')': '(', '}': '{', ']': '[', '>': '<'}
stack = ''
str = '((<>)[])'

flag = True
for s in str:
	if s in braces.values():
		stack += s
	else:
		if stack[-1] == braces[s]:
			stack = stack[:-1]
		else:
			flag = False
			break
if stack: 
	flag = False

print(flag)

