import numpy as np
import matplotlib.pyplot as plt
from sympy import *

a, b = symbols('a b')



A = np.array([a+b,a-b])
B = np.array([a-b,a+b])

I = (a*B+b*A)/a+b
E = (a*B-b*A)/a+b

print("Internal and External points are : ",simplify(I),simplify(E))
