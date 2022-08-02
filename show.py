import sqlite3 
import tkinter as tk
from tkinter import *
con=sqlite3.connect('college.db')

def show_data():
        fr1 = tk.Tk()
        cur = con.cursor()
        fr1.geometry("800x300")
        fr1.resizable(False,False)
        students = cur.execute("SELECT * FROM student")
        fr1.title('STUDENT NAME ==> FATHER NAME ==> ROLL NUMBER ==> MAIL ID ==> PHONE NO ')
        fr1.configure(bg='white')
        i=1
        j=1
        for student in students:
            if(i==1):
                l1=Label(fr1,text="S.NO\t",bg="red",fg="white",font=("Helvetica bold", "11")).grid(row=i,column=0)
                # l2=Label(fr1,text="\tSTUDENT NAME ==> FATHER NAME ==> ROLL NUMBER ==> MAIL ID ==> PHONE NO ",bg="white",fg="black",font=("Helvetica", "11")).grid(row=i,column=1)
                # # l3=Label(fr1,text="\t| FATHER NAME |",bg="white",fg="black",font=("Helvetica", "11")).grid(row=i,column=2)
                # # l4=Label(fr1,text="\t| ROLL NO |",bg="white",fg="black",font=("Helvetica", "11")).grid(row=i,column=3)
                # # l5=Label(fr1,text="\t| MAIL ID |",bg="white",fg="black",font=("Helvetica", "11")).grid(row=i,column=4)
                # # l6=Label(fr1,text="\t| PHONE NO |",bg="white",fg="black",font=("Helvetica", "11")).grid(row=i,column=5)
                i+=1
            
            l7=Label(fr1,text='{ '+str(j)+' }',bg="white",fg="black",font=("Helvetica", "10")).grid(row=i,column=0)
            l8=Label(fr1,text="[ "+student[0]+' ]',bg="white",fg="blue",font=("Helvetica", "10")).grid(row=i,column=1)
            l9=Label(fr1,text="[ "+student[1]+' ]',bg="white",fg="blue",font=("Helvetica", "10")).grid(row=i,column=2)
            l10=Label(fr1,text="[ "+student[2]+' ]',bg="white",fg="blue",font=("Helvetica", "10")).grid(row=i,column=3)
            l11=Label(fr1,text="[ "+student[3]+' ]',bg="white",fg="blue",font=("Helvetica", "10")).grid(row=i,column=4)
            l12=Label(fr1,text="[ "+student[4]+' ]',bg="white",fg="blue",font=("Helvetica", "10")).grid(row=i,column=5)
            i+=1
            j+=1
        fr1.mainloop()    
   
            