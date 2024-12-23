import random 

a="🪨"
b="✊"
c="✂️"
w=True
while w==True:
    
    print("Enter".center(20,"="))
    print("Rock.".ljust(16,".")+"🪨"+"  1")
    print("Pepper.".ljust(16,".")+"✊"+" 2")
    print("Scissor.".ljust(16,".")+"✂️"+"  3")
    playerchoice = int(input("Enter====>>>   "))

    computerchoice=random.choice("123")
    computers=int(computerchoice)

    if playerchoice<4 and playerchoice>0:

            if playerchoice==1 and computers==3:
                print("=============================\n",f"you win 🥇🎁 {a}"+"  "+f"{c}"+"\n=============================\n")
                break
            elif playerchoice==2 and computers==1:
                print("=============================\n",f"you win 🥇🎁 {b}"+"  "+f"{a}"+"\n=============================\n")
                break
            elif playerchoice==3 and computers==2:
                print("=============================\n",f"you win 🥇🎁 {c}"+"  "+f"{b}"+"\n=============================\n")
                break
            elif playerchoice == computers:
                print("=============================\n",f"Draw.........😉;{playerchoice}=={computers}\n=============================\n")
                w=True
            else :
                print("=============================\n",f"Sorry.........😑;{playerchoice}<{computers}\n=============================\n")   
                break
    else:
        print("Ivalid value")