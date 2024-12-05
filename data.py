def getsvalue():
    print("name=",namevalue.get().lower())
    print("age=",agevalue.get().lower())
    print("gender=",gendervalue.get().lower())
    print("lose weight or gain weight=",optionvalue.get().lower())
    print("disease=",diseasevalue.get().lower())
    print("veg or non veg=",vnvvalue.get().lower())
    bajaj1 = Label(text=("welcome",namevalue.get().upper()), font=("hindi", 20)).grid(column=2)
    
def exit1():
    exit()

sahil_12 = Label(text="WELCOME TO MY DIET PLAN SYSTEM",bg="black",fg="white",padx=20,pady=20,font=("algerian",13),borderwidth=
                 3,relief=SUNKEN)

sahil_12.grid(column=2)

namevalue=StringVar()
agevalue=StringVar()
gendervalue=StringVar()
optionvalue=StringVar()
diseasevalue=StringVar()
vnvvalue=StringVar()

name= Label(top,text="name",font=("calibri",10)).grid(row=2)
age= Label(top,text="age",font=("calibri",10)).grid(row=3)
gender = Label(top,text="gender",font=("calibri",10)).grid(row=4)
vsb=Label(text="lose weight or gain weight",font=("calibri",10)).grid(row=5)
vb=Label(text="do you have any diseases", font=("calibri", 10)).grid(row=6)
vnv=Label(text="veg or non veg",font=("calibri",10)).grid(row=7)

namevalue=StringVar()
agevalue=StringVar()
gendervalue=StringVar()
optionvalue=StringVar()
diseasevalue=StringVar()
vnvvalue=StringVar()

def myfunc():
    tmsg.askquestion("reveiw","was your experience good?")

nameentry = Entry(top,textvariable=namevalue).grid(row=2,column=2)
ageentry = Entry(top,textvariable=agevalue).grid(row=3,column=2)
genderentry = Entry(top,textvariable=gendervalue).grid(row=4,column=2)
optionentry=Entry(top,textvariable=optionvalue).grid(row=5,column=2)
diseaseentry=Entry(top,textvariable=diseasevalue).grid(row=6,column=2)
vnventry=Entry(top,textvariable=vnvvalue).grid(row=7,column=2)
Button(text="submit", command=open_toplevel).grid(row=8, column=2)
Button(text="EXIT", command=exit1).grid(row=1, column=4)

mainmenu=Menu(top)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="review",command=myfunc)
m1.add_command(label="complain")
m1.add_command(label="suggestion")
top.config(menu=mainmenu)
mainmenu.add_cascade(label="feedback",menu=m1)
top.mainloop()
