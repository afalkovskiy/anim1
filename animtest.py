import streamlit as st
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time

st.title("anim test 4")

x = [3]
y = [9]

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

fig, ax = plt.subplots()

ax = plt.gca()
xmin = 0.
ymin = 0.
xmax = 100.
ymax = xmax
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])

plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.grid(True)

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

x = [3]
y = [9]

plt.scatter(x, y)

# st.pyplot(fig)

txt1 = ''
st.write(txt1) 
st.header(txt1)
t = st.empty()
for i in range(20):
    # animation_function(i)
    txt1 = str(i)
    x=[i]
    y=[i*i]
    t.write(txt1) 
    time.sleep(.5)
    plt.scatter(x, y)
    st.pyplot(fig)
st.header(txt1)

# st.pyplot(fig)

st.write(txt1)  
# st.pyplot(fig)


    

