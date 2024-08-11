import random
def rock_paper_scissor_game():
    print("\''''Welcome to Rock Paper Scissor Game\''''")
    options = ["rock","paper","scissor"]
    user_score = 0
    computer_score = 0
    while True:
        user_choice = input("Enter the choice (rock, paper, scissor) :\t").lower()
        
        if user_choice not in options:
            print(f"Invalid input. Please enter the choice {options}")
            continue
            
        computer_choice = random.choice(options)
        
        if user_choice == computer_choice:
            print(f"Your choice '{user_choice}' and Computer choice '{computer_choice}' is same")
            print(f"\t The game is Tied")
            
        elif user_choice == "rock" and computer_choice == "scissor":
            print(f"Your choice is '{user_choice}' and Computer choice is '{computer_choice}'")
            print(f"\t You Win! 'The Rock Smashed the Scissor'")
            user_score += 1
        
        elif user_choice == "scissor" and computer_choice == "paper":
            print(f"Your choice is '{user_choice}' and Computer choice is '{computer_choice}'")
            print(f"\t You Win! 'The Scissor cut the Paper'")
            user_score += 1

        elif user_choice == "paper" and computer_choice == "rock":
            print(f"The user choice '{user_choice}' and computer choice '{computer_choice}'")
            print(f"\t You Win! 'The Paper cover the Rock'")
            user_score += 1
            
        else:
            print(f"Your choice is '{user_choice}' and Computer choice is '{computer_choice}'")
            print(f"\t You Loss! 'Computer Win the game'")
            computer_score += 1
           
        next_round = input("Please enter Yes to play the next round and No to exit the game:\t").lower()

        if next_round == "no":
            print(f"\t Your Score is {user_score} and Computer score is {computer_score}")
            break
            
        elif next_round == "yes":
            continue

        else:
            print("Invalid input. Please enter 'yes' and 'no'")
            
rock_paper_scissor_game()