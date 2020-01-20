####Remenber to kepp all zeroes at n+1 term in string######
def noof(A):
	q = 0
	for f in range(0,len(A)-1):
		if (A[f] == '1'):
			q+=1
	return q
	
def order(B):
	for i in range(1,len(B)-1):
		key = noof(B[i])
		j = i -1	
		while j >=0 and key < noof(B[j]):
			B[j+1] = B[j]
			j -=1
		B[j+1] = B[i]
	return B

def common(A,B):
	count = 0
	C = ''
	for i in range(len(A) - 1):
		if(A[i] != B[i]):
			C += '-'
			count +=1
		else:
			C +=A[i]
	if (count ==1):
		C +='0'
		return C
	else:
		return None
		
def status(A,B):
	if(common(A,B)):
		A = A[:-1] 
		B = B[:-1]
		A += '1'
		B += '1'
	return A,B

def nxtbl(A):   ####m ------ no of tures for output
	C =[]
	for i in range(m-1):
		for j in range(i,m):
			if(common(A[i],A[j])):
				C.append(common(A[i],A[j]))
			A[i],A[j] = status(A[i],A[j])
	return C
