import random 

print("=== ROCK PAPER SCISSORS ===")
print("1 for rock \n2 for paper \n3 for scissor")
print("First to win 5 rounds wins the game!\n")

def rock_paper_scissor():
    i = 0  # CPU score
    j = 0  # Player score
    
    while i < 5 and j < 5:
        a = random.randint(1, 3)
        try:
            b = int(input("\nEnter your choice (1-3): "))
            if b not in [1, 2, 3]:
                print("Invalid choice! Please enter 1, 2, or 3")
                continue
        except ValueError:
            print("Invalid input! Please enter a number")
            continue
        
        # Show choices
        choices = {1: "Rock", 2: "Paper", 3: "Scissor"}
        print(f"You chose: {choices[b]}")
        print(f"CPU chose: {choices[a]}")
        
        if a == b:
            print("It's a tie!")
        elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
            j += 1
            print(f"You win this round! Score: You {j} - {i} CPU")
        else:
            i += 1
            print(f"CPU wins this round! Score: You {j} - {i} CPU")
    
    print("\n" + "="*40)
    if j > i:
        print(f"🎉 YOU WIN THE GAME! Final Score: {j}-{i}")
    else:
        print(f"💻 CPU WINS THE GAME! Final Score: {i}-{j}")
    print("="*40)

if __name__ == "__main__":
    rock_paper_scissor()