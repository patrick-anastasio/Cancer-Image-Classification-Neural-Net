import tensorflow as tf

model = tf.keras.models.load_model('my_model.hdf5')

import streamlit as st

st.write("""
         # ALL Detection
         """
         )

st.write("This is a simple image classification web app to predict if a cell is cancerous or normal")

file = st.file_uploader("Please upload an image file", type=["jpg", "png", "bmp"])


import cv2
from PIL import Image, ImageOps
import numpy as np
def import_and_predict(image_data, model):

        size = (450,450)
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img_resize = (cv2.resize(img, dsize=(256, 256),    interpolation=cv2.INTER_CUBIC))/255.

        img_reshape = img_resize[np.newaxis,...]

        prediction = model.predict(img_reshape)

        return prediction

if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    prediction = import_and_predict(image, model)

    if np.argmax(prediction) == 0:
        st.write("NORMAL")
    elif np.argmax(prediction) == 1:
        st.write("ALL")

    st.text("Probability (0: Normal, 1: ALL,")
    st.write(prediction)
