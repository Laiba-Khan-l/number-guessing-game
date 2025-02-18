# Number Guessing Game  

This is a simple command-line Python application that implements a number guessing game. The computer randomly selects a number between 1 and 100, and the player has three attempts to guess the number correctly.  

## Features  

- Random number generation between 1 and 100.  
- 3 attempts to guess the number.  
- Feedback on whether the guess is too high or too low.  
- Displays the correct number if not guessed within 3 attempts.  

## Prerequisites  

Before running the script, ensure you have the following:  

1. **Python 3.x** installed on your system.  

## Installation  

1. Clone this repository or download the script to your local machine.  
2. Create a new Python file named `number_guessing_game.py` and copy the game code into it:  

   ```python  
   import random  

   def number_guessing_game():  
       """Play a number guessing game."""  
       number_to_guess = random.randint(1, 100)  
       attempts = 3  
       print("Welcome to the Number Guessing Game!")  
       print("I have selected a number between 1 and 100.")  
       print(f"You have {attempts} attempts to guess it.")  

       for attempt in range(1, attempts + 1):  
           guess = input(f"Attempt {attempt}: Enter your guess: ")  

           # Validate input  
           if not guess.isdigit():  
               print("Please enter a valid number.")  
               continue  

           guess = int(guess)  

           if guess < number_to_guess:  
               print("Too low! Try again.")  
           elif guess > number_to_guess:  
               print("Too high! Try again.")  
           else:  
               print(f"Congratulations! You've guessed the number {number_to_guess} correctly!")  
               break  
       else:  
           print(f"Sorry! You've used all your attempts. The correct number was {number_to_guess}.")  

   if __name__ == "__main__":  
       number_guessing_game()
   python number_guessing_game.py
   Example Output
vbnet
Welcome to the Number Guessing Game!  
I have selected a number between 1 and 100.  
You have 3 attempts to guess it.  
Attempt 1: Enter your guess: 50  
Too low! Try again.  
Attempt 2: Enter your guess: 75  
Too high! Try again.  
Attempt 3: Enter your guess: 65  
Congratulations! You've guessed the number 65 correctly!  
If you do not guess the number within three attempts:

vbnet
Sorry! You've used all your attempts. The correct number was 42.  
Contributing
Feel free to fork this repository and submit your changes. Pull requests are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for details.

vbnet

### Instructions for Using the README  

1. Create a new file called `README.md` in the same directory as your `number_guessing_game.py` file.  
2. Copy and paste the above content into the `README.md` file.  
3. Modify any sections as necessary to fit your project's specifics.  

This README provides a clear overview of the number guessing game and instructions for users. If you need any adjustments or additional information, feel free to ask!
