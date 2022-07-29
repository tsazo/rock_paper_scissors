import random

def play():
  user_count = 0
  comp_count = 0

  while (user_count < 2 and comp_count < 2):
    user = input("Type 'r' for rock, 'p' for paper, and 's' for scissors: ").lower()
    comp =random.choice(['rock', 'paper', 'scissors'])

    if user not in ['r', 'p', 's']:
      print("Please enter a valid input: r, p, or s.")
      continue

    user = 'rock' if user == 'r' else 'paper' if user == 'p' else 'scissors'

    if user == comp:
      print(f"You picked {user}, computer picked {comp}. You tied this round!")
      continue

    if is_win(user, comp):
      print(f"You picked {user}, computer picked {comp}. You win this round!")
      user_count += 1
    else:
      print(f"You picked {user}, computer picked {comp}. You lose this round.")
      comp_count += 1
  
  if user_count == 2:
    print("Congratulations! You won!")
  else:
    print("Sorry, you lose. Try again next time!")

def is_win(player, opponent):
    return (player == 'rock' and opponent == 'scissors') or \
        (player == 'paper' and opponent == 'rock') or \
        (player == 'scissors' and opponent == 'paper')

def main():
  print("Welcome to rock paper scissors! Best 2 out of 3.")
  play()


if __name__ == "__main__":
  main()