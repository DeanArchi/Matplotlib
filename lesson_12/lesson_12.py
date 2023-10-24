import matplotlib
import numpy as np
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')

fig = plt.figure(figsize=(7, 4))
ax_3d = fig.add_subplot(projection='3d')

# # === 3D graphics
# # === plot() - 2D line graph in 3 dimensions
# x = np.linspace(0, 10, 50)
# z = np.cos(x)
# ax_3d.plot(x, x, z)

x = np.arange(-2*np.pi, 2*np.pi, 0.2)
y = np.arange(-2*np.pi, 2*np.pi, 0.2)
xgrid, ygrid = np.meshgrid(x, y)
zgrid = np.sin(xgrid) * np.sin(ygrid) / (xgrid * ygrid)
# # === plot_wireframe() - 3D construction of the frame surface
# ax_3d.plot_wireframe(xgrid, ygrid, zgrid)
# # === plot_surface() - building a continuous 3D surface
# ax_3d.plot_surface(xgrid, ygrid, zgrid)
# # !!! params rstride and cstride it's a step
# ax_3d.plot_surface(xgrid, ygrid, zgrid, rstride=5, cstride=5, cmap='plasma')


# # === scatter() - 3D dot plot
ax_3d.scatter(xgrid, ygrid, zgrid, s=1, color='g')




# # !!! we can set labels to all axes:
# ax_3d.set_xlabel('x')
# ax_3d.set_ylabel('y')
# ax_3d.set_zlabel('z')

plt.show()
