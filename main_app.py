from train_model import train_model
from test_model import test_model
from plot_number import plot_number
from test_image import test_image
from keras.datasets import mnist
import pandas as pd


# Use only if you didn't create model
def train_new_model():
    """Train new model recognizing numbers based on neural network and Keras library.

    :return: string informing about successful created and saved model
    """
    train_model()
    return "Model saved"


def show_test_numbers():
    """Show all available images numbers from mnist library which we can test our model.
    (test number is that same as number in test image)

    :return: Pandas dataframe with test numbers and their indexes in table
    """
    # train_images and train_labels aren't used but we need them for importing mnist data
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
    result = pd.DataFrame(test_labels, columns=["test numbers"])
    # if we want to see all dataframe (9999 numbers!)
    # pd.set_option("display.max_rows", None)
    return result


def test_model_with_numbers():
    """Choose index number from mnist test data and test correctness trained model

    :return Error information if our input isn't a number or that number isn't in range 0-999 corresponding test label
    index.
    If our input is correct we get test_model function result which takes imputed mnist test image label and return
    guessed number from our model. Function also plot image our chosen label.
    """
    try:
        number = int(input("Input test label number(0-999):"))
    except ValueError as err:
        print("Wrong input", err)
    else:
        if number not in range(0, 1000):
            print("Number not in range")
        else:
            print(f"Computer guessed: {test_model(number)}")
            plot_number(number)


# application interface
if __name__ == '__main__':
    while True:
        options = {1: "Show available test numbers", 2: "Test model using test number",
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
                print("""Thank you for launching the application. See you later.
                
                Author: Adam Palacz""")
                break
            else:
                print("Wrong option")
