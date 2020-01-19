####Remenber to kepp all zeroes at n+1 term in string######
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
		while key < noof(B[j]):
			while j >=0 :
				B[j+1] = B[j]
				j -=1
		B[j+1] = B[i]
	return B

def common(A,B):
	count = 0
	C = ''
	for i in range(len(A)):
		if(A[i] != B[i]):
			C += '-'
			count +=1
		else:
			C +=A[i]
	if (count ==1):
		
		return C
	else:
		return None
