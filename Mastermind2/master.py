from random import randint
from colorama import Fore, Back, Style
import time
from drawscreen import drawscreen,cls
from checkanswer import checkanswer


def master(chances):
     #text to display when program loads
    messages=[] #optional messages for the start of screendraw
    
    guesses=["-","-","-","-"] #what player enters
    answers=[0,0,0,0] #correct answers
    marks=["","","",""] #visual marking
    logs=[] #what the player guessed on last turn
    
    turns=chances #total turns
    turncntr=0 #turns player has taken
    allcorrect=False
    
    
    #assign answers randomly
    for i in range(0,4):
        answers[i]=randint(1,9)
    for answer in answers:
        print(answer)
    
    cls()
    print("The computer has picked a Four digit number with digits between 1 and 9, \nIt's your job to guess it, you get",chances,"chances. \nThe computer will give you the following hints each time you make a guess: \n"+Back.LIGHTGREEN_EX+"  "+Back.RESET+"--> Correct \n"+Back.LIGHTYELLOW_EX+"  "+Back.RESET+"--> Right number, wrong place \n"+Back.LIGHTRED_EX+"  "+Back.RESET+"--> Incorrect\nBegin Guessing!")
    print("\nPress Enter to start...")
    str(input("")) #holds program until enter pressed
    
    #first guess
    drawscreen(chances,guesses,logs,marks,messages,turns,turncntr ) #refresh screen
    while True:
        try:
            intguess=int(input("Current       : ")) 
            if intguess>=1111 and intguess<=9999: #ensures input is four digits
                drawscreen(chances,guesses,logs,marks,messages,turns,turncntr )
                break
            else:
                drawscreen(chances,guesses,logs,marks,messages,turns,turncntr )
                print("invalid input")
                pass #loop back
        except ValueError:
            drawscreen(chances,guesses,logs,marks,messages,turns,turncntr )
            print("Invalid input")

    guesses=[int(guesses) for guesses in str(intguess)] #turns int into list of spaces, dont know how it works
    checkanswer(guesses,answers,marks,allcorrect)


    logs.append(intguess) #add int of last guess to logs
    turncntr=turncntr+1
    
    
    
    #loop for normal guesses
    while turncntr<turns and guesses!=answers: #will loop while there are turns remaining and guesses are incorrect
        intguess=0
        guesses=["-","-","-","-"] #clears guesses
        drawscreen(chances,guesses,logs,marks,messages,turns,turncntr )
        while True:
            try:
                intguess=int(input("Current       : "))
                if intguess>=1111 and intguess<=9999: #ensures input is four digits
                    drawscreen(chances,guesses,logs,marks,messages,turns,turncntr )
                    break
                else:
                    drawscreen(chances,guesses,logs,marks,messages,turns,turncntr )
                    print("invalid input")
                    pass #loop back
            except ValueError:
                drawscreen(chances,guesses,logs,marks,messages,turns,turncntr )
                print("Invalid input")

        guesses=[int(guesses) for guesses in str(intguess)]
        checkanswer(guesses,answers,marks,allcorrect)
        logs.append(intguess) #add int of last guess to logs
        
        turncntr=turncntr+1

    #endstates
    if guesses==answers:
        for i in range(4):
            messages=[Back.LIGHTGREEN_EX+Fore.BLACK+"Congratulations, you won!"+Fore.RESET+Back.RESET]
            drawscreen(chances,guesses,logs,marks,messages,turns,turncntr )
            time.sleep(0.4)

            messages=[Fore.LIGHTGREEN_EX+"Congratulations, you won!"+Fore.RESET]
            drawscreen(chances,guesses,logs,marks,messages,turns,turncntr )
            time.sleep(0.4)
        input("Press Enter to exit...")
    elif turncntr==turns:
        drawscreen(chances,guesses,logs,marks,messages,turns,turncntr )
        print(Fore.LIGHTRED_EX+"Game over: out of turns\n"+Fore.RESET+"Correct answer was:",end="")
        for answer in answers:
            print(answer,end="")
        print("")
        input("Press Enter to exit...") #holds until player is ready
    

master(7)