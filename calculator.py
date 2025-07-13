from tkinter import*
r=Tk()
r.title('Rajput Calculator')
 #r.geometry('400x500+100+200')
val=""
def b_input(number):
    global val
    val=val+str(number)
    data.set(val)

def b_clear():
    global val
    val=""
    data.set('')

def b_eqals():
    global val
    result=str(eval(val))
    data.set(result)

data=StringVar()
display=Entry(r,bd=30,textvariable=data,justify='right',bg='powder blue',font=('arial',25,'bold'),)
display.grid(row=0,columnspan=4)

b7=Button(r,text='7',font=('ariel',15,'bold'),bd=12,height=2,width=6,command=lambda:b_input(7))
b7.grid(row=1,column=0)
b8=Button(r,text='8',font=('ariel',15,'bold'),bd=12,height=2,width=6,command=lambda:b_input(8))
b8.grid(row=1,column=1)
b9=Button(r,text='9',font=('ariel',15,'bold'),bd=12,height=2,width=6,command=lambda:b_input(9))
b9.grid(row=1,column=2)
b_add=Button(r,text='+',font=('ariel',15,'bold'),bd=12,height=2,width=6,command=lambda:b_input('+'))
b_add.grid(row=1,column=3)

b4=Button(r,text='4',font=('ariel',15,'bold'),bd=12,height=2,width=6,command=lambda:b_input(4))
b4.grid(row=2,column=0)
b5=Button(r,text='5',font=('ariel',15,'bold'),bd=12,height=2,width=6,command=lambda:b_input(5))
b5.grid(row=2,column=1)
b6=Button(r,text='6',font=('ariel',15,'bold'),bd=12,height=2,width=6,command=lambda:b_input(6))
b6.grid(row=2,column=2)
b_sub=Button(r,text='-',font=('ariel',15,'bold'),bd=12,height=2,width=6,command=lambda:b_input('-'))
b_sub.grid(row=2,column=3)

b1=Button(r,text='1',font=('ariel',15,'bold'),bd=12,height=2,width=6,command=lambda:b_input(1))
b1.grid(row=3,column=0)
b2=Button(r,text='2',font=('ariel',15,'bold'),bd=12,height=2,width=6,command=lambda:b_input(2))
b2.grid(row=3,column=1)
b3=Button(r,text='3',font=('ariel',15,'bold'),bd=12,height=2,width=6,command=lambda:b_input(3))
b3.grid(row=3,column=2)
b_mul=Button(r,text='*',font=('ariel',15,'bold'),bd=12,height=2,width=6,command=lambda:b_input('*'))
b_mul.grid(row=3,column=3)

b_clear=Button(r,text='C',font=('ariel',15,'bold'),bg='red',bd=12,height=2,width=6,command=b_clear)
b_clear.grid(row=4,column=0)
b0=Button(r,text='0',font=('ariel',15,'bold'),bd=12,height=2,width=6,command=lambda:b_input(0))
b0.grid(row=4,column=1)
b_eqal=Button(r,text='=',font=('ariel',15,'bold',),bg='blue',bd=12,height=2,width=6,command=b_eqals)
b_eqal.grid(row=4,column=2)
b_div=Button(r,text='÷',font=('ariel',15,'bold'),bd=12,height=2,width=6,command=lambda:b_input('/'))
b_div.grid(row=4,column=3)
r.mainloop()