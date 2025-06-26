import random

def game():
    choices = ['snake', 'water', 'gun']
    user_score = 0
    comp_score = 0
    draw_score = 0

    while True:
        move = input("Enter your choice (snake/water/gun): ").lower()
        if move not in choices:
            print("Invalid choice. Please try again.")
            continue

        comp_move = random.choice(choices)
        print(f"You chose {move} ; My move is {comp_move}")

        if move == comp_move:
            print("It's a draw")
            draw_score += 1
        elif (move == 'snake' and comp_move == 'water') or \
             (move == 'water' and comp_move == 'gun') or \
             (move == 'gun' and comp_move == 'snake'):
            print("You win")
            user_score += 1
        else:
            print("I win")
            comp_score += 1

        print(f"\nScoreboard:")
        print(f"You: {user_score} | Me: {comp_score} | Draws: {draw_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
game()
