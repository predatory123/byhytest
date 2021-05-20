import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt

squares = [1,4,9,16,25]
# plt.plot(squares)
plt.show()


x = np.arange(1, 11)
y = 2 * x + 5
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x, y)
plt.show()



plt.plot(np.arange(10))
plt.show()
