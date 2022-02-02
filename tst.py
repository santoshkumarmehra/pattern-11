n=5
for i in range(1,n+1):
	x=i
	for j in range(1,n+1):
		if x%2==0:
			print("0",end="")
		else:
			print("1",end="")
		x=x+1
	print()
