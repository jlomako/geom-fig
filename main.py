# terminal: streamlit run main.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Spirograph")

num_spirographs = np.random.randint(2, 4)

for i in range(num_spirographs):
    R = np.random.randint(1, 99)  # big circle radius
    r = np.random.randint(1, 50)  # small circle radius
    d = np.random.randint(1, 50)  # distance from the center of the small circle to the tracing point
    theta = np.linspace(0, 50 * np.pi, 500)
    x = (R - r) * np.cos(theta) + d * np.cos((R - r) / r * theta)
    y = (R - r) * np.sin(theta) - d * np.sin((R - r) / r * theta)
    plt.plot(x, y, linewidth=0.3)

plt.axis('equal')
plt.axis('off')

fig = plt
st.pyplot(fig)

