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
# st.text(txt1) 
st.header(txt1)
for i in range(20):
    # animation_function(i)
    txt1 = str(i)
    time.sleep(1.5)

# st.text(txt1)  
# st.pyplot(fig)

    

