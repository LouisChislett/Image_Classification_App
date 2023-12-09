import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load the model
model = load_model('image_classification.h5')

# CIFAR-10 categories
categories = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']


# Set up the title of the app
st.title('Image Upload and Display App')

# Create an image uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

def preprocess_image(uploaded_file):
    # Open the uploaded image
    img = Image.open(uploaded_file).convert('RGB')

    # Resize the image to 32x32 pixels
    img = img.resize((32, 32))

    # Convert the image to a numpy array
    img_array = np.array(img)

    # Scale the pixel values to be between 0 and 1
    img_array = img_array / 255.0

    # Add a batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    return img_array

# Display the uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Preprocess the image
    preprocessed_image = preprocess_image(uploaded_file)

    # Predict the category of the image
    predictions = model.predict(preprocessed_image)
    predicted_category = categories[np.argmax(predictions)]

    # Display the prediction
    st.write(f"This image is a {predicted_category}.")





