import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import NullFormatter, FormatStrFormatter, FuncFormatter, ScalarFormatter, FixedFormatter

matplotlib.use('TkAgg')

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-np.pi, np.pi, 0.1)
# ax.plot(x, np.sin(x))
ax.grid()

# # ===== format of coordinate axis labels
# # ===== func set_xticklabels()
# # !!! removes numeric values from the X-axis labels
# ax.set_xticklabels([])

# # ===== func set_yticklabels()
# # !!! removes numeric values from the Y-axis labels
# ax.set_yticklabels([])

# # ===== func set_major_formatter()

# # == NullFormatter()
# # !!! removes numeric values from the X-axis labels
# # !!!!! this approach is better !!!!!
# ax.xaxis.set_major_formatter(NullFormatter())
# ax.yaxis.set_major_formatter(NullFormatter())

# # == FormatStrFormatter()
# # !!! allows you to set the format of numerical values of labels
# ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
# ax.yaxis.set_major_formatter(FormatStrFormatter('%f'))
# ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# ax.yaxis.set_major_formatter(FormatStrFormatter('text = %.2f'))

# # == FuncFormatter()
# # !!! calls a function to generate numeric values
# def format_oy(x, pos):
#     return f'[{x}]' if x < 0 else f'({x})'
#
#
# ax.yaxis.set_major_formatter(FuncFormatter(format_oy))

# # == ScalarFormatter()
# # !!! displays numerical data as it is, but with minor manipulations
# # !!! matplotlib uses this formatter by default, and we can change it

# how it works without ScalarFormatter():
# ax.plot(x, np.sin(x) * 1e5)

# sf = ScalarFormatter()
# sf.set_powerlimits((-4, 4))

# # !!! we can change limits globally:
# matplotlib.rcParams['axes.formatter.limits'] = (-4, 4)

# ax.yaxis.set_major_formatter(sf)

# # == FixedFormatter()
# # !!! assigns a strictly defined value to each axis line
ax.xaxis.set_major_formatter(FixedFormatter(['a', 'b', 'c', 'd', 'e', 'f', 'g']))

plt.show()
