## NumPy Array Example

|     Code             | Output            |
|------                |           --------|
| ```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.arange(1, 10, 2)
c = np.linspace(0, 10, 5)
d = np.zeros((3, 3))
e = np.ones((3, 3))
f = np.eye(3)

print("Array a:", a)
print("Arange b:", b)
print("Linspace c:", c)
print("Zeros d:")
print(d)
print("Ones e:")
print(e)
print("Identity matrix f:")
print(f)
``` | ```text
Array a: [1 2 3 4 5]
Arange b: [1 3 5 7 9]
Linspace c: [ 0.   2.5  5.   7.5 10. ]
Zeros d:
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
Ones e:
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
Identity matrix f:
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
``` |

