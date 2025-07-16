from tkinter import *
from tkinter import messagebox
import pymysql
taz=Tk()
taz.title('Taz Hotel')
height=taz.winfo_screenheight()
#print(height)
width=taz.winfo_screenwidth()
#print(width)
def clear_screen():
    global taz
    for widgets in taz.winfo_children():
        widgets.grid_remove()
def dbconfig():
    global conn, mycursor
    conn=pymysql.connect(host="localhost",user="root",db="rajput_hotel")
    mycursor=conn.cursor()
def back():
    back_Button = Button(taz, text="Back", font=('arial', 18, 'normal'), fg="green", bd=10, command=welcomewindow)
    back_Button.grid(row=4, column=0, padx=10, pady=5)
    logoutButton = Button(taz, text="Logout", font=('arial',18,'normal'),width=8, fg="green", bd=10, command=adminLogout)
    logoutButton.grid(row=4, column=5, padx=20, pady=5)
def manage_restaurant():
    clear_screen()
    main_heading()
    labelmanage = Label(taz, text="Manage Restaurant", font=("ariel", 30, "bold"), bg="blue", fg="white")
    labelmanage.grid(row=1, column=2, columnspan=2, padx=0, pady=10)
    back()

def bill():
    clear_screen()
    main_heading()
    label_bill = Label(taz, text="Generate Bill", font=("ariel", 30, "bold"), bg="blue", fg="white")
    label_bill.grid(row=1, column=2, columnspan=2, padx=0, pady=10)
    back()
def adminLogout():
    clear_screen()
    main_heading()
    loginwindow()
def adminLogin():
    if usernameVar.get()=='' or passwordVar.get()=='':
        messagebox.showerror("Error",'Please enter Both Entries')
    else:
        # print(usernameVar.get())
        # print(passwordVar.get())
        dbconfig()
        username = usernameVar.get()
        password = passwordVar.get()
        que = "select * from login_info where username=%s and password=%s"
        val = (username, password)
        mycursor.execute(que, val)
        data = mycursor.fetchall()
        print(data)
        flag = False
        for row in data:
            flag = True
        conn.close()

        if flag == True:
            welcomewindow()
            # messagebox.showwarning('','login successfull')
        else:
            messagebox.showerror("Invalid User Credential", "Either User Name or Password is Incorrect")
            usernameVar.set("")
            passwordVar.set("")
#main heading
def main_heading():
    label=Label(taz,text="Rajput Hotel Management System",fg="red",bg="yellow",
            font=("comic sans Ms",40,"bold"),padx=350,pady=0)
    label.grid(row=0,columnspan=6)

usernameVar=StringVar()
passwordVar=StringVar()
def loginwindow():
    usernameVar.set("")
    passwordVar.set("")
    labellogin=Label(taz,text="Admin Login",font=("ariel",30,"bold"),bg="blue",fg="white")
    labellogin.grid(row=1,column=1,columnspan=4,padx=50,pady=10)

    usernameLabel=Label(taz,text="User Name",justify="left",font=("ariel",25,"bold"))
    usernameLabel.grid(row=2,column=0,columnspan=4,padx=50,pady=5)

    passwordLabel = Label(taz, text="User Password",font=("ariel",25,"bold"))
    passwordLabel.grid(row=3, column=0,columnspan=4, padx=20, pady=5)

    usernameEntry=Entry(taz,textvariable=usernameVar,font=('arial',20,'normal'))
    usernameEntry.grid(row=2,column=3,padx=20,pady=10)

    passwordEntry=Entry(taz,show="?",textvariable=passwordVar,font=('arial',20,'normal'))
    passwordEntry.grid(row=3, column=3, padx=20, pady=5)

    loginButton=Button(taz,text="Login",font=('arial',20,'normal'),width=10,fg="green",bd=10,command=adminLogin)
    loginButton.grid(row=4, column=1, columnspan=4,padx=20, pady=5)

# welcome window
def welcomewindow():
    clear_screen()
    main_heading()
    labelwelcome = Label(taz, text=" Welcome Admin ",font=("ariel",30,"bold"),bg="blue",fg="white")
    labelwelcome.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

    manage_restaurantButton = Button(taz, text="Manage Restaurant", font=('arial',18,'normal'),width=15, fg="green", bd=10, command=manage_restaurant)
    manage_restaurantButton.grid(row=4, column=0, padx=10, pady=5)

    bill_Button = Button(taz, text="Generate Bill", font=('arial',18,'normal'),width=15, fg="green", bd=10, command=bill)
    bill_Button.grid(row=4, column=1,columnspan=3, padx=20, pady=5)

    logoutButton = Button(taz, text="Logout", font=('arial',18,'normal'),width=8, fg="green", bd=10, command=adminLogout)
    logoutButton.grid(row=4, column=5, padx=20, pady=5)
main_heading()
loginwindow()
taz.geometry("%dx%d+0+0"%(width,height))
taz.mainloop()