import numpy as np
from keras import models
from PIL import Image
from paint_number import paint_app


def test_image():
    paint_app()
    model = models.load_model('number_reader.model')
    image = Image.open('image.jpg')
    image = image.resize((28,28), Image.ANTIALIAS)
    data = np.asarray(image,)
    data = data[:,:,1]
    data = data.astype('float32') / 255
    data = data.reshape((28*28))
    result = model.predict(np.array([data]))
    return np.argmax(result)



