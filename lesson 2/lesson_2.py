import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

# x = np.array([4, 5, 6, 7, 8])
# y = np.array([1, 2, -6, 0, 4])
# # === if plot() has 1 argument - takes the list of values for Y-axis
#  plt.plot(y)
# # === if plot() has 2 arguments - 1st takes the list of values for X-axis and 2nd for X-values
# plt.plot(x, y)

# x1 = np.array([1, 1, 5, 5, 1])
# y1 = np.array([1, 5, 5, 1, 1])
# plt.plot(x1, y1)

# x2 = np.arange(0, 5)
# y2 = np.array([y*y for y in x2])

# x3 = [0, 1, 2, 3]
# y3 = [i+1 for i in x3]
# plt.plot(x2, y2)

# # !!! to display multiple graphs, you need to specify other coordinates (x, y, x, y, etc.) separated by commas.
# # !!! or use another or call another plot()

# # 1 case:
# plt.plot(x2, y2, x3, y3)

# # 2 case:
# plt.plot(x2, y2)
# plt.plot(x3, y3)

x4 = np.arange(0, 5)
y4 = np.array([y*y for y in x4])
# # !!! parameter 3 is responsible for the type of line display. In this case, it is a dotted line
# plt.plot(x4, y4, '--')
# plt.plot(x4, y4, '-')  # fixed line, by default
# plt.plot(x4, y4, '-.')  # dashed line ( _ . _ . )
# plt.plot(x4, y4, ':')  # dotted line ( . . . . )
# plt.plot(x4, y4, 'None')  # without drawing a line
# plt.plot(x4, y4, ' ')  # without drawing a line

# line = plt.plot(x4, y4)
# # !!! plot() returns a list for the Line2D object, so we can control the display of lines by the Line2D object
# print(line)
# # === setp() sets certain properties
# plt.setp(line, linestyle='-.')

# # !!! setp() can control 2 or more graphics:
x5 = [0, 1, 2, 3]
y5 = [i+1 for i in x5]
# lines = plt.plot(x4, y4, x5, y5)
# plt.setp(lines, linestyle='--')


# # !!! we can change color of the lines:
# # 'b' as blue
# # 'g' as green
# # 'r' as red
# # 'c' as cyan
# # 'm' as magenta
# # 'y' as yellow
# # 'k' as black
# # 'w' as white
# lines = plt.plot(x4, y4, '--r', x5, y5, ':m')
# lines = plt.plot(x4, y4, 'r--', x5, y5, 'm:')
# # !!! parameter 'color' set the same color to all graphics
# # !!! we can also set the color using the 16-bit code, RGB (numbers from 0 to 1). 4 param in RGB means transparency
# lines = plt.plot(x4, y4, '--', x5, y5, ':', color='k')
# lines = plt.plot(x4, y4, '--', x5, y5, ':', color='#0000CC')
# lines = plt.plot(x4, y4, '--', x5, y5, ':', color=(0, 1, 0))
# lines = plt.plot(x4, y4, '--', x5, y5, ':', color=(0, 1, 0, 0.4))


# # !!! we can change markers of points
# # markers: 'o', 'v', '^', '<', '>', '2', '3', '4', 's', '*', 'h', 'H', '+', 'x', '|', '_'
# lines = plt.plot(x4, y4, '--ro', x5, y5, ':ms')
# lines = plt.plot(x4, y4, '--rv', x5, y5, ':m^')
# lines = plt.plot(x4, y4, '--r<', x5, y5, ':m>')
# lines = plt.plot(x4, y4, '--r2', x5, y5, ':m3')
# lines = plt.plot(x4, y4, '--r4', x5, y5, ':m*')
# lines = plt.plot(x4, y4, '--rh', x5, y5, ':mH')
# lines = plt.plot(x4, y4, '--r+', x5, y5, ':mx')
# lines = plt.plot(x4, y4, '--r|', x5, y5, ':m_')

# # !!! we can use parameter 'marker' to set markers
# lines = plt.plot(x4, y4, '--r', x5, y5, ':m', marker='+')

# # !!! parameter 'markerfacecolor' set fill color to markers
# lines = plt.plot(x4, y4, '--o', x5, y5, ':s', markerfacecolor='y')


# # !!! we can use step() for all this parameters
# lines = plt.plot(x4, y4, x5, y5)
# plt.setp(lines[0], linestyle='-.', color='b', marker='o', markerfacecolor='y', linewidth=4)
# plt.setp(lines[1], linestyle=':', color='m', marker='s', markerfacecolor='w', linewidth=3)

# # !!! PARAMETERS OF FUNCTION setp():
# # alpha
# # color || c
# # linestyle || ls
# # linewidth || lw
# # marker
# # markeredgecolor || mec
# # markeredgewidth || mew
# # markerfacecolor || mfc
# # markersize || ms


# # ===== fill areas of the graph
# # ===== fill_between() function
x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.cos(x)
plt.plot(x, y)
# plt.fill_between(x, y)
# plt.fill_between(x, y, 0.5)
# plt.fill_between(x, y, 0.5, where=(y < 0))
# plt.fill_between(x, y, 0.5, where=(y < 0))
plt.fill_between(x, y, where=(y < 0), color='r', alpha=0.5)
plt.fill_between(x, y, where=(y > 0), color='g', alpha=0.5)



# === grid() for displaying the grid
plt.grid()
plt.show()
