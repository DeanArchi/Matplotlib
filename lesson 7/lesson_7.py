import matplotlib
import numpy as np
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')

# # ===== typical design of graphs
# y = np.arange(0, 5)
# x = np.array([a*a for a in y])
# y2 = [0, 2, 3, 4, 5, 7]
# x2 = [i+1 for i in y2]
# line = plt.plot(x, y, x2, y2)
# plt.minorticks_on()
# plt.grid(which='major', color='#444', lw=1)
# plt.grid(which='minor', color='#aaa', ls=':')

# # == inscription and signature creation
# # !! you can define such text elements for each axis:
# # title - title for axes
# # xlabel, ylabel - signatures for each axis
# # text - text information in the axis area
# # annotate - annotation

# # for window (Frame) you can define such text elements:
# # suptitle - title for frame
# # figtext - placing text information in the frame area

fig = plt.figure(figsize=(7, 4), facecolor='#eee')
ax = fig.add_subplot(facecolor='#AAFFAA')
plt.figtext(0.05, 0.6, 'Text in the frame area', fontsize=24, color='r')
fig.suptitle('Frame title')
ax.set_xlabel('Ox')
ax.set_ylabel('Oy')
ax.text(0.05, 0.1, 'Text in the axis area', bbox={'boxstyle': 'darrow', 'facecolor': '#AAAAFF'})
ax.annotate('Annotation', xy=(0.2, 0.4), xytext=(0.6, 0.7),
            arrowprops={'facecolor': 'gray', 'shrink': 0.1})

plt.show()
