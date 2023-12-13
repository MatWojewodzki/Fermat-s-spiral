import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


rotation_step = np.pi / 64

plt.style.use('ggplot')

plt.figure(num='Wykres biegunowy')
plt.subplot(111, projection='polar')

theta1 = np.linspace(0, 9 * np.pi, 300)
theta2 = theta1 + np.pi

r = 0.2 * np.sqrt(theta1)


def animate(frame):
    plt.cla()
    plt.plot(theta1 + (frame * rotation_step), r, color='#d41313')
    plt.plot(theta2 + (frame * rotation_step), r, color='#d41313')

    plt.ylim(0, 1.05)
    plt.autoscale(False)
    plt.gca().axes.yaxis.set_ticklabels([])
    plt.title('Spirala Fermata - animacja')


anim = FuncAnimation(plt.gcf(), animate, interval=16, cache_frame_data=False)

plt.show()
