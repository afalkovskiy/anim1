# import streamlit as st
# from matplotlib import pyplot as plt
# from matplotlib.animation import FuncAnimation
# import numpy as np
# import time

# st.title("anim test 4")

# x = [3, 4]
# y = [9, 16]

# fig, ax = plt.subplots()


# fig, ax = plt.subplots()

# ax = plt.gca()
# xmin = 0.
# ymin = 0.
# xmax = 100.
# ymax = xmax
# ax.set_xlim([xmin, xmax])
# ax.set_ylim([ymin, ymax])


# plot1, = ax.plot(x, y, 'o', color='red')
# plt.xlabel("X (m)")
# plt.ylabel("Y (m)")
# plt.grid(True)

# st.pyplot(fig)

# for i in range(1, 10):
#   x = [i, i + 1]
#   y = [i**2, (i + 1)**2]
#   # plot1.set_xdata(x)
#   # plot1.set_ydata(y)
#   # st.pyplot(fig.canvas.draw())
#   # st.pyplot(fig.canvas.flush_events())
#   # ax.plot(x, y, 'o', color='red')
#   time.sleep(2.5)
#   ax.plot(x, y, 'o', color='red')

import streamlit as st
import time
import numpy as np
import math


pi = math.pi
g = 9.81

def projectile(v, alpha, dt=0.01):
    vx = v * math.cos(alpha)
    vy = v * math.sin(alpha)
    g = 9.81
    t1 = vy/g
    t2 = 2*t1
    d = vx*t2
    h = vy*t1 - 0.5*g*t1**2
    t2 = 2 * vy / g
    t = np.linspace(0, t2, int(t2/dt))
    x = vx * t
    y = vy * t - 0.5 * g * np.square(t)
    return x, y, t2, d, h

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

st.header('test Projectile Motion \n AF, Dec 2023'

# col1, col2 = st.columns(2)
# with col1:
#     v = st.slider('Velocity (m/s)', value=120., min_value=1., max_value=1500.)
#     # st.write("Velocity = ", v)
# with col2:
#     alpha = st.slider('Inclination to the horizontal (deg)', value=30., min_value=0., max_value=90.)
#     alpha_rad = pi * alpha / 180.

chart = st.line_chart(np.zeros(shape=(1,1)))
x = np.arange(0, 100*np.pi, 0.1)

for i in range(1, 101):
    y = np.sin(x[i])
    status_text.text("%i%% Complete" % i)
    chart.add_rows([y])
    progress_bar.progress(i)
    time.sleep(0.05)

progress_bar.empty()




