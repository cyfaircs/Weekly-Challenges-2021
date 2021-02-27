from time import sleep

score = 0

HEADER_COLOR = "\033[1;32m"
QUESTION_COLOR = "\033[1;36m"
ANSWERS_COLOR = "\033[0;36m"
CORRECT_COLOR = "\033[1;32m"
WRONG_COLOR = "\033[1;31m"

NORMAL = "\033[0m"

def ask_question(question, a, b, c, d, correct_answer):
    print(QUESTION_COLOR + question)
    print(ANSWERS_COLOR, end="")
    sleep(1)
    print(f"a - {a}")
    sleep(1)
    print(f"b - {b}")
    sleep(1)
    print(f"c - {c}")
    sleep(1)
    print(f"d - {d}")

    answer = get_answer()

    if answer.lower() == correct_answer:
        print(CORRECT_COLOR + "CORRECT!!!")
        return 1
    else:
        print(WRONG_COLOR + "Yikes.")
        return 0

def get_answer():
    letter = input("Enter the correct letter: ")
    if letter.lower() in ["a", "b", "c", "d"]:
        return letter
    else:
        print("You must enter one of the 4 letters displayed.")
        return get_answer()

print(HEADER_COLOR + 
r"""
 ___       __   _______   ___       ________  ________  _____ ______   _______      
|\  \     |\  \|\  ___ \ |\  \     |\   ____\|\   __  \|\   _ \  _   \|\  ___ \     
\ \  \    \ \  \ \   __/|\ \  \    \ \  \___|\ \  \|\  \ \  \\\__\ \  \ \   __/|    
 \ \  \  __\ \  \ \  \_|/_\ \  \    \ \  \    \ \  \\\  \ \  \\|__| \  \ \  \_|/__  
  \ \  \|\__\_\  \ \  \_|\ \ \  \____\ \  \____\ \  \\\  \ \  \    \ \  \ \  \_|\ \ 
   \ \____________\ \_______\ \_______\ \_______\ \_______\ \__\    \ \__\ \_______\
    \|____________|\|_______|\|_______|\|_______|\|_______|\|__|     \|__|\|_______|
                                                                                    
                                                                                    
                                                                                    
 _________  ________                                                                
|\___   ___\\   __  \                                                               
\|___ \  \_\ \  \|\  \                                                              
     \ \  \ \ \  \\\  \                                                             
      \ \  \ \ \  \\\  \                                                            
       \ \__\ \ \_______\                                                           
        \|__|  \|_______|                                                           
                                                                                    
                                                                                    
                                                                                    
 _________  ________  ___  ___      ___ ___  ________                               
|\___   ___\\   __  \|\  \|\  \    /  /|\  \|\   __  \                              
\|___ \  \_\ \  \|\  \ \  \ \  \  /  / | \  \ \  \|\  \                             
     \ \  \ \ \   _  _\ \  \ \  \/  / / \ \  \ \   __  \                            
      \ \  \ \ \  \\  \\ \  \ \    / /   \ \  \ \  \ \  \                           
       \ \__\ \ \__\\ _\\ \__\ \__/ /     \ \__\ \__\ \__\                          
        \|__|  \|__|\|__|\|__|\|__|/       \|__|\|__|\|__|
""" + NORMAL)

score += ask_question("Who is the current president of the CS club?",
    "Trevor Hatcher",
    "Hagar Kangah",
    "Chasey Lamport",
    "Amr Ojjeh",
    "a")

score += ask_question("Who's you're absolute favorite VP?",
    "Michael C",
    "Gabriel Williams",
    "Luis. Just Luis.",
    "Amr Ojjeh",
    "d")

score += ask_question("Which programming language is this using?",
    "C++",
    "Python",
    "Java",
    "Windows",
    "b")

print(NORMAL + "With all the questions answered, your score is: " + str(score))
