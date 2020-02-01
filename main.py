from function import *

Minimised_Prime_Implecants,Prime_Implecants,Inputs,No_of_variables,time_taken = main("ssd.txt")
W =[]
for a in Prime_Implecants:
	W.append((expressiongnr(a)))
print("Prime Implecants",W)

W =[]
for a in Prime_Implecants:
	W.append((expressiongnr(a)))
print("Prime Implecants",W)
print("Final Expression is ",expr(Minimised_Prime_Implecants))

table(Prime_Implecants,Inputs,create_chart_save(Prime_Implecants,Inputs))
