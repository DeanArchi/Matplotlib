import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import *

matplotlib.use('TkAgg')

# # ===== legend for graphs

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

# === 1 case
# ax.plot(np.arange(0, 5, 0.25), label='line 1')
# ax.plot(np.arange(0, 10, 0.5), label='line 2')
# ax.plot(np.arange(0, 5, 0.25), '--o', label='line 1')
# ax.plot(np.arange(0, 10, 0.5), ':s', label='line 2')

# # !!! to use this method you need to add param 'label' to the graphs
# ax.legend()

# === 2 case
# ax.plot(np.arange(0, 5, 0.25))
# ax.plot(np.arange(0, 10, 0.5))
#
# ax.legend(['1 line', '2 line'])

# !!! param 'loc' of func legend():
ax.plot(np.arange(0, 5, 0.25), '--o', label='line 1')
ax.plot(np.arange(0, 10, 0.5), ':s', label='line 2')
# ax.legend(loc='best')
# ax.legend(loc='upper right')
# ax.legend(loc='upper left')
# ax.legend(loc='lower left')
# ax.legend(loc='lower right')
# ax.legend(loc='right')
# ax.legend(loc='center left')
# ax.legend(loc='center right')
# ax.legend(loc='lower center')
# ax.legend(loc='upper center')
# ax.legend(loc='center')

# # !!! legend() properties
# ax.legend(facecolor='#aaa', framealpha=0.5)

# # == Line2D
# l1 = Line2D([1, 2, 3], [1, 2, 4])
# ax.add_line(l1)

# # === patches
# rect = Rectangle((0, 0), 2.5, 0.5, facecolor='g')
# ax.add_patch(rect)

plt.show()
