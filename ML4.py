import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-5, 5, 100)
y = 2*x+1

plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.title('Grap y=2x+1')
plt.grid()
plt.show()

