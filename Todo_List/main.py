import tkinter as tk
from tkinter import messagebox
import csv
import sqlite3

window=tk.Tk()
window.title("TO DO LIST")
# window.iconbitmap("calc.ico")
window.config(background="cyan")
window.geometry("600x400")
window.minsize(height=444,width=1300)
def ADD():
    if(add_title_entry.get()!="" and add_date_entry.get()!=""):
        title=add_title_entry.get()
        days=add_date_entry.get()
        prog=int(add_pro_spin.get())
        con=sqlite3.Connection("todo.db")
        cur=con.cursor()
        table_create='''
                CREATE TABLE IF NOT EXISTS tasktable
                (task TEXT,days TEXT,prog INT)
                '''   
        con.execute(table_create)
            # insert
        data_insert='''
                 insert into tasktable(task,days,prog)
                 values(?,?,?)
            '''
        data_insert_tuple=(title,days,prog)
        row=cur.execute(data_insert,data_insert_tuple)
        if row:
            print("fetch")
            lab=tk.Label(add,text="Task Added Successfully!",font=("arial",10,"bold"),width=40,height=2,bg="lightgrey",fg="Green",border=2,borderwidth=2,relief="solid")
            lab.grid(row=10,column=2)
        else:
            print("Failed")
            lab=tk.Label(add,text="Add Task Failed!",font=("arial",10,"bold"),width=40,height=2,bg="lightgrey",fg="red",border=2,borderwidth=2,relief="solid")
            lab.grid(row=10,column=2)     
        con.commit()
        con.close()
        
    else:
        messagebox.showerror("Error!","please enter title and date")
        lab=tk.Label(add,text="Add TasK Failed!",font=("arial",10,"bold"),width=40,height=2,bg="lightgrey",fg="red",border=2,borderwidth=2,relief="solid")
        lab.grid(row=10,column=2)        

def editTask():
    if(edit_title_entry.get()!="" and edit_date_entry.get()!=""):
        title=edit_title_entry.get()
        days=edit_date_entry.get()
        prog=int(edit_pro_spin.get())
        con=sqlite3.Connection("todo.db")
        cur=con.cursor()
        update_query=f"update tasktable set days=?,prog=? where task=?"
        update_tup=(days,prog,title)
        row=cur.execute(update_query,update_tup)
        if row.rowcount>0:
            print("edited")
            lab=tk.Label(edit,text="Task Edited Successfully!",font=("arial",10,"bold"),width=40,height=2,bg="lightgrey",fg="Green",border=2,borderwidth=2,relief="solid")
            lab.grid(row=10,column=2)
        else:
            print("eidit Failed")
            lab=tk.Label(edit,text="Task Edit Failed!",font=("arial",10,"bold"),width=40,height=2,bg="lightgrey",fg="red",border=2,borderwidth=2,relief="solid")
            lab.grid(row=10,column=2)     
        con.commit()
        con.close()
        
    else:
        messagebox.showerror("Error!","please enter title and date")
        lab=tk.Label(edit,text="Task Edit Failed!",font=("arial",10,"bold"),width=40,height=2,bg="lightgrey",fg="red",border=2,borderwidth=2,relief="solid")
        lab.grid(row=10,column=2)        

    

def trackTask():
    con=sqlite3.Connection("todo.db")
    cur=con.cursor()
    sel="select * from tasktable"
    cur.execute(sel)
    rows=cur.fetchall()
    r=9
    for i in rows:
        lab=tk.Label(track,text=f"{i}%",font=("arial",10),width=40,height=1,bg="lightgrey",fg="black",border=2,borderwidth=2,relief="solid")
        lab.grid(row=r,column=2)
        r=r+1


    con.commit()
    con.close()

# main desig
frame=tk.Frame(window,bg="cyan")
frame.pack()
heading=tk.Label(frame,text="TO DO LIST",bg="black",fg="white",font=("Arial",25,"bold"),width="1200")
heading.pack()
body=tk.Frame(frame,bg="cyan",pady=30)
body.pack()


# add task
add=tk.LabelFrame(body,padx=30,pady=50,text="Add New Task",bg="lightgrey",font=("Arial",15,"bold"),fg="red",border=2,relief="solid")
add.grid(row=4,column=0,padx=20,pady=30)

add_title=tk.Label(add,text="Title: ",font=("arial",10,"bold"),width=40,height=2)
add_title.grid(row=1,column=2,columnspan=2)
add_date=tk.Label(add,text="Days to Complete task: ",font=("arial",10,"bold"),width=40,height=2)
add_date.grid(row=3,column=2,columnspan=2)
add_progress=tk.Label(add,text="Progress %: ",font=("arial",10,"bold"),width=40,height=2)
add_progress.grid(row=5,column=2,columnspan=2)

add_title_var=tk.StringVar()
add_title_entry=tk.Entry(add,width=45,border=1,borderwidth=1,relief="solid",font=("arial",10,"bold"),textvariable=add_title_var)
add_title_entry.grid(row=2,column=2)

add_date_var=tk.StringVar()
add_date_entry=tk.Entry(add,width=45,border=1,borderwidth=1,relief="solid",font=("arial",10,"bold"),textvariable=add_date_var)
add_date_entry.grid(row=4,column=2)

add_pro_spin=tk.Spinbox(add,from_=0,to=100,width=45,font=("arial",10,"bold"),borderwidth=1,relief="solid")
add_pro_spin.grid(row=6,column=2)

add_btn=tk.Button(add,text="Add Task",width=20,font=("arial",15,"bold"),height=1,border=2,borderwidth=2,relief="solid",background="green",fg="red",command=ADD)  #
add_btn.grid(row=8,column=2)


for widget in add.winfo_children():
    widget.grid_configure(padx=5,pady=10)
  

# edit task
edit=tk.LabelFrame(body,padx=30,pady=50,text="Edit Task",bg="lightgrey",font=("Arial",15,"bold"),fg="red",border=2,relief="solid")
edit.grid(row=4,column=1,padx=20,pady=30)
edit_title=tk.Label(edit,text="Title: ",font=("arial",10,"bold"),width=40,height=2)
edit_title.grid(row=1,column=2,columnspan=2)
edit_date=tk.Label(edit,text="Days to Complete task: ",font=("arial",10,"bold"),width=40,height=2)
edit_date.grid(row=3,column=2,columnspan=2)
edit_progress=tk.Label(edit,text="Progress %: ",font=("arial",10,"bold"),width=40,height=2)
edit_progress.grid(row=5,column=2,columnspan=2)

edit_title_var=tk.StringVar()
edit_title_entry=tk.Entry(edit,width=45,border=1,borderwidth=1,relief="solid",font=("arial",10,"bold"),textvariable=edit_title_var)
edit_title_entry.grid(row=2,column=2)

edit_date_var=tk.StringVar()
edit_date_entry=tk.Entry(edit,width=45,border=1,borderwidth=1,relief="solid",font=("arial",10,"bold"),textvariable=edit_date_var)
edit_date_entry.grid(row=4,column=2)

edit_pro_spin=tk.Spinbox(edit,from_=0,to=100,width=45,font=("arial",10,"bold"),borderwidth=1,relief="solid")
edit_pro_spin.grid(row=6,column=2)

edit_btn=tk.Button(edit,text="Edit Task",width=20,font=("arial",15,"bold"),height=1,border=2,borderwidth=2,relief="solid",background="green",fg="red",command=editTask)
edit_btn.grid(row=8,column=2)

for widget in edit.winfo_children():
    widget.grid_configure(padx=5,pady=10)

# track task
track=tk.LabelFrame(body,padx=30,pady=50,text="Track Task",bg="lightgrey",font=("Arial",15,"bold"),fg="red",border=2,relief="solid")
track.grid(row=4,column=2,padx=20,pady=30)

track_btn=tk.Button(track,text="Track Tasks",width=20,font=("arial",15,"bold"),height=1,border=2,borderwidth=2,relief="solid",background="green",fg="red",command=trackTask)
track_btn.grid(row=1,column=2)

track_title=tk.Label(track,text="Task,Days,Progress ",font=("arial",10,"bold"),width=40,height=2)
track_title.grid(row=3,column=2,columnspan=2)

for widget in track.winfo_children():
    widget.grid_configure(padx=5,pady=10)
    

window.mainloop()
