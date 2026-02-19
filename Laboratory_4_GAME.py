import os 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def normalize(text):
    return text.lower()

##INTRO HEADER AND RULES SECTION
while True:
    print("---------------------------")
    print("Modified Hangman Game")
    print("=========================================================================================")
    print("Rules:\n")
    print("This is a two player game. Player one will input the name of any movie, artist, song title, or game")
    print("Player two on the other hand will try to guess whatever player one inputed one letter at a time.")
    print("The difficulty will decide how many mistakes the guessing player can make before they lose")
    print("You will then be asked how many points one player needs in order to win the game.")
    print("Have fun!")
    print("===========================================================================================")

    p1 = input("Enter Player 1 Name: ")
    p2 = input("Enter Player 2 Name: ")
    
    ##DIFFICULTY SELECTION
    def difficulty():
        while true:
            print ("Choose your difficulty")
            print("A. Beginner ")
            print("B. Moderate ")
            print("C. Advance ")
            option = input("Selection Option: ").upper()
            print("---------------------------")
            if choice in ("A", "B","C",):
                return choice
            
    ##BEST OF HOW MANY SELECTION
    print("Choose how many points it will take to win")
    print("A. Best of 3 (first to three points win)")
    print("B. Best of 5 (first to five points win)")
    print("C. Best of seven (first to seven points will win)")
    while true
        bestof = input("Selction Option: ")
        if bestof == "1":
            wins_needed = 2
            break
        elif bestof == "2":
            wins_needed = 3
            break
        elif bestof == "3":
            wins_needed = 4
            break
        else: 
            print("Invalid Choice. Try again.")
    
## DIFFICULTY SELECTION
    level = difficulty()

    if level == "A":
        max_wrong = 6
    elif level == "B":
        max_wrong = 4
    else:
        max_wrong = 2

## GRAPHICS (used list)
    
    hangman = [
"""
 +---+
     |
     |
     |
     |
     |
=========
""",
"""
 +---+
 O   |
     |
     |
     |
     |
=========
""",
"""
 +---+
 O   |
 |   |
     |
     |
     |
=========
""",
"""
 +---+
 O   |
/|   |
     |
     |
     |
=========
""",
"""
 +---+
 O   |
/|\\  |
     |
     |
     |
=========
""",
"""
 +---+
 O   |
/|\\  |
/     |
     |
     |
=========
""",
"""
 +---+
 O   |
/|\\  |
/ \\  |
     |
     |
=========
"""
]

## main
p1_score = 0
p2_score = 0

while p1_score < wins_needed and p2_score < wins_needed:

    ## player 1
    secret = normalize(input(f"\n{p1}, enter an artist/movie name: "))
    clear_screen()

    wrongGraphics = 0
    guessed = ""

    while True:

        print("================================")
        print(f"Current Player: {p2}")
        print(f"Score = {p1}: {p1_score} | {p2}: {p2_score}")
        print("=================================")

        print(hangman[wrongGraphics])

        ## ADD UNDERSCORE GRAPHICS

        print(f"Wrong guesses: {wrong} / {max_wrong}")
        print(f"Guessed: {guessed}")

        guess = normalize(input("Enter letter or number: "))

        guessed += guess
        
        if guess not in secret:
            wrong += 1

        
    


    
