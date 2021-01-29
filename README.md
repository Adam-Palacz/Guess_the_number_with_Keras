# Guess_the_number_with_Keras
Small application using easy neural network based on Keras library to guess by computer the number imputed from user by Paint App created in Tkinker (medium success rate depending on accuracy drawn number).

# Interface
Application interface is located in main_app.py. Interface give us 5 options:
![interface](graphs/interface.png)

### 1. Show available test numbers
Show all available images numbers from mnist library which we can test our model.(test number is that same as number in test image)
In function show_test_numbers we have commented option showing all dataframe (9999 numbers!) 

![test_numbers](graphs/show_test_numbers.png)

### 2. Test model using test number
Choose index number from mnist test data and test correctness trained model.
We will get error information if our input isn't a number or that number isn't in range 0-999 corresponding test label index.
If our input is correct we get test_model function result which takes imputed mnist test image label and return
guessed number from our model. Function also plot image our chosen label.
![test_model](graphs/test_model_with_image.png)



