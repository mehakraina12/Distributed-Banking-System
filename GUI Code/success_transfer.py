from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class success_transfer:
    def __init__(self,root):
        self.root=root
        self.root.title("Banking System")
        self.root.geometry("1199x600+100+50")
        self.bg=ImageTk.PhotoImage(file="success_depoit.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        Frame_login=Frame(self.root,bg="light yellow")
        Frame_login.place(x=250,y=180,height=350,width=800)

        desc=Label(Frame_login,text="Your transfer of amount1 was successful!",font=("Goudy old style",25,"bold"),fg="#d25d17",bg="light yellow").place(x=85,y=100)
        desc=Label(Frame_login,text="Current Balance is amount2.",font=("Goudy old style",25,"bold"),fg="#d25d17",bg="light yellow").place(x=85,y=150)
    

        Login_btn=Button(Frame_login,text="Go to Dashboard",fg="white",bg="sea green",font=("times new roman",20)).place(x=350,y=260,width=340,height=40)

    def success_transfer(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

root=Tk()
obj=success_transfer(root)
root.mainloop()