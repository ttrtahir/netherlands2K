import random
import time
import os 

question_file = open('netherlandsV.txt', 'r')
questions = question_file.read().splitlines()
answer_file = open('englishV.txt')
answers = answer_file.read().splitlines()

def display(delay, afterClear):
    counter = 0
    while(1):
        counter=counter+1
        i = random.randint(0,1635)
        print(f"{counter:4}  {questions[i]:20}  ---------->  {answers[i]:20}")
        time.sleep(delay)
        if afterClear == True:
            os.system("clear")

def welcome():
    afterClear = False

    os.system("clear")

    print("""
            Welcome to Netherlands Language Teacher
                    Press ENTER to Continue    
    """)
    temp = input()
    os.system("clear")

    print("""
            Do you want to clear screen
                    after a match

                1-) Yes, clear them all
                2-) No, leave them
    """)
    afterClearOptions = input()
    if afterClearOptions == '1':
        afterClear = True
    os.system("clear")

    print("""
            Select a mode:

                1-) Rapid
                2-) Normal
                3-) Slow
    """)
    mode = int(input())
    os.system("clear")
    if mode == 1: 
        delay = 1
    if mode == 2: 
        delay = 3
    if mode == 3: 
        delay = 5
    display(delay, afterClear)

def main():
    welcome()
    
    
if __name__ == "__main__":
    main()
