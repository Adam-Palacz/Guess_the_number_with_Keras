import numpy as np
from keras import models
from convert_image import convert_app
from paint_number import paint_app


def test_image():
    paint_app()
    image = convert_app('./image.png')
    model = models.load_model('number_reader.model')
    data = np.asarray(image, )
    result = model.predict(np.array([data]))
    return f"Computer guessed number: {np.argmax(result)}"
