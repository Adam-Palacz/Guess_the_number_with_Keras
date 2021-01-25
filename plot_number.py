import matplotlib.pyplot as plt
from keras.datasets import mnist


def plot_number(number):
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
    img = test_images[number]
    result = plt.imshow(img, cmap=plt.cm.binary)
    plt.show()
    return result
