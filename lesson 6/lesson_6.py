import matplotlib
import numpy as np
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')

# # ===== logarithmic scale of coordinate axes

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

x = np.arange(-10*np.pi, 10*np.pi, 0.1)
ax.plot(x, np.sinc(x) * np.exp(-np.abs(x/10)))

# # ===== func semilogy() - on the Y-axis makes a logarithmic scale
# ax.semilogy(x, np.sinc(x) * np.exp(-np.abs(x/10)))
# # ===== func semilogx() - on the X-axis makes a logarithmic scale
# ax.semilogx(x, np.sinc(x) * np.exp(-np.abs(x/10)))

# # !!! we can man a logarithmic scale for plot() func:
# # ===== func set_yscale() - redefines the scale in the Y axis
# ax.plot(x, np.sinc(x) * np.exp(-np.abs(x/10)))
# ax.set_yscale('log')
# # ===== func set_xscale() - redefines the scale in the X axis
# ax.set_xscale('log')

# # parameters of func set_yscale():
# # linear - linear scale
# # log - logarithmic scale
# # symlog - near 0 the scale is linear, and in the rest of the region it is logarithmic

# # !!! default logarithm base 10, but we can change it:
# ax.set_yscale('log', base=2)

# # symlog usage:
# ax.set_xscale('symlog', linthresh=2)

# # ===== func loglog() - set a logarithmic scale for both axes
ax.loglog(x, np.sinc(x) * np.exp(-np.abs(x/10)))

ax.grid()
plt.show()
