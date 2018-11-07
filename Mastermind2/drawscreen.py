import os

#makes a clear screen function that works on any system
def cls():
    os.system('cls' if os.name=='nt' else 'clear') 

#draw game screen function
def drawscreen(chances,guesses,logs,marks,messages,turns,turncntr ):
    cls()
    for message in messages: #print all messages
        print(message)
        print("")
    

    print("Guesses Remaining: ",end="")#make bar
    print("[",end="")
    for i in range(turns-turncntr):
        print("#",end="")
    for i in range(turncntr):
        print("-",end="")
    print("]")

    print("")

    print("Logged Guesses:")
    for log in logs:
        print("                ",end="")
        print(log," ")

    print("Computer Mark : "+marks[0]+marks[1]+marks[2]+marks[3])