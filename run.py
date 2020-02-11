#Made for the sole purpose of GCI 2019
import numpy as np
import random
import time
import os
os.system("clear")
print()
def prRed(skk): return str("\033[91m {}\033[00m" .format(skk)) 
def prYellow(skk): return str("\033[93m {}\033[00m" .format(skk)) 
def prPurple(skk): return str("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): return str("\033[96m {}\033[00m" .format(skk)) 
print((prRed("This program would generate 10 matrices which are giving garbage values i.e. having a high conditional value")))
print()
time.sleep(1)
x=int(input(prCyan("Enter the order of matrix : ")))
print()
a=10
try1=0
while a!=0:	
	tmp1=np.random.rand(x,x)
	id1=np.identity(x)
	condition=np.linalg.cond(tmp1)
	y=np.linalg.inv(tmp1)
	z=np.dot(tmp1,y)
	if (z!=id1).any():
	    a-=1
	    try1+=1
	    print(prYellow(str(try1)+")"))
	    print()
	    print(prPurple("Matrix Generated :\n\n "+str(tmp1)))
	    time.sleep(2)
	    print()
	    print(prCyan("Inverse of the generated matrix :\n\n "+str(y)))
	    time.sleep(2)
	    print()
	    print(prYellow("Matrix * Inverse of that Matrix :\n\n "+str(z)))
	    print()
	    time.sleep(2)
	    print(prRed("The above matrix should've been an identity matrix but it isn't, so the generated matrix is giving out garbage values"))
	    print()
	    time.sleep(2)
	    print(prYellow("Condition Number of Matrix: "+str(np.linalg.cond(tmp1))))
	    print()
	    time.sleep(5)
print(prPurple("Hence, to conclude you really can't trust numeric computations with these ill-conditioned matrices!"))
