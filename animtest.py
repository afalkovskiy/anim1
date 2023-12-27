import streamlit as st
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time

st.title("anim test 3")

x = []
y = []

fig, ax = plt.subplots()

# Setting limits for x and y axis
ax.set_xlim(0, 100)
ax.set_ylim(0, 12)

# Since plotting a single graph
line,  = ax.plot(0, 0)

def init():  # give a clean slate to start
    line.set_ydata([np.nan] * len(x))
def animation_function(i):
    x.append(i * 15)
    y.append(i)

    # line.set_xdata(x)
    # line.set_ydata(y)
    # return line,

# animation = FuncAnimation(fig,
#                           func = animation_function,
#                           frames = np.arange(0, 10, 0.1),
#                           interval = 10)
# plt.show()
txt1 = ''
st.write(txt1) 
st.header(txt1)
t = st.empty()
for i in range(20):
    # animation_function(i)
    txt1 = str(i)
    t.write(txt1) 
    time.sleep(1.5)
st.header(txt1)

st.write(txt1)  
# st.pyplot(fig)
fig, ax = plt.subplots()

ax = plt.gca()
xmin = 0.
ymin = 0.
xmax = 10.
ymax = xmax
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])

plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.grid(True)
st.pyplot(fig)

    

