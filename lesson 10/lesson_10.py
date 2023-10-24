import matplotlib
import numpy as np
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

# # ===== histograms, bar graphs and pie charts
# # === histograms
# y = np.random.normal(0, 2, 500)
# ax.hist(y)
# # !!! we can change the quantity of intervals:
# ax.hist(y, 50)

# # === bar graphs
# # == func bar() = builds arbitrary bar graphs along the Ox axis
# x = [f'H{i+1}' for i in range(10)]
# y = np.random.randint(1, 5, len(x))
#
# y = np.random.normal(0, 2, 500)
# x = np.linspace(np.min(y), np.max(y), 10)
# bars = [len(y[np.bitwise_and(y >= x[i], y < x[i+1])]) for i in range(len(x)-1)]
# ax.bar(range(len(x)-1), bars)

# # func barh() - builds arbitrary bar charts along the Oy axis
# ax.barh(range(len(x)-1), bars)

# # !!! bar() and barh() properties
# x = [f'H{i+1}' for i in range(10)]
# y = np.random.randint(-20, 20, len(x))
# ax.bar(x, y, width=0.5, linewidth=2, edgecolor='r', yerr=2, bottom=10)

# x = np.arange(10)
# y1 = np.random.randint(3, 20, len(x))
# y2 = np.random.randint(3, 20, len(x))
# w = 0.3
# ax.bar(x - w/2, y1, width=w)
# ax.bar(x + w/2, y2, width=w)

# # === pie charts
values = [10, 40, 23, 30, 7]
labels = ['BMW', 'Toyota', 'Lexus', 'Audi', 'Mercedes']
exp = [0.1, 0.2, 0, 0, 0]
# ax.pie(values, labels=labels)
# ax.pie(values, labels=labels, autopct='%.2f', explode=exp, shadow=True)
ax.pie(values, labels=labels, autopct='%.2f', wedgeprops=dict(width=0.5), shadow=True)

ax.grid()
plt.show()
