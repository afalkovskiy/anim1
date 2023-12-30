import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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

st.header('test Projectile Motion \n AF, Dec 2023')

col1, col2 = st.columns(2)
with col1:
    v = st.slider('Velocity (m/s)', value=120., min_value=1., max_value=1500.)
    # st.write("Velocity = ", v)
with col2:
    alpha = st.slider('Inclination to the horizontal (deg)', value=30., min_value=0., max_value=90.)
    alpha_rad = pi * alpha / 180.

chart = st.line_chart(np.zeros(shape=(1,1)))
x = np.arange(0, 100*np.pi, 0.1)

for i in range(1, 101):
    y = np.sin(x[i])
    status_text.text("%i%% Complete" % i)
    chart.add_rows([y])
    progress_bar.progress(i)
    time.sleep(0.05)

progress_bar.empty()
