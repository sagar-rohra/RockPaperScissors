import random

def get_choices():
  player_choice = input("Enter a choice- Rock, paper, Scissors: ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player" : player_choice, "computer" : computer_choice}
  return choices

def check_win(player, computer):
  print (f"You chose {player} , computer chose {computer} ")
  if player == computer:
    return "It's a tie"
  elif player == "rock":
    if computer == "scissors":
      return "rock smahdes scissors! You win! "
    else:
      return "Paper covers rock. You lose"
  elif player == "paper":
    if computer == "scissors":
      return "scissors cuts paper! You win! "
    else:
      return "paper covers rock. You lose"
  elif player == "scissors":
    if computer == "rock":
      return "rock smahdes scissors! You win! "
    else:
      return "rock smaches scissors! You lose! "    

choices = get_choices();
result = check_win(choices["player"], choices["computer"])
print(result)