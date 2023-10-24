import matplotlib
import numpy as np
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

# # ===== step, stack, stem and dot plots
# # === step plot
# x = np.arange(0, 10)
# ax.step(x, x)
# ax.step(x, x, '--go')
# ax.step(x, x, '--go', where='pre')  # 'pre' is default
# ax.step(x, x, '--go', where='post')
# ax.step(x, x, '--go', where='mid')
# ax.step(x, x, '--go', x, np.cos(x), '-x', where='mid')


# # === stack plot
# x = np.arange(-2, 2, 0.1)
# y1 = np.array([-y**2 for y in x]) + 8
# y2 = np.array([-y**2 for y in x]) + 8
# y3 = np.array([-y**2 for y in x]) + 8
# ax.stackplot(x, y1, y2, y3)

# # === stem plot
# x = np.arange(-np.pi, np.pi, 0.3)
# ax.stem(x, np.cos(x))
# !!! we can change value of baseline:
# ax.stem(x, np.cos(x), bottom=0.5)
# ax.stem(x, np.cos(x), '--r', bottom=0.5)

# # === dot plot()
x = np.random.normal(0, 2, 500)
y = np.random.normal(0, 2, 500)

# ax.scatter(x, y)
ax.scatter(x, y, s=50, c='g', linewidths=1, marker='s', edgecolors='r')

ax.grid()
plt.show()
