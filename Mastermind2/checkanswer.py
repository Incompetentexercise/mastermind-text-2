from colorama import Fore, Back, Style

#function to mark answers
def checkanswer(guesses,answers,marks,allcorrect):
    marked=False #if the entry is marked not incorrect
    for i in range(0,4): #loop for all entries
        if guesses[i]==answers[i]: #if the guess matches the answer in that place
            marks[i]=Back.LIGHTGREEN_EX+Fore.BLACK+str(guesses[i])+Back.RESET+Fore.RESET
        else:
            for o in range(0,4): #check against other answer places
                if marked==False:
                    if guesses[i]==answers[o]:
                        marks[i]=Back.LIGHTYELLOW_EX+Fore.BLACK+str(guesses[i])+Back.RESET+Fore.RESET
                        marked=True
                    else:
                        marks[i]=Back.LIGHTRED_EX+Fore.BLACK+str(guesses[i])+Back.RESET+Fore.RESET
            marked=False