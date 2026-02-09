import numpy as np
import matplotlib.pyplot as plt
from aaa import BarycentricRational, aaa

nodes = np.array([1.0, 4.0, 9.0])
values = np.array([1.0, 2.0, 3.0])
weights = np.array([0.5, -1, 0.5])
f = BarycentricRational(nodes, values, weights)

x = np.linspace(0.1, 10, 1000)
y = f(x)

plt.figure()
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

print(f(1.0))
print(f(4.0))
print(f(9.0))

poles, residues = f.polres()
print(poles)