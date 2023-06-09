#program to print a positive integer
import numpy as np
list1=np.array([-1,6,9,2,-7,-5])
ps=list1[list1 >=0];
print("LIST = ",list1)
#printing the positive integers
print("\nPOSITIVE INTEGERS IN THE LIST : ",*ps)
