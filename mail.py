from cProfile import label
import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror


def main_mail():
    def send_sms(number, message):
        url = 'https://www.fast2sms.com/dev/bulk'
        params = {
            'authorization': 'BKJzNoTH06IsnHEqr8EuTvxAbXzQcF1XCBheCTp2qvfBpBLyhkQAPJoyTIIQ',
            'sender_id': 'FSTSMS',
            'message': message,
            'language': 'english',
            'route': 'p',
            'numbers': number
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
    root.title("SEND MAIL ")
    root.geometry("400x580+800+60")
    root.configure(bg='yellow')
    root.resizable(False,False)
    font = ("Helvetica", 15, "bold")
    label=Label(root,text='WRITE MAIL IN THE BOX < O O >',bg='yellow',font=('Arial bold',12)).pack()
    textMsg = Text(root,bg='white')
    textMsg.pack(fill=X)
    phone=Label(root,text='\t\t\t\t\t\n Enter your Mail ID , and click send button . \n\t\t\t\t\t',bg="blue",fg="white",font=('Arial bold',13),bd=18,borderwidth=2,relief='ridge')
    phone.pack()
    textNumber = Entry(root, font=font,bg='white',fg='black',bd=18,borderwidth=2,relief='ridge',width='29')
    textNumber.pack(padx=1, pady=14)
    sendBtn = Button(root, text="SEND MAILL ", command=btn_click,bg='green',width=22,fg='white')
    sendBtn.place(x=120,y=527)
    root.mainloop()

