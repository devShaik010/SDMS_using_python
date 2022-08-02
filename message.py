import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror


def main_msg():
    def send_sms(number, message):
        url = 'https://www.fast2sms.com/dev/bulkV2'
        params = {
            'authorization': 'Hqn5nMTJfyBUCaKdT8WR9SSa2e05Pa9nvcSAHptKWtnaDr4M49Z9YxVzkrCV',
            'sender_id': 'TXTIND',
            'message': message,
            'language': 'english',
            'route': 'v3',
            'numbers':number
        }
        response = requests.get(url, params=params)
        dic = response.json()
        print(dic)
        return dic.get('return')


    def btn_click():
        num = textNumber.get()
        msg = textMsg.get("1.0", END)
        r = send_sms(num, msg)
        if r:
            showinfo("Send Success", "Successfully sent")
        else:
            showerror("Error", "Something went wrong..")


# Creating GUI
    root = Tk()
    root.title("Send_messeg")
    root.geometry("300x480+800+60")
    root.resizable(False,False)    
    font = ("Helvetica", 18, "bold")
    phone=Label(root,text='Enter Mobile number ',bg="blue",fg="white",font=('curiar bold',15),bd=18,borderwidth=2,relief='ridge')
    phone.pack()
    textNumber = Entry(root, font=font,bg='white',fg='black',bd=18,borderwidth=2,relief='ridge')
    textNumber.pack(padx=12, pady=14)
    textMsg = Text(root,bg='white')
    textMsg.pack(fill=X)
    sendBtn = Button(root, text="SEND SMS", command=btn_click,bg='blue',width=22,fg='white')
    sendBtn.place(relx=0.2,rely=0.9)
    root.mainloop()


