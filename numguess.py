import random  
correct_number = random.randint(1, 10)  
choice = 3  
print("Guess the number between 1 and 10. You have 3 attempts.")  
for choice in range(choice):  
    user_guess = int(input(f"Attempt {choice + 1}: guess the number: "))  

    if user_guess == correct_number:  
        print("your number is correct")  
        break   
else:  
     
    print(f"you have loose the game The correct number was {correct_number}")