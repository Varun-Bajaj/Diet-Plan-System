from tkinter import *
from PIL import Image, ImageTk
'''varun_1=Tk()


varun_1.title("DIET PLAN SYSTEM")
def getsvalue():
    print("name=",namevalue.get())
    print("age=",agevalue.get())
    print("gender=",gendervalue.get())
    print("disease=",diseasevalue.get())
    print("lose weight or gain weight=",optionvalue.get())
    bajaj1 = Label(text=("welcome",namevalue.get()), font=("hindi", 20)).grid(column=2)
    #varun_2=Tk()
    #varun_2.mainloop()
def exit1():
    exit()
optionvalue=StringVar()
def next2():
    vsb=Label(text="do you want to lose weight or gain weight", font=("calibri", 8)).grid(row=9)
    optionentry=Entry(varun_1,textvariable=optionvalue).grid(row=9,column=2)
    #Button(text="next").grid(column=2)
diseasevalue=StringVar()
def next1():
    vb=Label(text="do you have any diseases", font=("calibri", 10)).grid(row=7)
    diseaseentry=Entry(varun_1,textvariable=diseasevalue).grid(row=7,column=2)
    Button(text="next",command=next2).grid(column=2)
#varun_1.geometry("5000x5000")

varun_1.minsize(800,500)


#text - adds the text
# bg - background
# fg - foreground
# padx - x padding
# pady - y padding
# font - sets the font
# releif - border styling - SUNKEN,RAISED,GROOVE,RIDGE

sahil_12 = Label(text="WELCOME TO MY DIET PLAN SYSTEM",bg="black",fg="white",padx=20,pady=20,font=("algerian",13),borderwidth=
                 3,relief=SUNKEN)

sahil_12.grid(column=2)

#krish_m=Label(text="HI, I AM VARUN BAJAJ YOUR DIET PLANNER AND I AM GONNA MAKE YOU HEALTY IN 30 DAYS BY PROVIDING MEALS AND EXERCISES",bg="red",
 #             fg="yellow",font=("calibri",17,"bold"))
#krish_m.grid()
name= Label(varun_1,text="name").grid(row=2)
age= Label(varun_1,text="age").grid(row=3)
gender = Label(varun_1,text="gender").grid(row=4)
vsb=Label(text="lose weight or gain weight").grid(row=5)

namevalue=StringVar()
agevalue=StringVar()
gendervalue=StringVar()
optionvalue=StringVar()
diseasevalue=StringVar()

nameentry = Entry(varun_1,textvariable=namevalue).grid(row=2,column=2)
ageentry = Entry(varun_1,textvariable=agevalue).grid(row=3,column=2)
genderentry = Entry(varun_1,textvariable=gendervalue).grid(row=4,column=2)
optionentry=Entry(varun_1,textvariable=optionvalue).grid(row=9,column=2)
Button(text="next",command=next1).grid(column=2)
Button(text="submit",command=getsvalue).grid(row=2,column=4)
Button(text="EXIT",command=exit1).grid(row=1,column=4)

f1=Frame(varun_1,borderwidth=9).grid()
def name1():
    print("welcome, I am varun bajaj your diet planner")
v1=Button(f1,text="lets start our diet plan",font=("algerian",9,"bold"),fg="blue",command=name1)
v1.grid()

#photo = PhotoImage(file="1.jpg")
image=Image.open("diet plan.jpg")
photo=ImageTk.PhotoImage(image)

sahil_13 = Label(image=photo)
#anchor = n,w,e,s
#side= top,bottom,left,right
#fill
#padx
#pady
sahil_13.grid(row=1)


varun_1.mainloop()'''
