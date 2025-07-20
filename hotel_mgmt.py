from tkinter import *
from tkinter import messagebox, StringVar,ttk,filedialog
from PIL import ImageTk, Image
from datetime import datetime
import pymysql

taz=Tk()
taz.title('Taz Hotel')
height=taz.winfo_screenheight()
width=taz.winfo_screenwidth()
c=['#F31C20','#1CF31F','#FFE54A','black','white','#a85a31','#D17DF3','red','cyan','#c8d9b0',"magenta",'#b3c677','#9514D2']
taz.config(bg=c[9])
logo=ImageTk.PhotoImage(Image.open(r'C:\Users\Aniket\Downloads\Screenshot 2025-07-16 214243.png'))


def only_char_input(G):
    if G.isalpha() or G=='':
        return True
    return False
callback=taz.register(only_char_input)


def only_numeric_input(G):
    if G.isdigit() or G=='':
        return True
    return False
callback1=taz.register(only_numeric_input)

h_tv=ttk.Treeview(height=10,columns=('Name''Type','Rate'))
h_tv1=ttk.Treeview(height=5,columns=('' '','','',''))
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

#################### OnDoubleClick ####################
def OnDoubleClick(event):
    item=h_tv.selection()
    itemNameVar1=h_tv.item(item,'text')
    item_detail = h_tv.item(item,'values')
    itemName.set(itemNameVar1)
    itemRate.set(item_detail[1])
    itemType.set(item_detail[0])
#########################################################

def getItemInTreeview():
    # to delete already inserted data
    records=h_tv.get_children()
    for x in records:
        h_tv.delete(x)
    conn=pymysql.connect(host="localhost",user="root",db="rajput_hotel")
    mycursor=conn.cursor(pymysql.cursors.DictCursor)
    query1="select * from menu_items"
    mycursor.execute(query1)
    data=mycursor.fetchall()
    # print(data)
    for row in data:
        h_tv.insert('','end',text=row['Name'],values=(row["Type"],row['Rate'],))
    conn.close()
    h_tv.bind("<Double-1>",OnDoubleClick)

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
        getItemInTreeview()

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
        getItemInTreeview()

def delete_item():
    if itemName.get()=='' or itemType.get()=='' or itemRate.get()=='':
        messagebox.showerror("Error",'Please enter All Details')
    else:
        dbconfig()
        name = itemName.get()
        types = itemType.get()
        rate = itemRate.get()
        que_del = "delete from menu_items where name=%s"
        val = (name)
        mycursor.execute(que_del, val)
        conn.commit()
        messagebox.showinfo("Success", "Item Delete Successfully")
        itemName.set('')
        itemType.set('')
        itemRate.set('')
        getItemInTreeview()


itemName=StringVar()
itemType=StringVar()
itemRate=StringVar()
def manage_restaurant():
    clear_screen()
    main_heading()
    back()
    labelmanage = LabelFrame(taz, text="              Insert Menu Items",font=("ariel", 35, "bold"), bg=c[5], fg="white")
    labelmanage.grid(row=2,rowspan=3, column=0, columnspan=6, padx=0, pady=10)

    item_name_Label=Label(labelmanage ,text="Item Name",justify="left",font=("Eras Bold ITC",25,"bold"),bg=c[5])
    item_name_Label.grid(row=3,column=1,padx=30,pady=5)

    item_type_Label = Label(labelmanage , text="Item Type",font=("Eras Bold ITC",25,"bold"),bg=c[5])
    item_type_Label.grid(row=4, column=1, padx=50, pady=5)

    item_rate_Label = Label(labelmanage , text="Item Price(INR)", font=("Eras Bold ITC", 25, "bold"),bg=c[5])
    item_rate_Label.grid(row=5, column=1, padx=50, pady=5)


    item_name_Entry=Entry(labelmanage ,font=('arial',20,'normal'),textvariable=itemName)
    item_name_Entry.configure(validate="key", validatecommand=(callback, "%P"))
    item_name_Entry.grid(row=3,column=2,padx=30,pady=5)

    item_type_Entry=Entry(labelmanage ,font=('arial',20,'normal'),textvariable=itemType)
    item_type_Entry.grid(row=4, column=2, padx=30, pady=5)

    item_rate_Entry=Entry(labelmanage ,font=('arial',20,'normal'),textvariable=itemRate)
    item_rate_Entry.configure(validate="key", validatecommand=(callback1, "%P"))
    item_rate_Entry.grid(row=5,column=2,padx=30,pady=5)

    loginButton=Button(labelmanage ,text="Update",font=('Eras Bold ITC',15,'normal'),width=8,fg=c[3],bg='yellow',bd=10,command=update_item)
    loginButton.grid(row=6, column=1,padx=0, pady=10)
    loginButton=Button(labelmanage ,text="Add Item",font=('Eras Bold ITC',15,'normal'),width=8,fg=c[3],bg=c[1],bd=10,command=add_Items)
    loginButton.grid(row=6, column=1,columnspan=3,padx=30, pady=10)
    loginButton=Button(labelmanage ,text="Delete",font=('Eras Bold ITC',15,'normal'),width=8,fg=c[4],bg='#F31C20',bd=10,command=delete_item)
    loginButton.grid(row=6, column=2,padx=30, pady=10)

#####################  Treeviwe ###############
    h_tv.grid(row=7,column=1,columnspan=4,padx=0, pady=10)
    style = ttk.Style(taz)
    style.theme_use('clam')
    style.configure('Treeview',background='#b3c677',bg=c[2],fieldbackground=c[4])
    tv_scrool1=Scrollbar(taz,orient='vertical',command=h_tv.yview)
    tv_scrool1.grid(row=7,column=4,pady=12,padx=10,sticky='ns')
    h_tv.configure(yscrollcommand=tv_scrool1.set)
    h_tv.heading('#0',text='Item Name',anchor='center')
    h_tv.heading('#1',text='Item Type',anchor='center')
    h_tv.heading('#2',text='Item Price',anchor='center')
    getItemInTreeview()

############### Combo Data ##############
def combo_input():
    dbconfig()
    mycursor.execute('select Name from menu_items')
    datas=[]
    for row in mycursor.fetchall():
        datas.append(row[0])
    return datas

######################   optionCallback  ##################
def optionCallback(*args):
    global item_name
    item_name=itemnamevar.get()
    aa=rateList()
    item_Rate.set(aa)
    global v
    for i in aa:
        for j in i:
            v=j
    # item_Rate.set(v)
############### ratelist ##########
def rateList():
    dbconfig()
    que_rate = "select Rate from menu_items where Name=%s"
    val = (item_name)
    mycursor.execute(que_rate,val)
    da=mycursor.fetchall()
    # print(da)
    return da
############# optionCallback1 #############
def optionCallback1(*args):
    global item_qty
    item_qty=itemqtyvar.get()
    final=int(v)*int(item_qty)
    cast.set(final)


def save():
    if dateTime.get()=='' or cust_Name.get()=='' or con_No.get()=='' or itemnamevar.get()==''or item_Rate.get()=='' or itemqtyvar.get()==''or cast.get()=='':
        messagebox.showerror("Error",'Please enter All Details')
    else:
        dbconfig()
        dt = dateTime.get()
        c_n = cust_Name.get()
        c_no = con_No.get()
        i_na = itemnamevar.get()
        i_ra = v
        i_qt = itemqtyvar.get()
        t_p = cast.get()
        # print(dt,c_n,c_no,i_na,i_ra,i_qt,t_p)
        que_i = "insert into g_bill (Date_Time,	Cust_Name,	Cust_m_No,	Item_Name,	Item_Rate,	Item_Qty,Total) values (%s, %s, %s,%s, %s, %s, %s)"
        val = (dt,c_n,c_no,i_na,i_ra,i_qt,t_p)
        mycursor.execute(que_i, val)
        conn.commit()
        messagebox.showinfo("Success", "Successfully Added Item")
        dateTime.set(dt)
        cust_Name.set('')
        con_No.set('')
        itemnamevar.set('Select Item')
        item_Rate.set('')
        # itemqtyvar.set('Select Quty')
        cast.set('')
def print_sc():
    clear_screen()
    main_heading()
    back_Button = Button(taz, text="Back", font=('arial', 25, 'bold'), fg="white",bg='blue', bd=10, command=bill)
    back_Button.grid(row=1, column=0, padx=5, pady=5)

    logoutButton = Button(taz, text="Logout", font=('arial',25,'bold'), fg="white", bg='red',bd=10, command=adminLogout)
    logoutButton.grid(row=1 ,column=4)

    # labelprint=Frame(taz,bg='blue',bd=10,)
    # labelprint.grid(row=2,rowspan=4, column=0, padx=500, pady=100)
    labelprint1 = Label(taz, text="Bill Detail", font=("ariel", 35, "bold"),bg=c[9])
    labelprint1.grid(row=1,column=1, columnspan=3, padx=0, pady=10)

    labelprint1 = Label(taz, text="Double click on Treeview to Print Bill", font=("ariel", 15, "bold"),bg=c[9], fg=c[7])
    labelprint1.grid(row=2,column=1, columnspan=3, padx=0, pady=10)

    h_tv1.grid(row=3,column=1,padx=80, pady=0)
    style = ttk.Style(taz)
    style.theme_use('clam')
    style.configure('Treeview',background='yellow',bg=c[2],fieldbackground=c[5])
    tv_scrool2=Scrollbar(taz,orient='vertical',command=h_tv1.xview)
    tv_scrool2.grid(row=3,column=2,sticky='ns')

    h_tv1.configure(yscrollcommand=tv_scrool2.set)
    h_tv1.heading('#0',text='Date & Time')
    h_tv1.heading('#1',text='Name',anchor='center')
    h_tv1.heading('#2',text='Mobile No.',anchor='center')
    h_tv1.heading('#3',text='Selected Food',anchor='center')
    # h_tv1.heading('#4',text='Item Rate & Qty',anchor='center')
    h_tv1.heading('#4',text='Total Cost',anchor='center')

    records=h_tv1.get_children()
    for x in records:
        h_tv1.delete(x)
    conn=pymysql.connect(host="localhost",user="root",db="rajput_hotel")
    mycursor=conn.cursor(pymysql.cursors.DictCursor)
    query2="select * from g_bill"
    mycursor.execute(query2)
    data=mycursor.fetchall()
    # print(data)
    for row in data:
        h_tv1.insert('','end',text=row['Date_Time'],values=(row["Cust_Name"],row['Cust_m_No'],row['Item_Name'],row['Total']))
    conn.close()
    h_tv1.bind("<Double-1>",OnDoubleClick1)

#################### OnDoubleClick ####################
def OnDoubleClick1(event):
    item=h_tv1.selection()
    global itemNameVar2
    itemNameVar2=h_tv1.item(item,'text')
    item_detail1 = h_tv1.item(item,'values')
    receipt()

################### receipt() ##################
def receipt():
    bill_String=''
    bill_String+='====================== Rajput Hotel =====================\n\n'
    bill_String +='==================== Customer Detail ====================\n\n'

    dbconfig()
    billqury= "select * from g_bill where Date_Time = '{}';".format(itemNameVar2)
    mycursor.execute(billqury)
    data1=mycursor.fetchall()
    for row in data1:
        bill_String+="{}{:<19}{:5}\n".format("Date/Time :-"," ",row[1])
        bill_String += "{}{:15}{:20}\n".format("Customer Name :-", " ", row[2])
        bill_String += "{}{:<17}{:10}\n".format("Contact No :- ", " ", row[3])
        bill_String += '\n====================== Item Detail ======================\n'
        bill_String += "{:<19}{:<13}{:<15}{:<18}".format("Item Name", "Rate","Quantity","Total Cost")
        bill_String += "\n{:<19}{:<13}{:<15}{:<18}".format(row[4], row[5],row[6],row[7])
        bill_String += "\n========================================================="
        bill_String += "\n{:<15}{:<15}{:<10}\n".format(""," Total Cost=",row[7])
        bill_String += "\n******************** Thank You **************************"
        bill_String += "\n\n**************** Please Visit Again *********************"

    bill_File =filedialog.asksaveasfile(mode='w', defaultextension=".txt",filetypes=(('Text Files', '*.txt'),))
    if bill_File is None:
        messagebox.showerror("Error", "No file selected")
    else:
        bill_File.write(bill_String)
        bill_File.close()
        mycursor.close()
        messagebox.showinfo("Success", "Rajput Hotel Bill Saved")

########################################################################################

dateTime=StringVar()
dateTime.set(datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
cust_Name=StringVar()
con_No=StringVar()
item_Rate=StringVar()
itemqtyvar=StringVar()
itemnamevar=StringVar()
cast=StringVar()
def bill():
    clear_screen()
    main_heading()
    back()
    labelbill = LabelFrame(taz, text="                   Generate Bill", font=("ariel", 35, "bold"), bg=c[12],
                             fg="white")
    labelbill.grid(row=2,rowspan=4, column=0, columnspan=6, padx=0, pady=10)

    dateTime_Lable = Label(labelbill, text="Date & Time", justify="left", font=("Eras Bold ITC", 25, "bold"), bg=c[12])
    dateTime_Lable.grid(row=3, column=1, padx=30, pady=5)

    cu_Name_Label = Label(labelbill, text="Customer Name", font=("Eras Bold ITC", 25, "bold"), bg=c[12])
    cu_Name_Label.grid(row=4, column=1, padx=50, pady=5)

    co_no_Label = Label(labelbill, text="Contact No.", font=("Eras Bold ITC", 25, "bold"), bg=c[12])
    co_no_Label.grid(row=5, column=1, padx=50, pady=5)

    i_name_Label = Label(labelbill, text="Select Item Name", justify="left", font=("Eras Bold ITC", 25, "bold"), bg=c[12])
    i_name_Label.grid(row=6, column=1, padx=30, pady=5)

    i_rate_Label = Label(labelbill, text="Item Price", font=("Eras Bold ITC", 25, "bold"), bg=c[12])
    i_rate_Label.grid(row=7, column=1, padx=50, pady=5)

    item_qt_Label = Label(labelbill, text="Item Qt.", font=("Eras Bold ITC", 25, "bold"), bg=c[12])
    item_qt_Label.grid(row=8, column=1, padx=50, pady=5)

    i_rate_Label = Label(labelbill, text="Total Price", font=("Eras Bold ITC", 25, "bold"), bg=c[12])
    i_rate_Label.grid(row=9, column=1, padx=50, pady=5)

    dateTime_Entry=Entry(labelbill ,font=('arial',20,'normal'),textvariable=dateTime)
    dateTime_Entry.configure(validate="key", validatecommand=(callback1, "%P"))
    dateTime_Entry.grid(row=3,column=2,padx=30,pady=5)

    cu_Name_Entry=Entry(labelbill ,font=('arial',20,'normal'),textvariable=cust_Name)
    cu_Name_Entry.configure(validate="key", validatecommand=(callback, "%P"))
    cu_Name_Entry.grid(row=4, column=2, padx=30, pady=5)

    co_no_Entry=Entry(labelbill,font=('arial',20,'normal'),textvariable=con_No)
    co_no_Entry.configure(validate="key", validatecommand=(callback1, "%P"))
    co_no_Entry.grid(row=5,column=2,padx=30,pady=5)

    i=combo_input()
    i_name=ttk.Combobox(labelbill,font=('arial',19,'normal'),values=i,textvariable=itemnamevar)
    i_name.set('Select Item')
    itemnamevar.trace('w', optionCallback)
    i_name.grid(row=6,column=2,padx=30,pady=5)


    item_rate_Entry=Entry(labelbill ,font=('arial',20,'normal'),textvariable=item_Rate)
    item_rate_Entry.grid(row=7,column=2,padx=30,pady=5)

    l=[1,2,3,4,5]
    item_qt=ttk.Combobox(labelbill,font=('arial',19,'normal'),values=l,textvariable=itemqtyvar)
    item_qt.set('Select Quty')
    item_qt.set('Select Quty')
    itemqtyvar.trace('w', optionCallback1)
    item_qt.grid(row=8,column=2,padx=30,pady=5)

    total_cost_Entry = Entry(labelbill, font=('arial', 20, 'normal'), textvariable=cast)
    total_cost_Entry.grid(row=9, column=2, padx=30, pady=5)

    saveButton = Button(labelbill, text="Save", font=('Eras Bold ITC', 15, 'normal'), width=8, fg=c[3], bg=c[1],
                         bd=10, command=save)
    saveButton.grid(row=10, column=1, columnspan=3, padx=30, pady=10)

    saveButton = Button(labelbill, text="Print Bill", font=('Eras Bold ITC', 15, 'normal'), width=8, fg=c[3], bg=c[2],
                        bd=10, command=print_sc)
    saveButton.grid(row=10, column=2, columnspan=3, padx=30, pady=10)


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
    label=Label(taz,image=logo,fg="red",bg="yellow",font=("comic sans Ms",55,"bold"),padx=250,pady=30)
    label.grid(row=0,columnspan=6)

usernameVar=StringVar()
passwordVar=StringVar()
def loginwindow():
    usernameVar.set("")
    passwordVar.set("")
    labellogin=LabelFrame(taz,text="             Admin Login",font=("ariel",35,"bold"),bg=c[10],fg='white')
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

    manage_restaurantButton = Button(taz, text="Manage Restaurant", font=('arial',25,'normal'),width=30,bg=c[5] ,fg=c[4], bd=10, command=manage_restaurant)
    manage_restaurantButton.grid(row=4, column=0, columnspan=6, padx=10, pady=10)

    bill_Button = Button(taz, text="Generate Bill", font=('arial',25,'normal'),width=30,bg=c[12], fg=c[4], bd=10, command=bill)
    bill_Button.grid(row=5, column=0, columnspan=6, padx=20, pady=10)

    logoutButton = Button(taz, text="Logout", font=('arial',25,'normal'),width=30, fg="white",bg='red', bd=10, command=adminLogout)
    logoutButton.grid(row=6, column=0, columnspan=6, padx=20, pady=10)
main_heading()
loginwindow()
taz.geometry("%dx%d+0+0"%(width,height))
taz.mainloop()