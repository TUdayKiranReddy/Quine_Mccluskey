from function import *
import time

start_time = time.time()
C = ['0000','0011','0101','0110','0111','1010','1100','1101','0010','1001','1111']

A = []
C = init(C)
#print(order(C))
m = len(C)

A.append(C)
A.append(nxtbl(C))
#print(A[0])

for i in range(1,m-1):
	if(A[i] !=[]):
		A.append(nxtbl(A[i]))
		#print(A[i])
	else:
		break
	
#print(primertr(A))

print("--- %s seconds ---" % (time.time() - start_time))
