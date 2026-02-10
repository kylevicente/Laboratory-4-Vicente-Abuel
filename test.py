import os

# ---------- Utility ----------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def normalize(text):
    return text.lower()


# ---------- Graphics ----------
BEGINNER = [
"""







=========""",
"""
      |
      |
      |
      |
      |
=========""",
"""
  +---+
      |
      |
      |
      |
      |
=========""",
"""
  +---+
  O   |
      |
      |
      |
      |
=========""",
"""
  +---+
  O   |
  |   |
      |
      |
      |
=========""",
"""
  +---+
  O   |
 /|   |
      |
      |
      |
=========""",
"""
  +---+
  O   |
 /|\\  |
      |
      |
      |
=========""",
"""
  +---+
  O   |
 /|\\  |
 /    |
      |
      |
=========""",
"""
  +---+
  O   |
 /|\\  |
 / \\  |
      |
      |
========="""
]

MODERATE = BEGINNER[2:]       # shorter progression
ADVANCED = BEGINNER[4:]       # even shorter


def get_graphics(level):
    if level == 1:
        return BEGINNER, 7
    elif level == 2:
        return MODERATE, 5
    else:
        return ADVANCED, 3


# ---------- Hangman Round ----------
def play_round(secret, graphics, max_wrong):
    secret = normalize(secret)
    guessed = set()
    wrong = 0

    while True:
        clear_screen()

        # Display graphics
        print(graphics[min(wrong, len(graphics)-1)])

        # Show word progress
        display = ""
        completed = True
        for ch in secret:
            if ch == " ":
                display += "  "
            elif ch in guessed:
                display += ch + " "
            else:
                display += "_ "
                completed = False
        print("\nWord:", display)
        print("Wrong guesses:", wrong, "/", max_wrong)
        print("Guessed letters:", " ".join(sorted(guessed)))

        # Win check
        if completed:
            print("\n🎉 Correct! Word was:", secret)
            return True

        # Lose check
        if wrong >= max_wrong:
            print("\n💀 Game Over! Word was:", secret)
            return False

        # Guess input
        guess = input("Enter letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input!")
            input("Press Enter...")
            continue

        if guess in guessed:
            continue

        guessed.add(guess)

        if guess not in secret:
            wrong += 1


# ---------- Main Game ----------
def choose_difficulty():
    while True:
        print("Choose difficulty:")
        print("1. Beginner")
        print("2. Moderate")
        print("3. Advanced")
        choice = input("Select: ")
        if choice in ("1", "2", "3"):
            return int(choice)


def choose_series():
    while True:
        choice = input("Best of (3/5/7): ")
        if choice in ("3", "5", "7"):
            return int(choice)


def main():
    clear_screen()
    print("=== Modified Hangman ===")

    level = choose_difficulty()
    graphics, max_wrong = get_graphics(level)
    total_games = choose_series()
    wins_needed = total_games // 2 + 1

    score = [0, 0]
    round_num = 1

    while score[0] < wins_needed and score[1] < wins_needed:
        clear_screen()
        print(f"\n--- Round {round_num} ---")
        print("Score P1:", score[0], " P2:", score[1])

        # Player 1 sets word
        secret = input("\nPlayer 1 enter word/phrase: ")
        clear_screen()

        print("Player 2 guessing...")
        win = play_round(secret, graphics, max_wrong)
        if win:
            score[1] += 1
        else:
            score[0] += 1

        # Swap roles
        secret = input("\nPlayer 2 enter word/phrase: ")
        clear_screen()

        print("Player 1 guessing...")
        win = play_round(secret, graphics, max_wrong)
        if win:
            score[0] += 1
        else:
            score[1] += 1

        round_num += 1

        # Continue option
        cont = input("\nContinue playing? (y/n): ").lower()
        if cont != "y":
            break

    clear_screen()
    print("=== Final Score ===")
    print("Player 1:", score[0])
    print("Player 2:", score[1])

    if score[0] > score[1]:
        print("🏆 Player 1 Wins!")
    elif score[1] > score[0]:
        print("🏆 Player 2 Wins!")
    else:
        print("It's a tie!")


# Run game
if __name__ == "__main__":
    main()
