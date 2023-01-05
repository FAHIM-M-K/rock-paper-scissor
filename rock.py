import random

# List of choices for the computer
choices = ['rock', 'paper', 'scissors']

# Initialize the score
score = 0
while True:
  # Get the user's choice
  user_choice = input("Enter your choice (rock, paper, scissors): ")

  # Check if the user's choice is valid
  if user_choice not in choices:
    print("Invalid choice. Please try again.")
    continue

  # Get the computer's choice
  computer_choice = random.choice(choices)

  # Compare the choices and determine the winner
  if user_choice == computer_choice:
    print("It's a tie!")
  elif user_choice == 'rock' and computer_choice == 'scissors':
    print("You win! Rock beats scissors.")
    score += 1
  elif user_choice == 'paper' and computer_choice == 'rock':
    print("You win! Paper beats rock.")
    score += 1
  elif user_choice == 'scissors' and computer_choice == 'paper':
    print("You win! Scissors beats paper.")
    score += 1
  else:
    print("You lose. {} beats {}.".format(computer_choice, user_choice))
    
  # Check if the user wants to play again
  play_again = input("Do you want to play again? (y/n) ")
  if play_again == 'n':
    break

# Print the final score
print("Your final score is: {}".format(score))