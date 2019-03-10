import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
font = {'family': 'meiryo'}
matplotlib.rc('font', **font)

a = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]])
b = np.random.rand(10)
print(a[0:1, 3:5])

plt.scatter(a[0, 0:], b)
plt.show()
'''
y = data[0:58905, 1]
fig, ax = plt.figure()
ax = fig.add_subplt(1, 1, 1)
ax.scatter(x, y)
'''
