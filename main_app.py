from train_model import train_model
from test_model import test_model
from plot_number import plot_number
from test_image import test_image
from keras import models
from keras.datasets import mnist
import pandas as pd


# Use only if you didn't create model
def train_new_model():
    model_name = input("Input model name")
    train_model(model_name)
    return "Model saved"


# Test model using test dataframe


def show_test_numbers():
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
    result = pd.DataFrame(test_labels)
    return result.head(100)


def test_model_with_numbers():
    try:
        number = int(input("Input test label number(1-999):"))
    except ValueError as error:
        print("Wrong input", error)
    else:
        if number not in range(0, 1000):
            print("Number not in range")
        else:
            print(test_model(number))
            plot_number(number)


if __name__ == '__main__':
    while True:
        options = {1: "Show part test numbers", 2: "Test model using test number",
                   3: "Test model using painted number", 4: "Train new model (Use if you are using app first time!)",
                   5: "End program"}
        print("\nMENU\n")
        for key, values in enumerate(options):
            print(values, options[values])
        try:
            print("*" * 10)
            option = int(input("Choose option: "))
            print("*" * 10)
        except ValueError as error:
            print("Wrong input", error)
        else:
            if option == 1:
                print(show_test_numbers())
            elif option == 2:
                test_model_with_numbers()
            elif option == 3:
                print(test_image())
            elif option == 4:
                print(train_new_model())
            elif option == 5:
                break
            else:
                print("Wrong option")
