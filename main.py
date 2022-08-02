from tkinter import *
from tkinter import messagebox
import sqlite3
import message
import mail
import time
import delete
import update 
import show

con = sqlite3.connect("college.db")
def creat_table():
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(student_name text,student_father text,roll_no text,mail_id text,phon_no text)")
    con.commit()
    print(" table created sucsess ...... ")

global counter 
counter = 1

def show_d():
    show.show_data()

def del_win():
    root=Tk()
    root.title("Delete Window")
    root.configure(bg="indigo")
    root.geometry("350x150+100+50")
    
    def del_data():
        st_id = str(i1.get())    
        st_name = str(i2.get())
        
        if st_id!="" and st_name!="":
            sql = 'DELETE FROM student WHERE roll_no=?'
            cur = con.cursor()
            cur.execute(sql,(st_id,))
            con.commit() 
            messagebox.showerror('delete ! 😎'," "+st_name+"is deleted")
        else:
            messagebox.showerror('requirment error 😎','please fill the all details')
    heading =Label(root,text="Enter id Number to delete ",font=("Arial bold",13))
    heading.grid(row=0,column=1)
    sp=Label(root,text="",bg="indigo",fg="indigo")
    sp.grid(row=1,column=1)

    l1=Label(root,text="Enter ID : ",bg="black",fg="white")
    l1.grid(row=2,column=0)

    l2=Label(root,text="Enter Name : ",bg="black",fg="white")
    l2.grid(row=3,column=0)

    i1=Entry(root,width=28)
    i1.grid(row=2,column=1)

    i2=Entry(root,width=28)
    i2.grid(row=3,column=1)

    s1=Label(root,text="",bg="indigo",fg="indigo")
    s1.grid(row=4,column=1)
    butonn=Button(root,text="Delete",bg="black",fg="white",width=25,command=del_data)
    butonn.grid(row=5,column=1)
    root.mainloop()

def new_st():
     def inform():
        name   = i1.get()
        father = i2.get()
        roll   = i3.get()
        mail   = i4.get()
        phone  = i5.get()
     
        if name == "" or father == "" or roll == "" or mail == "" or phone == "":
            messagebox.showwarning('Empty','fill all details ! ')
        else:
         list=[(name,father,roll,mail,phone)]
         cur=con.cursor()
         cur.executemany("INSERT INTO student VALUES (?,?,?,?,?)",list)
         con.commit()
         print("done brooo ................... ")
         messagebox.showinfo('Add Success ',' Added '+name+" in database . ")

     def clear_text():
        i1.delete(0, END)   
        i2.delete(0, END)
        i3.delete(0, END)
        i4.delete(0, END)
        i5.delete(0, END)

     global counter
     if(counter < 2):
        root=Tk()
        root.title('ENTER STUDEN DETAILS ')   
        root.configure(bg='#0E0051')
        root.geometry('390x280+800+200')
        root.resizable(False,False)

        lh=Label(root,text="Insert student detail's\t\t ",font=('Arial bold',13),bg='yellow',fg='black').grid(row=0,column=1)
        ls=Label(root,text="   ",bg="#0E0051").grid(row=1,column=1)
            
        l1=Label(root,text="Student Name  :",font=('bold',12),bg='green',fg='black',bd=18,borderwidth=2,relief='ridge').grid(row=2,column=0)
        i1=Entry(root,width=38,bg='white',fg='black',bd=18,borderwidth=2,relief='ridge')
        i1.grid(row=2,column=1)
        
        l2=Label(root,text="Father  Name   :",font=('bold',12),bg='yellow',fg='black',bd=18,borderwidth=2,relief='ridge').grid(row=3,column=0)
        i2=Entry(root,width=38,bg='white',fg='black',bd=18,borderwidth=2,relief='ridge')
        i2.grid(row=3,column=1)
                
        l3=Label(root,text="Roll   Number   :",font=('bold',12),bg='skyblue',fg='black',bd=18,borderwidth=2,relief='ridge').grid(row=4,column=0)
        i3=Entry(root,width=38,bg='white',fg='black',bd=18,borderwidth=2,relief='ridge')
        i3.grid(row=4,column=1)
            
        l4=Label(root,text="Mail  account    :",font=('bold',12),bg='red',fg='black',bd=18,borderwidth=2,relief='ridge').grid(row=5,column=0)
        i4=Entry(root,width=38,bg='white',fg='black',bd=18,borderwidth=2,relief='ridge')
        i4.grid(row=5,column=1)

        l5=Label(root,text="Phone number  :",font=('bold',12),bg='black',fg='white',bd=18,borderwidth=2,relief='ridge').grid(row=6,column=0)
        i5=Entry(root,width=38,bg='white',fg='black',bd=18,borderwidth=2,relief='ridge')
        i5.grid(row=6,column=1)

        l0=Label(root,font=('bold',12),bg='#0E0051').grid(row=7,column=0)
        reset=Button(root,text=" clear ",bg='black',fg='white',bd=18,borderwidth=2,relief='ridge',width=14,command=clear_text).grid(row=8,column=0)    
        enter=Button(root,text=" Enter ",bg='black',fg='white',bd=18,borderwidth=2,relief='ridge',width=24,command=inform).grid(row=8,column=1)    
        
        counter+=1
        root.mainloop()
     else:
        messagebox.showerror('Input error ! ','Window is already open')
        counter = 1

def test(query):               
     query=str(input(" Enter query >> "))
     return query

def about():
    messagebox.showinfo('THANKS FOR CLICK', 'SORRY WE ARE WORKING ON THIS FETURE ')

def window():  
    root = Tk()
    root.title('HOME_PAGE')
    root.geometry('1280x660+45+2')
    root.configure(bg='indigo')
     
    label = Label(root, text="TIME", font=("Arial", 15), bg='#002040', fg="white", bd=18,borderwidth = 2,relief="ridge",)
    label.place(relx=1, x=-2, y=2, anchor=NE)

    def digitalclock():
        text_input = time.strftime("%H:%M:%S ")
        label.config(text=text_input)
        label.after(200, digitalclock)

    digitalclock()
    menubar = Menu(root, background='black', foreground='white', activebackground='gray', activeforeground='black', bd=18,borderwidth = 2,relief="ridge")
   
    edit = Menu(menubar, tearoff=0, bg='white')
    edit.add_command(label="@ MESSAGE ", command=message.main_msg)
    edit.add_command(label="@ GMAIL.COM ", command=mail.main_mail)
    menubar.add_cascade(label="  || CONTACT || ", menu=edit)

    help = Menu(menubar, tearoff=0, bg='white')
    help.add_command(label="SEND FEEDBACK !", command=about)
    menubar.add_cascade(label="  || FEED BACK || ", menu=help)
    root.config(menu=menubar)

    # ===============options==========================
    
    bgimg3= PhotoImage(file = "images/group.png")
    limg3= Label(root, i=bgimg3)
    limg3.place(x=90,rely=0.07)
    
    show_st=Button(root,text="Show Student's",bg="white",fg='black',font=("Arial bold",10),bd=15,borderwidth=4,relief='ridge',command=show_d)
    show_st.place(x=72,y=130)
  

    bgimg1= PhotoImage(file = "images/student.png")
    limg1= Label(root, i=bgimg1)
    limg1.place(x=258,rely=0.07)
    
    show_st1=Button(root,text="Add Student",bg="white",fg='black',font=("Arial bold",10),bd=15,borderwidth=4,relief='ridge',command=new_st)
    show_st1.place(x=250,y=130)

    bgimg2= PhotoImage(file = "images/trash.png")
    limg2= Label(root, i=bgimg2)
    limg2.place(x=419,rely=0.07)
    
    show_st2=Button(root,text="Delete-[DATA]",bg="white",fg='black',font=("Arial bold",10),bd=15,borderwidth=4,relief='ridge',command=delete.del_win)
    show_st2.place(x=405,y=130)

    bgimg4= PhotoImage(file = "images/update.png")
    limg4= Label(root, i=bgimg4)
    limg4.place(x=585,rely=0.07)
    
    show_st4=Button(root,text="Update details",bg="white",fg='black',font=("Arial bold",10),bd=15,borderwidth=4,relief='ridge',command=update.up_win)
    show_st4.place(x=570,y=130)


    bgimg5= PhotoImage(file = "images/messages.png")
    limg5= Label(root, i=bgimg5)
    limg5.place(x=885,rely=0.07)
    
    show_st5=Button(root,text="Send Message",bg="white",fg='black',font=("Arial bold",10),bd=15,borderwidth=4,relief='ridge',command=message.main_msg)
    show_st5.place(x=870,y=130)


    bgimg6= PhotoImage(file = "images/email.png")
    limg6= Label(root, i=bgimg6)
    limg6.place(x=1055,rely=0.07)
    
    show_st6=Button(root,text=" Send Mail ",bg="white",fg='black',font=("Arial bold",10),bd=15,borderwidth=4,relief='ridge',command=mail.main_mail)
    show_st6.place(x=1050,y=130)
   # ========================form fram=======================
   
    root.mainloop()
creat_table()    
