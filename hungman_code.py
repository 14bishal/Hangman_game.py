## Hangman game


import random

stage_1 = ['''
  +----+
  |    |
       |
   0   |
  /|\  |
  / \  |
       |
''']

stage = ['''
  +----+
  |    |
  0    |
 /|\   |
 / \   |
       |
''', '''
  +----+
  |    |
  0    |
 /|\   |
 /     | 
       |

''', '''

   +----+
  |    |
  0    |
 /|\   |
       | 
       |

''', '''
+----+
  |    |
  0    |
 /|    |
       | 
       |

''', '''

+----+
  |    |
  0    |
  |    |
       | 
       |

''', '''

+----+
  |    |
  0    |
       |
       | 
       |

''', '''

+----+
  |    |
       |
       |
       | 
       |

''']

print(" !!!! WELCOME TO THE HANGMAN GAME !!!!")
menu = int(input("Which Topic you want to choose? \nType 1 for Python_Keyword. \nType 2 for Science. \n"))

keyword_list = ["False", "await", "else", "import", "pass","None", "break", "except", "in", "raise", "True", "class",
            	"finally", "is", "return", "and", "continue",	"for", "lambda", "try", "as", "def", "from", "nonlocal", "if",
                "while", 'assert', "del",	"global",	"not", "with", "async", "elif", "or", "yield"]

science_keyword = ["atom", "biology", "cell", "chemical", "chemistry", "magnetism", "mass"]

if menu == 1:
    chosen_keyword = random.choice(keyword_list)
elif menu == 2:
    chosen_keyword = random.choice(science_keyword)
    
    
#chosen_keyword = random.choice(keyword_list)   ## Computer choose randomly keyword from the input
#print(f"Chosen keyword is: {chosen_keyword}")

lives = 6                                        ## number of stages to hang the person

display = []                                     ## an empty list to show the output
for _ in range (len(chosen_keyword)):            # Here, I fill the number of letter by "_" so that it will look appropiate
    display += "_"                               ## Adding the "_" till the length of keyword chosen
print(display)

end = False                                      # i initalize it so that until the game didn't finished the while loop will iterate continue...
while not end:
    guess = input("Gues a letter: ").lower()     ## Irrespective to the input, diractly converted the input in lowercase

    for position in range(len(chosen_keyword)):  # from the chosen keyword , it will iterate each letter of the keyword and
        letter = chosen_keyword[position]        # stored int the variable name calledd "letter" 
        if letter == guess:                      # then, it will compared with the each letter with the guess letter
            display[position] = letter           # if its true, it will display the letter
    
    if guess not in chosen_keyword:              # If the guess is not correct then, lives or chance will reduces
        lives -= 1
        if lives == 0:                           # If the lives=0, then you will loose the game
            end = True                           ## here, end is true means it will come out of while loop
            print("You lose")

    print(display)
    print(stage[lives])

    if "_" not in display:                 # It will track wheather there is any "_" or not
        end = True                         # if not, comes out of the while loop and you won the game. 
        print("Won")
        print("You are save now ")
        print(stage_1[0])
