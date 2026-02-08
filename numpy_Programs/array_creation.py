#1 array creation
import numpy as np
a=np.array([1,2,3,4,5])
b=np.arange(1,10,2)
c=np.linspace(0,10,5)
d=np.zeros((3,3))
e=np.ones((3,3))
f=np.eye(3)
g=np.random.randint(1,100,size=(3,3))
print("Array a:",a)
print("Arrange b:",b)
print("Linspace c:",c)
print("Zeros d:",d)
print("Ones e:",e)
print("Identity matrix f:",f)
print("Random matrix g:",g)

