import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import NullLocator, LinearLocator, MultipleLocator, IndexLocator, FixedLocator, LogLocator, MaxNLocator

matplotlib.use('TkAgg')

# # ===== limit values of coordinate axes
# # ===== func set(xlim=(xmin, xmax), ylim=(ymin, ymax))

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(1, 5, 0.25))
ax.grid()
# ax.set(xlim=(-5, 30), ylim=(-1, 6))

# # ===== functions set_xlim() and set_ylim()
# # !!! with this functions we can set only initial limit of X or Y axes, and final limit is set automatically
# ax.set_xlim(-5, 30)
# ax.set_ylim(-1, 6)

# ax.set_xlim(xmin=-5)
# ax.set_ylim(ymin=-1)

# # ===== func set_major_locator() - large grid risk management

# # !!! NullLocator()
# # we'll see only horizontal grid lines
# ax.xaxis.set_major_locator(NullLocator())
# # we'll see only vertical grid lines
# ax.yaxis.set_major_locator(NullLocator())

# # !!! LinearLocator()
# # on the X-axis we will see only 10 elements
# ax.xaxis.set_major_locator(LinearLocator(10))
# # on the Y-axis we will see only 5 elements
# ax.yaxis.set_major_locator(LinearLocator(5))

# # !!! MultipleLocator()
# the step on the X-axis between the lines is 1 element
# ax.xaxis.set_major_locator(MultipleLocator(base=0.5, offset=0))
# the step on the Y-axis between the lines is 2 element
# ax.yaxis.set_major_locator(MultipleLocator(base=2))

# # !!! IndexLocator()
# x = np.arange(-np.pi/2, np.pi, 0.1)
# ax.plot(x, np.sin(x))
# ax.xaxis.set_major_locator(IndexLocator(base=0.5, offset=0))
# ax.xaxis.set_major_locator(IndexLocator(base=0.5, offset=0.57))

# # !!! FixedLocator()
# # we will see only those lines that were specified in the list
# ax.xaxis.set_major_locator(FixedLocator([-2, -1, 0, 1, 2, 3]))

# # !!! LogLocator()
# # it works like base ^ i, where i += 1
# ax.xaxis.set_major_locator(LogLocator(base=2))

# # !!! MaxNLocator()
# # performs a split along the coordinate axis by the specified number of lines
# ax.xaxis.set_major_locator(MaxNLocator(5))

# ===== func set_minor_locator() - small grid risk management
# # !!! to use it you need to call this method:
ax.minorticks_on()
ax.grid(which='major', lw=2)
ax.grid(which='minor')

# ax.xaxis.set_minor_locator(NullLocator())
# ax.xaxis.set_minor_locator(LinearLocator(5))
# ax.xaxis.set_minor_locator(MultipleLocator(base=0.25))
# ax.xaxis.set_minor_locator(IndexLocator(base=0.5, offset=0))
# ax.xaxis.set_minor_locator(FixedLocator([-2, -1, 0, 1, 2, 3]))
# ax.xaxis.set_minor_locator(LogLocator(base=2))
# ax.xaxis.set_minor_locator(MaxNLocator(5))

plt.show()
