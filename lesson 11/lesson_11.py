import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

matplotlib.use('TkAgg')

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

# # ===== displaying images and color grids
# === images
# img = Image.open('image.jpg')
# ax.imshow(img)

# # !!! imshow() properties
# img = np.array(Image.open('image.jpg'))
# ax.imshow(img, origin='lower', cmap='Grays', aspect='equal', alpha=0.7)

# # we can show color map of image:
# a = ax.imshow(img, origin='lower', cmap='plasma', aspect='equal', alpha=0.7)
# plt.colorbar(a)

# # === pcolormesh() func
data = np.random.randint(0, 255, (10, 10))
# plt.pcolormesh(data)
a = plt.pcolormesh(data, edgecolor='black', cmap='plasma')
plt.colorbar(a)

plt.show()
