import tkinter as tk
from math import pow
import re
window=tk.Tk()
window.title("CODSOFT CALCULATOR")
window.geometry("700x644")
window.minsize(height=650,width=600)
# window.iconbitmap("calc.ico")
window.config(bg="lightgreen")
val=tk.StringVar()
val.set("")
def submit(e):
    global val
    txt=e.widget.cget("text")
    print(txt)
    expr=""
    if txt=="=":
        if val.get().isdigit():
            ans=(val.get())
        else:
            try:
                expr=val.get()
                expr=re.sub("X","*",expr)
                if(expr.__contains__("%")):
                     expr=re.sub("%","/100*",expr)
                if(expr.__contains__("^")):
                     print("yes")    
                     expr=re.sub("^","**",expr)
                ans=str((eval(expr)))
            except Exception as er:
                print(er)   
                ans="Erorr!"
        if(ans[-1]=="0" and ans[-2]=="."):
                    ans=ans[:-2]          
        val.set(ans)    
        text_bar.update()   
    elif txt=="C":
        val.set("")   
        text_bar.update()
    else:
        # if txt=="X":
        #     txt="*"
        # elif txt=="^":
        #     txt="**"  
        # elif txt=="%":
        #      txt="/100*"
        val.set(val.get()+txt)    
        text_bar.update()

head=tk.Label(window,text="CODSOFT CALCULATOR",width=1200,bg="black",fg="white",font=("Arial",25,"bold"))
head.pack()
main_frame=tk.Frame(window,bg="lightgreen")
main_frame.pack()

calc_frame=tk.LabelFrame(main_frame,height=550,width=450,border=2,borderwidth=2,relief="solid")
# calc_frame.pack(padx=10,pady=40)
calc_frame.grid(row=0,column=0,padx=10,pady=40)

text_bar=tk.Entry(calc_frame,textvariable=val,bg="lightgrey",width=30,border=1,borderwidth=1,relief="solid",font=("Arial",20))
text_bar.grid(row=0,column=0,pady=10,padx=10)

R1=tk.Frame(calc_frame)
R1.grid(row=1,column=0,padx=5,pady=5)
btn=tk.Button(R1,text="C",height=1,width=6,font=("Arial",20),border=1,borderwidth=1,relief="solid")
btn.grid(row=0,column=0,padx=5,pady=5)
btn.bind("<Button-1>",submit)
btn=tk.Button(R1,text="()",height=1,width=6,font=("Arial",20),border=1,borderwidth=1,relief="solid")
btn.grid(row=0,column=1,padx=5,pady=5)
btn.bind("<Button-1>",submit)
btn=tk.Button(R1,text="%",height=1,width=6,font=("Arial",20),border=1,borderwidth=1,relief="solid")
btn.grid(row=0,column=2,padx=5,pady=5)
btn.bind("<Button-1>",submit)
btn=tk.Button(R1,text="/",height=1,width=6,font=("Arial",20),border=1,borderwidth=1,relief="solid")
btn.grid(row=0,column=3,padx=5,pady=5)
btn.bind("<Button-1>",submit)

R2=tk.Frame(calc_frame)
R2.grid(row=2,column=0,padx=5,pady=5)
btn=tk.Button(R2,text="7",height=1,width=6,font=("Arial",20),border=1,borderwidth=1,relief="solid")
btn.grid(row=0,column=0,padx=5,pady=5)
btn.bind("<Button-1>",submit)
btn=tk.Button(R2,text="8",height=1,width=6,font=("Arial",20),border=1,borderwidth=1,relief="solid")
btn.grid(row=0,column=1,padx=5,pady=5)
btn.bind("<Button-1>",submit)
btn=tk.Button(R2,text="9",height=1,width=6,font=("Arial",20),border=1,borderwidth=1,relief="solid")
btn.grid(row=0,column=2,padx=5,pady=5)
btn.bind("<Button-1>",submit)
btn=tk.Button(R2,text="X",height=1,width=6,font=("Arial",20),border=1,borderwidth=1,relief="solid")
btn.grid(row=0,column=3,padx=5,pady=5)
btn.bind("<Button-1>",submit)

R3=tk.Frame(calc_frame)
R3.grid(row=3,column=0,padx=5,pady=5)
btn=tk.Button(R3,text="4",height=1,width=6,font=("Arial",20),border=1,borderwidth=1,relief="solid")
btn.grid(row=0,column=0,padx=5,pady=5)
btn.bind("<Button-1>",submit)
btn=tk.Button(R3,text="5",height=1,width=6,font=("Arial",20),border=1,borderwidth=1,relief="solid")
btn.grid(row=0,column=1,padx=5,pady=5)
btn.bind("<Button-1>",submit)
btn=tk.Button(R3,text="6",height=1,width=6,font=("Arial",20),border=1,borderwidth=1,relief="solid")
btn.grid(row=0,column=2,padx=5,pady=5)
btn.bind("<Button-1>",submit)
btn=tk.Button(R3,text="-",height=1,width=6,font=("Arial",20),border=1,borderwidth=1,relief="solid")
btn.grid(row=0,column=3,padx=5,pady=5)
btn.bind("<Button-1>",submit)

R4=tk.Frame(calc_frame)
R4.grid(row=4,column=0,padx=5,pady=5)
btn=tk.Button(R4,text="1",height=1,width=6,font=("Arial",20),border=1,borderwidth=1,relief="solid")
btn.grid(row=0,column=0,padx=5,pady=5)
btn.bind("<Button-1>",submit)
btn=tk.Button(R4,text="2",height=1,width=6,font=("Arial",20),border=1,borderwidth=1,relief="solid")
btn.grid(row=0,column=1,padx=5,pady=5)
btn.bind("<Button-1>",submit)
btn=tk.Button(R4,text="3",height=1,width=6,font=("Arial",20),border=1,borderwidth=1,relief="solid")
btn.grid(row=0,column=2,padx=5,pady=5)
btn.bind("<Button-1>",submit)
btn=tk.Button(R4,text="+",height=1,width=6,font=("Arial",20),border=1,borderwidth=1,relief="solid")
btn.grid(row=0,column=3,padx=5,pady=5)
btn.bind("<Button-1>",submit)

R5=tk.Frame(calc_frame)
R5.grid(row=5,column=0,padx=5,pady=5)
btn=tk.Button(R5,text="^",height=1,width=6,font=("Arial",20),border=1,borderwidth=1,relief="solid")
btn.grid(row=0,column=0,padx=5,pady=5)
btn.bind("<Button-1>",submit)
btn=tk.Button(R5,text="0",height=1,width=6,font=("Arial",20),border=1,borderwidth=1,relief="solid")
btn.grid(row=0,column=1,padx=5,pady=5)
btn.bind("<Button-1>",submit)
btn=tk.Button(R5,text=".",height=1,width=6,font=("Arial",20),border=1,borderwidth=1,relief="solid")
btn.grid(row=0,column=2,padx=5,pady=5)
btn.bind("<Button-1>",submit)
btn=tk.Button(R5,text="=",height=1,width=6,font=("Arial",20),border=1,borderwidth=1,relief="solid")
btn.grid(row=0,column=3,padx=5,pady=5)
btn.bind("<Button-1>",submit)



window.mainloop()