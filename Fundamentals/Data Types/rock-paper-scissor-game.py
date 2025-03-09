import random

def win_message():
    return "You win!!!"

def rock_paper_scissor():

    print("Welcome to Rock Paper Scissor Game")
    
    computer_choice = random.choice(["rock", "paper", "scissor"])
    user_choice = input("Enter your choice (rock, paper, scissor): ")
    
    if user_choice not in ["rock", "paper", "scissor"]:
        print("Invalid choice. Please enter a valid choice")
        rock_paper_scissor()

    print(f"Computer's choice: {computer_choice}")  

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissor":
        win_message()
    elif user_choice == "paper" and computer_choice == "rock":
        win_message()
    elif user_choice == "scissor" and computer_choice == "paper":
        win_message()
    else:
        print("Computer wins!")

    repeat = input("Do you want to play again? (yes/no): ")

    if repeat == "yes":
        rock_paper_scissor()
    else:
        print("Thanks for playing!")    

       

rock_paper_scissor()