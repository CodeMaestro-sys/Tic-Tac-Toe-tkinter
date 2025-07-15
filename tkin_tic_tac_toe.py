from tkinter import *
root=Tk()
root.title("Tic Tac Toe")
Current_player=["X"]
buttons=[[None for i in range(3)] for j in range(3)]
def func(button):
    if(button["text"]==""):
        button["text"]=Current_player[0]
        if(Current_player[0]=="X"):
            Current_player[0]="O"
        else:
            Current_player[0]="X"
        if(buttons[0][0]["text"]==buttons[1][1]["text"]==buttons[2][2]["text"]!=""):
            print(buttons[0][0]["text"],"won")
            button.config(state="disabled")
        elif(buttons[0][2]["text"]==buttons[1][1]["text"]==buttons[2][0]["text"]!=""):
            print(buttons[0][2]["text"],"won")
            button.config(state="disabled")
        for i in range(3):
            if(buttons[i][0]["text"]==buttons[i][1]["text"]==buttons[i][2]["text"]!=""):
                print(buttons[i][0]["text"],"won")
                button.config(state="disabled")
        for j in range(3):
            if(buttons[0][j]["text"]==buttons[1][j]["text"]==buttons[2][j]["text"]!=""):
                print(buttons[0][j]["text"],"won")
                button.config(state="disabled")
        all_filled=True
        for i in buttons:
            for k in i:
                if(k["text"]==""):
                    all_filled=False
        if all_filled:
                    print("draw")
def play_again():
     for row in buttons:
          for btn in row:
            btn.config(text="",state="active")
     Current_player[0]="X"
for i in range(3):
    for j in range(3):
        button=Button(root,text="",height=2,width=3,font="Arial 20")
        button.config(command=lambda b=button:func(b))
        button.grid(row=i,column=j)
        buttons[i][j]=button
B=Button(root,text="Click if you want to play again",font="Arial 10",command=play_again)
B.grid(row=3,column=0,columnspan=3)

root.mainloop()