import matplotlib
import numpy as np
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')

# fig = plt.figure(figsize=(7, 4))
# ax_3d = fig.add_subplot(projection='3d')


# # ===== level lines
# # === func contour() and contourf() - if data on x, y, z axes are represented as two-dimensional arrays
# x = np.arange(-2*np.pi, 2*np.pi, 0.2)
# y = np.arange(-2*np.pi, 2*np.pi, 0.2)
# xgrid, ygrid = np.meshgrid(x, y)
# zgrid = np.sin(xgrid) * np.sin(ygrid) / (xgrid * ygrid)

# ax_3d.contour(xgrid, ygrid, zgrid)
# ax_3d.contourf(xgrid, ygrid, zgrid)

# # !!! usage of contour() and contourf() for two-dimensional plot:
# fig, ax = plt.subplots(1, 2)
# ax[0].contour(xgrid, ygrid, zgrid)
# # !!! we can change the quantity of lines:
# ax[0].contour(xgrid, ygrid, zgrid, 15)
# ax[0].contour(xgrid, ygrid, zgrid, [-0.5, -0.2, 0, 0.2, 0.5])
# ax[0].contour(xgrid, ygrid, zgrid, colors='g')
# ax[0].contour(xgrid, ygrid, zgrid, colors=['g', 'b', 'r'])
# ax[0].contour(xgrid, ygrid, zgrid, cmap='palsma')

# ax[1].contourf(xgrid, ygrid, zgrid)

# # === func tricontour() and tricontourf() - if data for x, y, z are represented by one-dimensional arrays4
fig, ax = plt.subplots()
x = np.random.rand(100) * 4*np.pi - 2*np.pi
y = np.random.rand(100) * 4*np.pi - 2*np.pi

z = np.sin(x) * np.sin(y) / (1 + np.abs(x * y))
# c1 = ax.tricontour(x, y, z)
c1 = ax.tricontourf(x, y, z)

# # === clabel() add labels for lines of graphic
c1.clabel(colors='k', fmt='%.2f')

plt.show()
