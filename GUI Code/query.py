from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class query:
    def __init__(self,root):
        self.root=root
        self.root.title("Banking System")
        self.root.geometry("1199x600+100+50")
        self.bg=ImageTk.PhotoImage(file="deposit_f1.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=300,y=200,height=350,width=700)

        title=Label(Frame_login,text="Know your balance here!",font=("Impact",35,"bold"),fg="sea green",bg="white").place(x=90,y=30)
        desc=Label(Frame_login,text="Current Balance",font=("Goudy old style",25,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)

        lbl_user=Label(Frame_login,text="Account Number",font=("Goudy old style",15,"bold"),fg="black",bg="white").place(x=90,y=150)
        self.txt_user=Entry(Frame_login,font=("times new roman",25),bg="lightgray")
        self.txt_user.place(x=90,y=190,width=350,height=35)

        Login_btn=Button(Frame_login,text="Submit",fg="white",bg="sea green",font=("times new roman",20)).place(x=90,y=260,width=340,height=40)

    def query(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

root=Tk()
obj=query(root)
root.mainloop()