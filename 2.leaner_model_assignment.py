import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]
l_sum = 0
W = np.arange(0.0, 4.1, 0.1)
B = np.arange(-2.0, 2.1, 0.1)
[w, b] = np.meshgrid(W, B)


def forward(x):
    return w * x + b


def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y)**2


for x_val, y_val in zip(x_data, y_data):
    y_pred_val = forward(x_val)
    loss_val = loss(x_val, y_val)
    l_sum += loss_val
print(l_sum.shape)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(w, b, l_sum/3, cmap='rainbow')
plt.show()
