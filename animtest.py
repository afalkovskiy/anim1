import streamlit as st
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time

st.title("anim test 4")

x = [3, 4]
y = [9, 16]

fig, ax = plt.subplots()


fig, ax = plt.subplots()

ax = plt.gca()
xmin = 0.
ymin = 0.
xmax = 100.
ymax = xmax
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])


ax.plot(x, y, 'o', color='red')
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.grid(True)

for i in range(1, 10):
  x = [i, i + 1]
  y = [i**2, (i + 1)**2]
  time.sleep(0.5)
  ax.plot(x, y, 'o', color='red')
  st.pyplot(fig)


