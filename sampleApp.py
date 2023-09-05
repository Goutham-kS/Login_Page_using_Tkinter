from tkinter import *
app=Tk()
app.geometry("1200x800")
app.configure(bg="green")
def login():
    a=user.get()
    b=password.get()
    if(a=="admin" and b=="1234"):
        print("login is succesfull")
    else:
        print("login failed")

user=StringVar()
password=StringVar()
lb1=Label(app,fg="black",bg="white",font=("arial",50,"bold"),text="SampleApp").place(x=500,y=10)
lb2=Label(app,fg="red",bg="white",font=("arial",25,"bold"),text="Username").place(x=100,y=200)
lb3=Label(app,fg="red",bg="white",font=("arial",25,"bold"),text="Password").place(x=100,y=300)
El1=Entry(app,fg="red",bg="white",font=("arial",25,"bold"),textvariable=user).place(x=350,y=200)
El2=Entry(app,fg="red",bg="white",font=("arial",25,"bold"),textvariable=password).place(x=350,y=300)
bt=Button(app,fg="blue",bg="white",font=("arial",23,"bold"),text="Login",command=login).place(x=500,y=450)


