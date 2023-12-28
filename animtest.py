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


ax.plot(x, y, linestyle='o')
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.grid(True)
st.pyplot(fig)
