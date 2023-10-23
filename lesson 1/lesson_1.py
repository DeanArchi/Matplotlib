import matplotlib
from matplotlib import pyplot as plt

# # rendering graphics in Tk
matplotlib.use('TkAgg')
print(matplotlib.get_backend())

plt.plot([1, 2, -6, 0, 4])
plt.show()
