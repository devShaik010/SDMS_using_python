import tkinter as tk  
import sqlite3
from tkinter import messagebox

con = sqlite3.connect("college.db")
def del_win():
    root=tk.Tk()
    root.title("Delete Window")
    root.configure(bg="indigo")
    root.geometry("350x150+100+50")
    
    def del_data():
        st_id = str(i1.get())    
        st_name = str(i2.get())
        
        if st_id!="" and st_name!="":
            con.execute("DELETE FROM student where roll_no = ? ",(st_id,))
            con.commit()
            con.close()
            messagebox.showerror('delete ! 😎'," "+st_name+"is deleted")
        else:
            messagebox.showerror('requirment error 😎','please fill the all details')
    heading =tk.Label(root,text="Enter id Number to delete ",font=("Arial bold",13))
    heading.grid(row=0,column=1)
    sp=tk.Label(root,text="",bg="indigo",fg="indigo")
    sp.grid(row=1,column=1)

    l1=tk.Label(root,text="Enter ID : ",bg="black",fg="white")
    l1.grid(row=2,column=0)

    l2=tk.Label(root,text="Enter Name : ",bg="black",fg="white")
    l2.grid(row=3,column=0)

    i1=tk.Entry(root,width=28)
    i1.grid(row=2,column=1)

    i2=tk.Entry(root,width=28)
    i2.grid(row=3,column=1)

    s1=tk.Label(root,text="",bg="indigo",fg="indigo")
    s1.grid(row=4,column=1)
    butonn=tk.Button(root,text="Delete",bg="black",fg="white",width=25,command=del_data)
    butonn.grid(row=5,column=1)
    root.mainloop()

