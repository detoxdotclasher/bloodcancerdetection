import streamlit as st
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.preprocessing import image 
import numpy as np 

# Set page title and favicon
st.set_page_config(page_title='BLOOD CANCER DETECTOR WEB APP', page_icon='C:/Users/rickb/Documents/favicon_io (1)/favicon.ico')

# Define the CNN
model = Sequential()

# Add convolutional layer
model.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))

# Add pooling layer
model.add(MaxPooling2D(pool_size=(2, 2)))

# Add second convolutional layer
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Flattening
model.add(Flatten())

# Full connection
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

# Compile the CNN
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Load and preprocess the image
def load_image(img_path, show=False):
    img = image.load_img(img_path, target_size=(64, 64))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.  # Model was trained with inputs scaled to [0, 1]

    if show:
        plt.imshow(img_tensor[0])
        plt.axis('off')
        plt.show()

    return img_tensor

# Streamlit code to create a title and a file uploader
st.title('BLOOD CANCER DETECTOR WEB APP')
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    new_image = load_image(uploaded_file)

    # Predict the probability of the image being blood cancer
    pred = model.predict(new_image)

    # Print the result
    if pred[0][0] > 0.5:
        prediction = (f'Blood Cancer Detected:{pred[0][0]}')
    else:
        prediction = 'Blood Cancer Not found'

    st.write(prediction)
