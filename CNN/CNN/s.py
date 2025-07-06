import numpy as np
from matplotlib import pyplot as plt

function = lambda x: (x ** 3)-(3 *(x ** 2))+7
x = np.linspace(-1,3,500)
plt.plot(x, function(x))
plt.axhline(0, color='y', alpha = 0.7)
plt.axvline(0, color='y', alpha = 0.7)
plt.grid()
plt.title("Function (x ** 3)-(3 *(x ** 2))+7 ")
plt.show()
