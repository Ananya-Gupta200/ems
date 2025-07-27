from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or pwdEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif usernameEntry.get()=='Ananya' and pwdEntry.get()=='1234':
        messagebox.showinfo('Success','Login is successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','wrong credentials')
root=CTk()
root.geometry('1200x563')
root.resizable(0,0)
root.title('Login Page')
image= CTkImage(Image.open('employee.jpg'),size=(1200,563))
imageLabel=CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)

headinglabel=CTkLabel(root,text='Employee Management System',bg_color='#FEFEFE', font=('Gody Old Style',25,'bold'),text_color='dark blue')
headinglabel.place(x=40,y=140)

usernameEntry = CTkEntry(root,placeholder_text='Enter Your Username',width=200)
usernameEntry.place(x=80,y=200)

pwdEntry = CTkEntry(root,placeholder_text='Enter Your Password',width=200,show='*')
pwdEntry.place(x=80,y=235)

loginButton =CTkButton(root, text='Login',cursor='hand2',command = login)
loginButton.place(x=105,y=280)




root.mainloop()
