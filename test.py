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

MODERATE = BEGINNER[2:]
ADVANCED = BEGINNER[4:]


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

        print(graphics[min(wrong, len(graphics)-1)])

        # Display progress
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
        print("Guessed:", " ".join(sorted(guessed)))

        if completed:
            print("\n🎉 Correct! Word was:", secret)
            return True

        if wrong >= max_wrong:
            print("\n💀 Game Over! Word was:", secret)
            return False

        guess = input("Enter letter or number: ").lower()

        # ✅ Allow letters AND digits
        if len(guess) != 1 or not guess.isalnum():
            print("Invalid input! Enter one letter or number.")
            input("Press Enter...")
            continue

        if guess in guessed:
            continue

        guessed.add(guess)

        if guess not in secret:
            wrong += 1


# ---------- Main ----------
def choose_difficulty():
    while True:
        print("1. Beginner\n2. Moderate\n3. Advanced")
        choice = input("Choose difficulty: ")
        if choice in ("1", "2", "3"):
            return int(choice)


def choose_series():
    while True:
        choice = input("Best of (3/5/7): ")
        if choice in ("3", "5", "7"):
            return int(choice)


def main():
    clear_screen()
    level = choose_difficulty()
    graphics, max_wrong = get_graphics(level)
    total_games = choose_series()
    wins_needed = total_games // 2 + 1

    score = [0, 0]
    round_num = 1

    while score[0] < wins_needed and score[1] < wins_needed:
        clear_screen()
        print(f"Round {round_num}")
        print("Score P1:", score[0], " P2:", score[1])

        secret = input("\nPlayer 1 word/phrase: ")
        clear_screen()
        if play_round(secret, graphics, max_wrong):
            score[1] += 1
        else:
            score[0] += 1

        secret = input("\nPlayer 2 word/phrase: ")
        clear_screen()
        if play_round(secret, graphics, max_wrong):
            score[0] += 1
        else:
            score[1] += 1

        round_num += 1

        if input("\nContinue? (y/n): ").lower() != "y":
            break

    clear_screen()
    print("Final Score:", score)
    print("Winner:",
          "Player 1" if score[0] > score[1]
          else "Player 2" if score[1] > score[0]
          else "Tie")


if __name__ == "__main__":
    main()
