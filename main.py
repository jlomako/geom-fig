# terminal: streamlit run main.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import io


@st.cache_data # caches data for session?
def create_spyro(number, selected):
    cmap = mpl.colormaps[selected]
    num_spirographs = np.random.randint(2, 4)
    fig = plt.figure()
    for i in range(num_spirographs):
        R = np.random.randint(1, 99)  # big circle radius
        r = np.random.randint(1, 50)  # small circle radius
        d = np.random.randint(1, 50)  # distance from the center of the small circle to the tracing point
        theta = np.linspace(0, 50 * np.pi, 500)
        x = (R - r) * np.cos(theta) + d * np.cos((R - r) / r * theta)
        y = (R - r) * np.sin(theta) - d * np.sin((R - r) / r * theta)
        plt.plot(x, y, c=cmap(i / num_spirographs), linewidth=0.3)
    plt.axis('equal')
    plt.axis('off')
    return fig


st.title("Spyrograph")

# get colormaps
colours = ["spring", "summer", "autumn", "winter"]
selected = st.radio(label="color", options=colours, horizontal=True, label_visibility="hidden")

plt.style.use('dark_background')
# #plt.style.use('default')


if st.button("Create") or selected:
    # refresh cache with random numbers
    st.pyplot(create_spyro(np.random.randint(1, 9999), selected))


fn = 'image.png'
img = io.BytesIO()
plt.savefig(img, format='png')

st.download_button(
    label="Save",
    data=img,
    file_name=fn,
    mime="image/png"
)


