from tkinter import *
from PIL import Image, ImageTk
from random import randint
def msg_updation(e):
    final_msg['text']=e

def comp_update():
    final=int(computer_score['text'])  
    final+=1
    computer_score['text']=str(final)

def player_update():
    final=int(player_score['text'])  
    final+=1
    player_score['text']=str(final)

def winner_check(player,comp):
    if(player==comp):
        msg_updation("It's a tie.")
    elif ((player=="ROCK" and comp=="PAPER") or (player=="SCISSOR" and comp=="ROCK") or (player=="PAPER" and comp=="SCISSOR")) :
        msg_updation("Computer Wins !!")
        comp_update()
    else:
        msg_updation("Player Wins !!") 
        player_update()

def choice_update(e):
    choice_computer=to_select[randint(0,2)]
    if choice_computer=="ROCK":
        lable_computer.configure(image=img_rock)
    elif choice_computer=="PAPER":
        lable_computer.configure(image=img_paper)  
    else:
        lable_computer.configure(image=img_scissor)    

    #user
    if e=="ROCK":
        lable_player.configure(image=img_rock)
    elif e=="PAPER":
        lable_player.configure(image=img_paper)
    else:
        lable_player.configure(image=img_scissor) 

    winner_check(e,choice_computer)       

window=Tk()
window.title("Game Rock, Paper and Scissor")
window.config(bg="black")
window.minsize(width=1100,height=600)

#images 
img_rock=ImageTk.PhotoImage(Image.open("rock.png"))
img_paper=ImageTk.PhotoImage(Image.open("paper1.png"))
img_scissor=ImageTk.PhotoImage(Image.open("scissor.png"))

lable_player=Label(window,image=img_rock,width=160,height=160,border=2,borderwidth=2,relief="solid")
lable_computer=Label(window,image=img_rock,width=160,height=160,border=2,borderwidth=2,relief="solid")

lable_computer.grid(row=0,column=5,padx=10,pady=30)
lable_player.grid(row=0,column=0,padx=10,pady=30)

computer_score=Label(window,text=0,font=("Arial",60,"bold"),fg="red")
player_score=Label(window,text=0,font=("Arial",60,"bold"),fg="red")

player_score.grid(row=0,column=1,padx=10,pady=10)
computer_score.grid(row=0,column=4,padx=10,pady=10)

player_indicator=Label(window,font=("Arial",30,"bold"),text="PLAYER",bg="orange",fg="blue")
computer_indicator=Label(window,font=("Arial",30,"bold"),text="COMPUTER",bg="orange",fg="blue")

player_indicator.grid(row=1,column=0,padx=10,pady=20)
computer_indicator.grid(row=1,column=5,padx=10,pady=20)

to_select=["ROCK","PAPER","SCISSOR"]

final_msg=Label(window,font=("Arial",30,"bold"),bg="red",fg="white")
final_msg.grid(row=3,column=2,padx=10,pady=10)

button_rock=Button(window,width=16,height=3,text="ROCK",font=("Arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("ROCK"))
button_rock.grid(row=2,column=0,padx=10,pady=10)
button_paper=Button(window,width=16,height=3,text="PAPER",font=("Arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("PAPER"))
button_paper.grid(row=2,column=2,padx=10,pady=10)
button_scissor=Button(window,width=16,height=3,text="SCISSOR",font=("Arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("SCISSOR"))
button_scissor.grid(row=2,column=5,padx=10,pady=10)


window.mainloop()