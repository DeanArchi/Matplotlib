import time

import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation, ArtistAnimation

matplotlib.use('TkAgg')

# # ===== animation of graphs
# # !!! to create an animated graph, you need to create an interactive graph playback mode with func ion()
# plt.ion()
#
# fig, ax = plt.subplots()
# x = np.arange(-2*np.pi, 2*np.pi, 0.1)
# y = np.cos(x)
#
# line, = ax.plot(x, y)
#
# for delay in np.arange(0, np.pi, 0.1):
#     y = np.cos(x+delay)
#
#     line.set_ydata(y)
#
#     plt.draw()
#     plt.gcf().canvas.flush_events()
#
#     time.sleep(0.02)
#
# plt.ioff()

# # ==== class FuncAnimation
# fig, ax = plt.subplots()
# x = np.arange(-2*np.pi, 2*np.pi, 0.1)
# y = np.cos(x)
#
# line, = ax.plot(x, y)
#
#
# def update_cos(frame, line, x):
#     """
#     frame - parameter that changes from frame to frame
#     in this case it is the initial phase
#     line - reference to Line2D object
#     """
#     line.set_ydata(np.cos(x + frame))
#     return [line]
#
#
# phase = np.arange(0, 4*np.pi, 0.1)
#
# animation = FuncAnimation(
#     fig,                # figure, where animation is displayed
#     func=update_cos,    # current frame update function
#     frames=phase,       # parameter that changes from frame to frame
#     fargs=(line, x),    # additional parameter for the update_cos() function
#     interval=30,        # delay between frames in ms
#     blit=True,          # whether to use double buffering
#     repeat=False        # loop the animation
# )


# # ==== class ArtistAnimation
fig = plt.figure(figsize=(10, 6))
ax_3d = fig.add_subplot(projection='3d')

x = np.arange(-2*np.pi, 2*np.pi, 0.2)
y = np.arange(-2*np.pi, 2*np.pi, 0.2)
xgrid, ygrid = np.meshgrid(x, y)

phase = np.arange(0, 2*np.pi, 0.1)
frames = []

for p in phase:
    zgrid = np.sin(xgrid + p) * np.sin(ygrid) / (xgrid * ygrid)

    line = ax_3d.plot_surface(xgrid, ygrid, zgrid, color='b')
    frames.append([line])

animation = ArtistAnimation(
    fig,
    frames,
    interval=30,
    blit=True,
    repeat=True
)

plt.show()
