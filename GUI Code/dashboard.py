import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

# create a Tkinter window
window = tk.Tk()

# set the window title and size
window.title("Distributed Banking System")
window.configure(bg="#000000")

window.geometry("800x600")

# set the background image
bg_image = ImageTk.PhotoImage(Image.open("bg.png"))
bg_label = tk.Label(window, image=bg_image)
bg_label.place(x=40, y=0, relwidth=1, relheight=1)

heading=tk.Label(window,text='Distributed Banking System',fg='red',bg='white',font=('Goudy old style',25,'bold'))
heading.place(x=440,y=50)

heading=tk.Label(window,text='Dashboard',fg='red',bg='white',font=('Goudy old style',25,'bold'))
heading.place(x=540,y=150)

# add fancy icons
icon_size = (120, 120)
ss= (38,38)
deposit_icon = Image.open("deposit.jpg").resize(icon_size)
deposit_icon = ImageTk.PhotoImage(deposit_icon)
withdraw_icon = Image.open("withdraw.jpg").resize(icon_size)
withdraw_icon = ImageTk.PhotoImage(withdraw_icon)
query_icon = Image.open("query.jpg").resize(icon_size)
query_icon = ImageTk.PhotoImage(query_icon)
transfer_icon = Image.open("transfer.jpg").resize(icon_size)
transfer_icon = ImageTk.PhotoImage(transfer_icon)

# add deposit option
deposit_button = ttk.Button(window, text="Deposit", image=deposit_icon, compound="top", style="Option.TButton")
deposit_button.place(relx=0.25, rely=0.4, anchor="center")

# add query option
query_button = ttk.Button(window, text="Query", image=query_icon, compound="top", style="Option.TButton")
query_button.place(relx=0.25, rely=0.7, anchor="center")

# add withdraw option
withdraw_button = ttk.Button(window, text="Withdraw", image=withdraw_icon, compound="top", style="Option.TButton")
withdraw_button.place(relx=0.75, rely=0.4, anchor="center")

# add transfer option
transfer_button = ttk.Button(window, text="Transfer", image=transfer_icon, compound="top", style="Option.TButton")
transfer_button.place(relx=0.75, rely=0.7, anchor="center")

# add custom styles
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 14), background="#1C1C1C", foreground="blue", borderwidth=0)
style.configure("Option.TButton", padding=20)

# run the main event loop
window.mainloop()
