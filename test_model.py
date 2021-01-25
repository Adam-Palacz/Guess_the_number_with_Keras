import numpy as np
from keras import models
from keras.datasets import mnist


def test_model(number):
    model = models.load_model('number_reader.model')
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
    img = test_images[number]
    img = img.astype('float32') / 255
    img = img.reshape((28 * 28))
    result = model.predict(np.array([img]))
    return np.argmax(result)
