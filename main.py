from tensorflow import keras
from keras.models import load_model
from keras.applications.xception import preprocess_input
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
import streamlit as st
import cv2
# import tensorflow as tf
# print(tf.__version__)
# print(np.__version__)
# print(st.__version__)
# print(cv2.__version__)


st.write('# Cat and Dog Classifier')
st.markdown(
    '''
        This app uses transfer learning on  the Xception model to predict images of cats and dogs.
        It achieved an accuracy of approx. 99 percent on the validation set.
        
        > ### Enter an image of either a cat or a dog for the model to predict.
    '''
)

image_path = 'sample_images/hang-niu-Tn8DLxwuDMA-unsplash.jpg'
model = load_model('cat_and_dog_classifier.h5')  # model weights file
# print(model.summary())


def test_image(object_image):
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(object_image.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    opencv_image = cv2.resize(opencv_image, (200, 200))
    opencv_image.shape = (1, 200, 200, 3)
    opencv_image = preprocess_input(opencv_image)
    predictions = model.predict(opencv_image)

    if predictions[0, 0] >= 0.5:
        result = 'DOG'
        confidence = predictions[0, 0].round(3) * 100
    else:
        result = 'CAT'
        confidence = 100 - (predictions[0, 0].round(3) * 100)
        

    return result, confidence
    # it returns the predicted label and the precision i.e the confidence score


object_image = st.file_uploader("Upload an image...", type=[
                                'png', 'jpg', 'webp', 'jpeg'])
submit = st.button('Predict')

if submit:
    if object_image is not None:
        output = test_image(object_image)

        # Displaying the image
        st.image(object_image, channels="BGR")
        st.markdown(f"""## This is an image of a: {output[0]} """)
        st.write(f'## Confidence: { output[1]}%')


# print(f'The image was predicted as a {test_image(image_path)}')
