import streamlit as st
#import cv2
import numpy as np
#from keras.models import load_model

# # Import the class labels from labels.txt and assign to a list
# classes = [' '.join(x.split(' ')[1:]).replace('\n','') for x in open('labels.txt', 'r').readlines()]
# # Load the Model
# model = load_model('keras_model.h5', compile = False)

# # Create the streamlit Title and camera_input
# st.title(f'Is it {classes[0]} or {classes[1]}!?')
# img_file_buffer = st.camera_input(f"Take a picture of {classes[0]} or {classes[1]}")


# # Trigger when a photo has been taken and the bugger is no longer None
# if img_file_buffer is not None:
#     # Get the image and process it as required by the model
#     # We are reshaping and converting the image to match the input the model requires.
#     bytes_data = img_file_buffer.getvalue()
#     cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
#     image = cv2.resize(cv2_img, (224, 224), interpolation=cv2.INTER_AREA)
#     image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
#     image = (image / 127.5) - 1
#     probabilities = model.predict(image)

#     # We now have the probabilities of the image being for either class
#     # Check if either probability is over 80%, if so print the message for that classes.
#     if probabilities[0,0] > 0.8:
#         prob = round(probabilities[0,0] * 100,2)
#         st.write(f"I'm {prob}% sure that's {classes[0]}!")
#     elif probabilities[0,1] > 0.8:
#         prob = round(probabilities[0,1] * 100,2)
#         st.write(f"I'm {prob}% sure that's {classes[1]}!")
#     else:
#         st.write("I'm not confident that I know what this is! ")

#     # End on balloons
#     st.balloons()
