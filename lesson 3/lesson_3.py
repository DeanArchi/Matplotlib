import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec

matplotlib.use('TkAgg')

# ===== displaying several coordinate axes
# ===== func subplot(nrows, ncols, index)

# plt.subplot(1, 3, 1)
# plt.plot(np.random.random(10))
# plt.subplot(1, 3, 2)
# plt.plot(np.random.random(10))
# plt.subplot(1, 3, 3)
# plt.plot(np.random.random(10))

# plt.grid()

# # !!! in this case, grid() is applied to the last active plot
# # !!! to avoid this, you can save plots in variables and call grid() for all of them:

# plt1 = plt.subplot(1, 3, 1)
# plt.plot(np.random.random(10))
# plt2 = plt.subplot(1, 3, 2)
# plt.plot(np.random.random(10))
# plt3 = plt.subplot(1, 3, 3)
# plt.plot(np.random.random(10))
#
# plt1.grid()
# plt2.grid()
# plt3.grid()

# plt1 = plt.subplot(2, 3, 1)
# plt.plot(np.random.random(10))
# plt2 = plt.subplot(2, 3, 2)
# plt.plot(np.random.random(10))
# plt3 = plt.subplot(2, 3, 3)
# plt.plot(np.random.random(10))
# plt4 = plt.subplot(2, 1, 2)
# plt.plot(np.random.random(10))
#
#
# plt1.grid()
# plt2.grid()
# plt3.grid()
# plt4.grid()

# # ===== func subplots(nrows, ncols, index)
# f, ax = plt.subplots(2, 2)
#
# f.set_size_inches(7, 4)  # size 7 x 4 inches
# f.set_facecolor((0, 1, 0))  # background color
#
# ax[0, 0].plot(np.arange(0, 5, 0.2))
# ax[0, 0].grid()
# ax[0, 1].plot(np.arange(0, 10, 2))
# ax[0, 1].grid()
# ax[1, 1].plot(np.arange(10, 0, -2))
# ax[1, 1].grid()

# # ===== func figure() - creates new window
# fig = plt.figure(figsize=(7, 4))
# plt.plot(np.arange(0, 5))

# # ==== func add_subplot() is identical to the subplot()
# ax1 = fig.add_subplot(1, 3, 1)
# ax1.plot(np.arange(0, 5))
# plt.show()


# # ===== graph layout using GridSpec
fig = plt.figure(figsize=(7, 4))
gs = GridSpec(ncols=3, nrows=2, figure=fig)

ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(np.arange(0, 5, 0.2))

ax2 = fig.add_subplot(gs[1, 0:2])
ax2.plot(np.random.random(10))

ax3 = fig.add_subplot(gs[:, 2])
ax3.plot(np.random.random(10))

plt.show()
