import matplotlib.pyplot as plt
from keras.datasets import mnist


def plot_number(number):
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
    image = test_images[number]
    plt.imshow(image, cmap=plt.cm.binary)
    plt.show()

