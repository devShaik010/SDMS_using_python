import main
from tkinter import *
from tkinter import messagebox 

def body():
    login_window = Tk()
    user = 'admin'
    password = '1234'
    login_window.title('ADMIN_LOGIN')

    login = Label(login_window, text=' ADMIN_LOGIN', bg='#0f2f7f', fg='white', font=("arial", 20, 'bold'))
    login.place(relx=0.3, rely=0.1)
    login_window.configure(bg='#0f2f7f')
    login_window.geometry('520x320+450+150')
    login_window.resizable(False, False)

    user_name = Label(login_window, text='>> User Name  ', font='bold',bd=18,borderwidth=2,relief='ridge')
    user_name.place(relx='0.2', rely='0.3')
    entry1 = Entry(login_window, )
    entry1.place(relx='0.5', rely='0.3')

    user_pass = Label(login_window, text='>> Password   . ', font='bold',bd=18,borderwidth=2,relief='ridge')
    user_pass.place(relx='0.2', rely='0.4')
    entry2 = Entry(login_window, )
    entry2.place(relx='0.5', rely='0.4')

    # ==================================================>>

    def login_b():
        user_name1 = entry1.get()  
        user_pass1 = entry2.get()
        
        if user_name1 =="" and user_pass1=="":
            messagebox.showwarning('ERROR !',' Please enter Id \n and password .. ')

        elif user == user_name1 and password == user_pass1:
            messagebox.showinfo('login success', 'LOGIN SUCESS USER MACTHED !')
            login_window.destroy()
            main.window()
        
        else:
            messagebox.showwarning('login field !', 'Please check user_name or Password')
    # ====================================================>>

    login_button = Button(login_window, text='login', bg='BLACK', fg='white', width=39, command=login_b)
    login_button.place(relx='0.2', rely='0.5')

    ragister_button = Button(login_window, text=' Ragister Now !', bg='BLACK', fg='white', width=13)
    ragister_button.place(relx='0.6', rely='0.7')

    mauu_msg = Label(login_window, text=' @CREATE BY OUR TEAM')
    mauu_msg.place(relx='0.3', rely='0.9')

    login_window.mainloop()
body()
