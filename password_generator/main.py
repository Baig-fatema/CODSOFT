import tkinter as tk
import random
import string
from tkinter import messagebox as msg
window=tk.Tk()
window.title("Password Generator")
window.geometry("600x400")
window.minsize(height=400,width=600)
window.config(bg="lightblue")
def submit():
    print(name_entry.get())
    print(pass_entry.get())
    res=""
    if name_entry.get()!="" and pass_entry.get()!="":
        n=int(pass_entry.get())
        temp=str(name_entry.get())
        res=res.join(random.choices(temp+string.digits+"@$.&",k=n))
        res_lable=tk.Label(main_frame,text=f"{res}",font=("Arial",20,"bold"),bg="pink",fg="green",border=1,borderwidth=1,relief="solid")
        res_lable.grid(row=7,column=0,padx=10,pady=10)
    else:
        msg.showerror("Error!","Please enter length and string")

head=tk.Label(window,text="CODSOFT  PASSWORD  GENERATOR",width=1200,bg="black",fg="white",font=("Arial",25,"bold"))
head.pack()
main_frame=tk.Frame(window,border=2,borderwidth=2,relief="solid",bg="lightblue")
main_frame.pack(padx=10,pady=40)
name_str=tk.StringVar()
name_label=tk.Label(main_frame,text="Enter Name String: ",bg="lightblue",font=("Arial",15))
name_label.grid(row=0,column=0,padx=10,pady=20)
name_entry=tk.Entry(main_frame,font=("Arial",15),textvariable=name_str)
name_entry.grid(row=0,column=2,padx=10,pady=20)
pass_str=tk.StringVar()
pass_label=tk.Label(main_frame,text="Enter Length of Password: ",bg="lightblue",font=("Arial",15))
pass_label.grid(row=3,column=0,padx=10,pady=20)
pass_entry=tk.Entry(main_frame,font=("Arial",15),textvariable=pass_str)
pass_entry.grid(row=3,column=2,padx=10,pady=20)

btn=tk.Button(main_frame,text="Generate Password",bg="lightgrey",fg="black",font=("Arial",20,"bold"),border=2,borderwidth=2,relief="solid",command=submit)
btn.grid(row=5,column=0,padx=10,pady=10)

window.mainloop()