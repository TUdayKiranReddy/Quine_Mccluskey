def noof(A):
	q = 0
	for f in range(0,len(A)):
		if (A[f] == '1'):
			q+=1
	return q
	
def order(B):
	for i in range(1,len(B)):
		key = noof(B[i])
		j = i -1
		print(type(B[j]),type(noof(B[j])))
		while j >=0 and key < noof(B[j]):
			B[j+1] = B[j]
			j -=1
		B[j+1] = key
	return B
