from tkinter import *
from tkinter import messagebox, StringVar
from PIL import ImageTk, Image
import pymysql

taz=Tk()
taz.title('Taz Hotel')
height=taz.winfo_screenheight()
#print(height)
width=taz.winfo_screenwidth()
# print(width)
c=['#F31C20','#1CF31F','#FFE54A','black','white','#D17DF3']
taz.config(bg='cyan')
logo=ImageTk.PhotoImage(Image.open(r'C:\Users\Aniket\Downloads\Screenshot 2025-07-16 214243.png'))
def clear_screen():
    global taz
    for widgets in taz.winfo_children():
        widgets.grid_remove()
def dbconfig():
    global conn, mycursor
    conn=pymysql.connect(host="localhost",user="root",db="rajput_hotel")
    mycursor=conn.cursor()
def back():
    back_Button = Button(taz, text="Back", font=('arial', 25, 'bold'), fg="white",bg='blue', bd=10, command=welcomewindow)
    back_Button.grid(row=1,rowspan=2, column=0, padx=10, pady=5)
    logoutButton = Button(taz, text="Logout", font=('arial',25,'bold'), fg="white", bg='red',bd=10, command=adminLogout)
    logoutButton.grid(row=1,rowspan=2 ,column=5, pady=5)

def add_Items():
    if itemName.get()=='' or itemType.get()=='' or itemRate.get()=='':
        messagebox.showerror("Error",'Please enter All Details')
    elif itemRate.get().isdigit()==False:
        messagebox.showerror('error','Rate is Alfabet not allowed')
    else:
        dbconfig()
        name = itemName.get()
        types = itemType.get()
        rate = itemRate.get()
        que_insert = "insert into menu_items (Name, Type, Rate) values (%s, %s, %s)"
        val = (name,types,rate)
        mycursor.execute(que_insert, val)
        conn.commit()
        messagebox.showinfo("Success", "Successfully Added Item")
        itemName.set('')
        itemType.set('')
        itemRate.set('')

def update_item():
    if itemName.get()=='' or itemType.get()=='' or itemRate.get()=='':
        messagebox.showerror("Error",'Please enter All Details')
    elif itemRate.get().isdigit()==False:
        messagebox.showerror('error','Rate is Alfabet not allowed')

    else:
        dbconfig()
        name = itemName.get()
        types = itemType.get()
        rate = itemRate.get()
        que_update = "update menu_items set Type = %s, Rate = %s where Name = %s"
        val = (types, rate,name)
        mycursor.execute(que_update, val)
        conn.commit()
        messagebox.showinfo("Success", "Update Item Successfully")
        itemName.set('')
        itemType.set('')
        itemRate.set('')

def delete_item():
    if itemName.get()=='' or itemType.get()=='' or itemRate.get()=='':
        messagebox.showerror("Error",'Please enter All Details')
    elif itemRate.get().isdigit()==False:
        messagebox.showerror('error','Rate is Alfabet not allowed')
    else:
        dbconfig()
        name = itemName.get()
        types = itemType.get()
        rate = itemRate.get()
        que_del = "delete from menu_items where name=%s"
        val = (name)
        mycursor.execute(que_del, val)
        conn.commit()
        messagebox.showinfo("Success", "Successfully Added Item")
        itemName.set('')
        itemType.set('')
        itemRate.set('')



itemName=StringVar()
itemType=StringVar()
itemRate=StringVar()
def manage_restaurant():
    clear_screen()
    main_heading()
    back()
    labelmanage = LabelFrame(taz, text="              Insert Menu Items",font=("ariel", 35, "bold"), bg=c[5], fg="white")
    labelmanage.grid(row=2,rowspan=3, column=0, columnspan=6, padx=0, pady=30)

    item_name_Label=Label(labelmanage ,text="Item Name",justify="left",font=("Eras Bold ITC",25,"bold"),bg=c[5])
    item_name_Label.grid(row=3,column=1,padx=50,pady=5)

    item_type_Label = Label(labelmanage , text="Item Type",font=("Eras Bold ITC",25,"bold"),bg=c[5])
    item_type_Label.grid(row=4, column=1, padx=50, pady=5)

    item_rate_Label = Label(labelmanage , text="Item Price(INR)", font=("Eras Bold ITC", 25, "bold"),bg=c[5])
    item_rate_Label.grid(row=5, column=1, padx=50, pady=5)


    item_name_Entry=Entry(labelmanage ,font=('arial',20,'normal'),textvariable=itemName)
    item_name_Entry.grid(row=3,column=2,padx=30,pady=5)

    item_type_Entry=Entry(labelmanage ,font=('arial',20,'normal'),textvariable=itemType)
    item_type_Entry.grid(row=4, column=2, padx=30, pady=5)

    item_rate_Entry=Entry(labelmanage ,font=('arial',20,'normal'),textvariable=itemRate)
    item_rate_Entry.grid(row=5,column=2,padx=30,pady=5)

    loginButton=Button(labelmanage ,text="Update",font=('Eras Bold ITC',15,'normal'),width=8,fg=c[3],bg='yellow',bd=10,command=update_item)
    loginButton.grid(row=6, column=1,padx=0, pady=10)
    loginButton=Button(labelmanage ,text="Add Item",font=('Eras Bold ITC',15,'normal'),width=8,fg=c[3],bg=c[1],bd=10,command=add_Items)
    loginButton.grid(row=6, column=1,columnspan=3,padx=30, pady=10)
    loginButton=Button(labelmanage ,text="Delete",font=('Eras Bold ITC',15,'normal'),width=8,fg=c[4],bg='#F31C20',bd=10,command=delete_item)
    loginButton.grid(row=6, column=2,padx=30, pady=10)
def bill():
    clear_screen()
    main_heading()
    label_bill = Label(taz, text="Generate Bill", font=("ariel", 30, "bold"), bg="blue", fg="white")
    label_bill.grid(row=1, column=0, columnspan=6, padx=0, pady=30)
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
        flag = False
        for row in data:
            flag = True
        conn.close()

        if flag == True:
            welcomewindow()
        else:
            messagebox.showerror("Invalid User Credential", "Either User Name or Password is Incorrect")
            usernameVar.set("")
            passwordVar.set("")
#main heading
def main_heading():
    label=Label(taz,image=logo,text="Rajput Hotel Management System",fg="red",bg="yellow",font=("comic sans Ms",55,"bold"),padx=250,pady=30)
    label.grid(row=0,columnspan=6)

usernameVar=StringVar()
passwordVar=StringVar()
def loginwindow():
    usernameVar.set("")
    passwordVar.set("")
    labellogin=LabelFrame(taz,text="             Admin Login",font=("ariel",35,"bold"),bg="magenta",fg="white")
    labellogin.grid(row=1, columnspan=6,padx=10,pady=50)

    usernameLabel=Label(labellogin,text="User Name",font=("ariel",25,"bold"),bg='magenta')
    usernameLabel.grid(row=2,column=0,padx=50,pady=20)

    passwordLabel = Label(labellogin, text="User Password",font=("ariel",25,"bold"),bg='magenta')
    passwordLabel.grid(row=3, column=0, padx=20, pady=5)

    usernameEntry=Entry(labellogin,textvariable=usernameVar,font=('arial',20,'normal'))
    usernameEntry.grid(row=2,column=3,padx=20,pady=20)

    passwordEntry=Entry(labellogin,show="•",textvariable=passwordVar,font=('arial',20,'bold'))
    passwordEntry.grid(row=3, column=3, padx=20, pady=5)

    loginButton=Button(labellogin,text="Login",font=('arial',25,'normal'),width=10,fg="white",bg='blue',bd=10,command=adminLogin)
    loginButton.grid(row=4, column=0, columnspan=4,padx=20, pady=30)

# welcome window
def welcomewindow():
    clear_screen()
    main_heading()
    labelwelcome = Label(taz, text=" Welcome Dashboard ",font=("ariel",30,"bold"),bg="blue",fg="white")
    labelwelcome.grid(row=1, column=0, columnspan=6, padx=10, pady=30)

    manage_restaurantButton = Button(taz, text="Manage Restaurant", font=('arial',25,'normal'),width=30, fg="green", bd=10, command=manage_restaurant)
    manage_restaurantButton.grid(row=4, column=0, columnspan=6, padx=10, pady=10)

    bill_Button = Button(taz, text="Generate Bill", font=('arial',25,'normal'),width=30, fg="green", bd=10, command=bill)
    bill_Button.grid(row=5, column=0, columnspan=6, padx=20, pady=10)

    logoutButton = Button(taz, text="Logout", font=('arial',25,'normal'),width=30, fg="white",bg='red', bd=10, command=adminLogout)
    logoutButton.grid(row=6, column=0, columnspan=6, padx=20, pady=10)
main_heading()
loginwindow()
taz.geometry("%dx%d+0+0"%(width,height))
taz.mainloop()