from keras import models, layers
from keras.datasets import mnist
from keras.utils import to_categorical


def train_model(model_name):
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

    network = models.Sequential()
    network.add(layers.Dense(256, activation='relu', input_shape=(28 * 28,)))
    network.add(layers.Dense(10, activation='sigmoid'))
    network.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    train_labels = to_categorical(train_labels)
    train_images = train_images.reshape((60000, 28 * 28))
    train_images = train_images.astype('float32') / 255

    network.fit(train_images, train_labels, epochs=5, batch_size=128)
    network.save(f'{model_name}.model')

