import random
import os

def main():
    DATABASE = [
        "ANDRES",
        "FELIPE",
        "BARRERO",
        "ARCE"
    ]
    HANGMAN_IM = [ """ 
 ____
|/   |
|   (_)
|   /|\
|    |
|   | |
|
|_____    
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|   / \
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|   / 
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|
|    |
|    
|
|_____

""",
"""
 ____
|/   |
|   (_)
|    |
|    |    
|    
|
|_____

""",
"""
 ____
|/   |
|   (_)
|    
|    
|    
|
|_____

""",
"""
____
|/   |
|   
|    
|    
|    
|
|_____
"""]

    word = random.choice(DATABASE)
    spaces = ["_"] * len(word)
    attemps = 7

    while True:
        os.system("cls")
        for i in spaces:
            print(i, end=" ")
        print(HANGMAN_IM[attemps])
        menu = input("Choose a character: ").upper()

        found = False
        for idx, character in enumerate(word):
            if character == menu:
                spaces[idx] = menu
                found = True

        if not found:
                attemps -= 1

        if "_" not in spaces:
                os.system("cls")
                print("You win!!")
                break
                input()
        
        if attemps == 0:
                os.system("cls")
                print("You lose!! GAME OVER")
                break
                input()


if __name__ == '__main__':
    main()