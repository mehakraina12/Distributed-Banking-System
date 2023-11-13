from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Banking System")
        self.root.geometry("1199x600+100+50")
        self.bg=ImageTk.PhotoImage(file="login2.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=300,y=150,height=450,width=700)

        title=Label(Frame_login,text="Distributed Banking System",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc=Label(Frame_login,text="Login",font=("Goudy old style",25,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)

        lbl_user=Label(Frame_login,text="Account Number",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=150)
        self.txt_user=Entry(Frame_login,font=("times new roman",25),bg="lightgray")
        self.txt_user.place(x=90,y=190,width=350,height=35)

        lbl_user=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=250)
        self.txt_pass=Entry(Frame_login,font=("times new roman",25),bg="lightgray", show='*')
        self.txt_pass.place(x=90,y=290,width=350,height=35)

        Login_btn=Button(Frame_login,text="Login",fg="white",bg="#d77337",font=("times new roman",20)).place(x=90,y=380,width=340,height=40)

    def login(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

root=Tk()
obj=Login(root)
root.mainloop()