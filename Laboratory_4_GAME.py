

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
    
    ##DIFFICULTY SELECTION
    print ("Choose your difficulty")
    print("A. Beginner ")
    print("B. Moderate ")
    print("C. Advance ")
    option = input("Selection Option: ").upper()
    print("---------------------------")
    
    ##BEST OF HOW MANY SELECTION
    print("Choose how many points it will take to win")
    print("A. Best of 3 (first to three points win)")
    print("B. Best of 5 (first to five points win)")
    print("C. Best of seven (first to seven points will win)")
    bestof = input("Selction Option: ")
    
    
    lives = 1

    if option == "A":
        lives = 7
    elif option == "B":
        lives = 5
    elif option == "C":
        lives = 3
    else option != "A, B, C"
        print("Invalid input")
    
     p1score = 0
     p2score = 0 
     games = 0 
     make     kjxdkjchjxkv
    
    


    
