def fibb(n):
	if not n:
		return 0
	a = [0, 1, 1]
	for i in range(n-3):
		a[0] = a[1]
		a[1] = a[2]
		a[2] = a[0] + a[1]
	return a[2]

for i in range(10):
    print(fibb(i))
