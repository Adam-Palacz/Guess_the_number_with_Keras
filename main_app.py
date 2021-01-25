from Guess_the_number_with_Keras.train_model import train_model
from Guess_the_number_with_Keras.test_model import test_model
from Guess_the_number_with_Keras.plot_number import plot_number

# Use only if you didn't create model
model_name = input("Input model name")
print(train_model(model_name))

try:
    number = int(input("Input test label number(1-999):"))
except ValueError as error:
    print("Wrong input", error)
else:
    if number not in range(1, 1000):
        print("Number not in range")
    else:
        print(test_model(number))
        print(plot_number(number))


