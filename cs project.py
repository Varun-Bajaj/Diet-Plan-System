from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.ttk import Combobox
from tkinter.ttk import Progressbar
from tkinter.filedialog import asksaveasfile
import mysql.connector as con
import time
import pickle
from trial import *
from PIL import Image, ImageTk

def task():
    
    time.sleep(3) 
    root.destroy()

root = Tk()
root.configure(bg= '#F4A460')
root.geometry("1100x670")

# Create a photoimage object of the image in the path
image1v = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\1.jpg")
testv = ImageTk.PhotoImage(image1v)

label1v = Label(image=testv)
label1v.image = testv

# Position image
label1v.place(x=0, y=0)
root.after(200, task)
root.mainloop()

mydb=con.connect(host='localhost',database='cs_project',user='root',password='mouse@2010')
cur=mydb.cursor()
varun_1=Tk()

varun_1.minsize(800,500)
varun_1.configure(bg='#F4A460')
varun_1.title("DIET PLAN SYSTEM")

def exit1():
    exit()

#
def open_toplevel():
    varun_1.destroy()
    top=Tk()
    top.configure(bg="#F4A460")
    top.title("DIET PLAN SYSTEM")
    top.minsize(800,500)
    def getsvalue():
        
        print("name=",namevalue.get().lower())
        print("age=",agevalue.get().lower())
        print("gender=",gendervalue.get().lower())
        print("lose weight or gain weight=",optionvalue.get().lower())
        print("disease=",diseasevalue.get().lower())
        print("veg or non veg=",vnvvalue.get().lower())
        
        bajaj1 = Label(text=("welcome",namevalue.get().upper()), font=("hindi", 20))
        bajaj1.grid(column=2)
    
    def exit1():
        exit()

    sahil_12 = Label(top,text="WELCOME TO MY DIET PLAN SYSTEM",bg="black",fg="white",padx=20,pady=20,font=("times",13),borderwidth=
                     3,relief=SUNKEN)
    sahil_12.grid(column=2)


    name= Label(top,text="name",font=("italic",15))
    name.grid(row=2)
    
    name1= Label(top,text="",font=("italic",10))
    name1.grid(row=3)
    
    age= Label(top,text="age",font=("italic",15))
    age.grid(row=4)
    
    name2= Label(top,text="",font=("italic",10))
    name2.grid(row=5)
    
    gender = Label(top,text="gender",font=("italic",15))
    gender.grid(row=6)
    
    name3= Label(top,text="",font=("italic",10))
    name3.grid(row=7)
    
    vsb=Label(top,text="lose weight or gain weight",font=("italic",15))
    vsb.grid(row=8)
    
    name4= Label(top,text="",font=("italic",10))
    name4.grid(row=9)
    
    vb=Label(top,text="do you have any diseases", font=("italic", 15))
    vb.grid(row=10)
    
    name5= Label(top,text="",font=("italic",10))
    name5.grid(row=11)
    
    vnv=Label(top,text="veg/non-veg/vegan",font=("italic",15))
    vnv.grid(row=12)

    format1=Label(top,text="pls follow above format",font=("italic",10))
    format1.grid(row=13)

    def myfunc():
        tmsg.askquestion("reveiw","was your experience good?")

    namevalue=StringVar()
    agevalue=IntVar()
    gendervalue=StringVar()
    optionvalue=StringVar()
    diseasevalue=StringVar()
    vnvvalue=StringVar()

    nameentry = Entry(top,textvariable=namevalue)
    nameentry.grid(row=2,column=2)
    
    ageentry = Entry(top,textvariable=agevalue)
    ageentry.grid(row=4,column=2)
    
    genderentry = Combobox(top,textvariable=gendervalue,values=['Male','Female'],font=("italic",10),state='r')
    genderentry.grid(row=6,column=2)
    
    optionentry=Combobox(top,textvariable=optionvalue,values=['Gain','Lose'],font=("italic",10),state='r')
    optionentry.grid(row=8,column=2)
    
    diseaseentry=Combobox(top,textvariable=diseasevalue,values=['diabetes','blood pressure','thyroid','other','nothing'],font=("italic",10),state='r')
    diseaseentry.grid(row=10,column=2)
    
    vnventry=Entry(top,textvariable=vnvvalue)
    vnventry.grid(row=12,column=2)

    def clear_text():
        nameentry.delete(0, END)
        ageentry.delete(0, END)
        genderentry.set('')
        optionentry.set('')
        diseaseentry.set('')
        vnventry.delete(0,END)
        
        
    clear_button=Button(top, text="Clear",command=clear_text,font=("italic",15))
    clear_button.grid(row=13,column=3)
    
    def data():
        f1=open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\project.bin",'ab')
        data1=[namevalue.get(),agevalue.get(),gendervalue.get(),optionvalue.get(),diseasevalue.get(),vnvvalue.get()]
        pickle.dump(data1,f1)
        f1.close()
        v=namevalue.get()
        a=agevalue.get()
        r=gendervalue.get()
        u=optionvalue.get()
        n=diseasevalue.get()
        vb=vnvvalue.get()
        b="insert into data2(name,age,gender,weight,diseases,vnv) values(%s,%s,%s,%s,%s,%s)"
        g=[v,a,r,u,n,vb]
        cur.execute(b,g)
        cur.execute("commit")
        
    def open_top_toplevel():
        top_1=Tk()
        top_1.title("YOUR DIET PLAN")
        top_1.configure(bg="#F4A460")
        top_1.minsize(1200,1200)
        
        #frame.configure(yscrollcommand=y_scroll.set)
        
        if(optionvalue.get()=="Lose" and diseasevalue.get() in ("diabetes", "other","nothing") and vnvvalue.get().lower() in ("veg","vegan")):
            head1=Label(top_1,text="EAT MORE",bg="black",fg="white",padx=20,pady=20,font=("times",13),borderwidth=3,relief=SUNKEN)
            head1.grid(row=1,column=2)

            yash1=Label(top_1,text="1)-------SOY BEANS AND TOFU-->",font=("italic",15))
            yash1.grid(row=2,column=1)
            
            image1 = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\pictures\weight loss--diabetes--veg\soy beans and tofu.jpeg")
            resize_image1 = image1.resize((200, 200))
            img1 = ImageTk.PhotoImage(resize_image1)
            label1 = Label(top_1,image=img1)
            label1.image = img1
            label1.grid(row=2,column=3)

            yash2=Label(top_1,text="2)-------OLIVE OIL-->",font=("italic",15))
            yash2.grid(row=3,column=1)

            image2 = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\pictures\weight loss--diabetes--veg\olive oil.jpeg")
            resize_image2 = image2.resize((200, 200))
            img2 = ImageTk.PhotoImage(resize_image2)
            label2 = Label(top_1,image=img2)
            label2.image = img2
            label2.grid(row=3,column=3)

            yash3=Label(top_1,text="3)-------NUTS AND SEEDS-->",font=("italic",15))
            yash3.grid(row=4,column=1)

            image3 = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\pictures\weight loss--diabetes--veg\nuts and seeds.jpeg")
            resize_image3 = image3.resize((200, 200))
            img3 = ImageTk.PhotoImage(resize_image3)
            label3 = Label(top_1,image=img3)
            label3.image = img3
            label3.grid(row=4,column=3)

            head2=Label(top_1,text="EAT LESS",bg="black",fg="white",padx=20,pady=20,font=("times",13),borderwidth=3,relief=SUNKEN)
            head2.grid(row=1,column=5)

            yash4=Label(top_1,text="1)-------BREAD-->",font=("italic",15))
            yash4.grid(row=2,column=4)

            image4 = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\pictures\weight loss--diabetes--veg\bread.jpeg")
            resize_image4 = image4.resize((200, 200))
            img4 = ImageTk.PhotoImage(resize_image4)
            label4 = Label(top_1,image=img4)
            label4.image = img4
            label4.grid(row=2,column=6)

            yash5=Label(top_1,text="2)-------WHITE RICE-->",font=("italic",15))
            yash5.grid(row=3,column=4)

            image5 = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\pictures\weight loss--diabetes--veg\white rice.jpeg")
            resize_image5 = image5.resize((200, 200))
            img5 = ImageTk.PhotoImage(resize_image5)
            label5 = Label(top_1,image=img5)
            label5.image = img5
            label5.grid(row=3,column=6)

            yash6=Label(top_1,text="3)-------POTATOES-->",font=("italic",15))
            yash6.grid(row=4,column=4)

            image6 = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\pictures\weight loss--diabetes--veg\potatoes.jpeg")
            resize_image6 = image6.resize((200, 200))
            img6 = ImageTk.PhotoImage(resize_image6)
            label6 = Label(top_1,image=img6)
            label6.image = img6
            label6.grid(row=4,column=6)

            def save():
                files = [('All Files', '*.*'),
                         ('Python Files', '*.py'),
                         ('Text Document', '*.txt')]
                file = asksaveasfile(filetypes = files, defaultextension = files)

            blank=Label(top_1,text="")
            blank.grid(row=5,column=3)
            
            save_button=Button(top_1,text="SAVE", command=save)
            save_button.grid(row=6,column=3)
            #Exit_button=Button(top_1,text="EXIT",command=top_1.destroy)
            #Exit_button.grid()
            top_1.mainloop()

        elif(optionvalue.get()=="Gain" and diseasevalue.get() in ("diabetes", "other","nothing") and vnvvalue.get().lower() in ("veg","vegan")):
            head3=Label(top_1,text="YOU SHOULD EAT",bg="black",fg="white",padx=20,pady=20,font=("times",13),borderwidth=3,relief=SUNKEN)
            head3.grid(row=1,column=2)
            
            yash7=Label(top_1,text="1)-------AVOCADO OIL-->",font=("italic",15))
            yash7.grid(row=2,column=1)
            
            image7 = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\pictures\weight gain--diabetes--veg\avocado oil.jpeg")
            resize_image7 = image7.resize((200, 200))
            img7 = ImageTk.PhotoImage(resize_image7)
            label7 = Label(top_1,image=img7)
            label7.image = img7
            label7.grid(row=2,column=3)

            yash8=Label(top_1,text="2)-------GRANOLA-->",font=("italic",15))
            yash8.grid(row=3,column=1)
            
            image8 = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\pictures\weight gain--diabetes--veg\granola.jpeg")
            resize_image8 = image8.resize((200, 200))
            img8 = ImageTk.PhotoImage(resize_image8)
            label8 = Label(top_1,image=img8)
            label8.image = img8
            label8.grid(row=3,column=3)

            yash9=Label(top_1,text="3)-------PUMPKIN SEEDS-->",font=("italic",15))
            yash9.grid(row=4,column=1)
            
            image9 = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\pictures\pumpkin seeds.jpeg")
            resize_image9 = image9.resize((200, 200))
            img9 = ImageTk.PhotoImage(resize_image9)
            label9 = Label(top_1,image=img9)
            label9.image = img9
            label9.grid(row=4,column=3)

            yash9=Label(top_1,text="4)-------PULSES AND PEAS-->",font=("italic",15))
            yash9.grid(row=2,column=4)
            
            image9 = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\pictures\weight gain--diabetes--veg\pulses and peas.jpeg")
            resize_image9 = image9.resize((200, 200))
            img9 = ImageTk.PhotoImage(resize_image9)
            label9 = Label(top_1,image=img9)
            label9.image = img9
            label9.grid(row=2,column=6)

            def save1():
                files = [('All Files', '*.*'),
                         ('Python Files', '*.py'),
                         ('Text Document', '*.txt')]
                file = asksaveasfile(filetypes = files, defaultextension = files)

            blank=Label(top_1,text="")
            blank.grid(row=5,column=3)
            
            save_button=Button(top_1,text="SAVE", command=save1)
            save_button.grid(row=6,column=3)

        elif(optionvalue.get()=="Gain" and diseasevalue.get() in ("diabetes", "other","nothing","thyroid") and vnvvalue.get().lower()=="non-veg"):
            head3=Label(top_1,text="YOU SHOULD EAT",bg="black",fg="white",padx=20,pady=20,font=("times",13),borderwidth=3,relief=SUNKEN)
            head3.grid(row=1,column=2)
            
            yash7=Label(top_1,text="1)-------BOILED EGGS-->",font=("italic",15))
            yash7.grid(row=2,column=1)
            
            image7 = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\pictures\gain--diabetes--non_veg\boiled eggs.jpeg")
            resize_image7 = image7.resize((200, 200))
            img7 = ImageTk.PhotoImage(resize_image7)
            label7 = Label(top_1,image=img7)
            label7.image = img7
            label7.grid(row=2,column=3)

            yash8=Label(top_1,text="2)-------RED MEAT-->",font=("italic",15))
            yash8.grid(row=3,column=1)
            
            image8 = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\pictures\gain--diabetes--non_veg\RED MEAT.jpeg")
            resize_image8 = image8.resize((200, 200))
            img8 = ImageTk.PhotoImage(resize_image8)
            label8 = Label(top_1,image=img8)
            label8.image = img8
            label8.grid(row=3,column=3)

            yash9=Label(top_1,text="3)-------FISH(salmon,tuna,shrimps)-->",font=("italic",15))
            yash9.grid(row=4,column=1)
            
            image9 = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\pictures\gain--diabetes--non_veg\fish.jpeg")
            resize_image9 = image9.resize((200, 200))
            img9 = ImageTk.PhotoImage(resize_image9)
            label9 = Label(top_1,image=img9)
            label9.image = img9
            label9.grid(row=4,column=3)

            yash9=Label(top_1,text="4)-------PRAWNS-->",font=("italic",15))
            yash9.grid(row=2,column=4)
            
            image9 = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\pictures\gain--diabetes--non_veg\PRAWNS.jpeg")
            resize_image9 = image9.resize((200, 200))
            img9 = ImageTk.PhotoImage(resize_image9)
            label9 = Label(top_1,image=img9)
            label9.image = img9
            label9.grid(row=2,column=6)

            def save1():
                files = [('All Files', '*.*'),
                         ('Python Files', '*.py'),
                         ('Text Document', '*.txt')]
                file = asksaveasfile(filetypes = files, defaultextension = files)

            blank=Label(top_1,text="")
            blank.grid(row=5,column=3)
            
            save_button=Button(top_1,text="SAVE", command=save1)
            save_button.grid(row=6,column=3)

        elif(optionvalue.get()=="Gain" and diseasevalue.get()=="blood pressure" and vnvvalue.get().lower() in ("veg","vegan")):
            head3=Label(top_1,text="YOU SHOULD EAT",bg="black",fg="white",padx=20,pady=20,font=("times",13),borderwidth=3,relief=SUNKEN)
            head3.grid(row=1,column=2)
            
            yash7=Label(top_1,text="1)-------WALNUTS-->",font=("italic",15))
            yash7.grid(row=2,column=1)
            
            image7 = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\pictures\walnuts.jpeg")
            resize_image7 = image7.resize((200, 200))
            img7 = ImageTk.PhotoImage(resize_image7)
            label7 = Label(top_1,image=img7)
            label7.image = img7
            label7.grid(row=2,column=3)

            yash8=Label(top_1,text="2)-------COCONUT CREAM-->",font=("italic",15))
            yash8.grid(row=3,column=1)
            
            image8 = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\pictures\coconut milk.jpeg")
            resize_image8 = image8.resize((200, 200))
            img8 = ImageTk.PhotoImage(resize_image8)
            label8 = Label(top_1,image=img8)
            label8.image = img8
            label8.grid(row=3,column=3)

            yash9=Label(top_1,text="3)-------DATES-->",font=("italic",15))
            yash9.grid(row=4,column=1)
            
            image9 = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\pictures\dates.jpeg")
            resize_image9 = image9.resize((200, 200))
            img9 = ImageTk.PhotoImage(resize_image9)
            label9 = Label(top_1,image=img9)
            label9.image = img9
            label9.grid(row=4,column=3)

            yash9=Label(top_1,text="4)-------PEANUT BUTTER-->",font=("italic",15))
            yash9.grid(row=2,column=4)
            
            image9 = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\pictures\peanut butter.jpeg")
            resize_image9 = image9.resize((200, 200))
            img9 = ImageTk.PhotoImage(resize_image9)
            label9 = Label(top_1,image=img9)
            label9.image = img9
            label9.grid(row=2,column=6)

            def save1():
                files = [('All Files', '*.*'),
                         ('Python Files', '*.py'),
                         ('Text Document', '*.txt')]
                file = asksaveasfile(filetypes = files, defaultextension = files)

            blank=Label(top_1,text="")
            blank.grid(row=5,column=3)
            
            save_button=Button(top_1,text="SAVE", command=save1)
            save_button.grid(row=6,column=3)

        elif(optionvalue.get()=="Lose" and diseasevalue.get() in ("blood pressure" , "thyroid") and vnvvalue.get().lower() in ("veg","vegan")):
            head3=Label(top_1,text="YOU SHOULD EAT",bg="black",fg="white",padx=20,pady=20,font=("times",13),borderwidth=3,relief=SUNKEN)
            head3.grid(row=1,column=2)
            
            yash7=Label(top_1,text="1)-------COOKED CEREALS-->",font=("italic",15))
            yash7.grid(row=2,column=1)
            
            image7 = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\pictures\cooked cereals.jpeg")
            resize_image7 = image7.resize((200, 200))
            img7 = ImageTk.PhotoImage(resize_image7)
            label7 = Label(top_1,image=img7)
            label7.image = img7
            label7.grid(row=2,column=3)

            yash8=Label(top_1,text="2)-------VEGETABLE JUICE-->",font=("italic",15))
            yash8.grid(row=3,column=1)
            
            image8 = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\pictures\vegetable juice.jpeg")
            resize_image8 = image8.resize((200, 200))
            img8 = ImageTk.PhotoImage(resize_image8)
            label8 = Label(top_1,image=img8)
            label8.image = img8
            label8.grid(row=3,column=3)

            yash9=Label(top_1,text="3)-------COOKED DRY BEANS-->",font=("italic",15))
            yash9.grid(row=4,column=1)
            
            image9 = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\pictures\COOKED DRY BEANS.jpeg")
            resize_image9 = image9.resize((200, 200))
            img9 = ImageTk.PhotoImage(resize_image9)
            label9 = Label(top_1,image=img9)
            label9.image = img9
            label9.grid(row=4,column=3)

            yash9=Label(top_1,text="4)-------RAW LEAFY GREENS(SALAD)-->",font=("italic",15))
            yash9.grid(row=2,column=4)
            
            image9 = Image.open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\pictures\green leafy salad.jpeg")
            resize_image9 = image9.resize((200, 200))
            img9 = ImageTk.PhotoImage(resize_image9)
            label9 = Label(top_1,image=img9)
            label9.image = img9
            label9.grid(row=2,column=6)

            def save1():
                files = [('All Files', '*.*'),
                         ('Python Files', '*.py'),
                         ('Text Document', '*.txt')]
                file = asksaveasfile(filetypes = files, defaultextension = files)

            blank=Label(top_1,text="")
            blank.grid(row=5,column=3)
            
            save_button=Button(top_1,text="SAVE", command=save1)
            save_button.grid(row=6,column=3)

        elif(optionvalue.get()=="Lose"  and vnvvalue.get().lower()=="non-veg"):
            tmsg.showerror("showerror", "ERROR !    INVALID INPUT PLEASE TRY AGAIN")
            
          
            
        elif(optionvalue.get() in ("Gain" , "lose") and diseasevalue.get()=="blood pressure" and vnvvalue.get().lower()=="non-veg"):
            tmsg.showerror("showerror", "ERROR !    INVALID INPUT  PLEASE TRY AGAIN")
            

        else:
            tmsg.showerror("showerror", "ERROR !    INVALID INPUT  PLEASE TRY AGAIN")
            
    def combinedfunc1():
        data()
        top.destroy()
        open_top_toplevel()

    
    submit_button=Button(top,text="submit", command= combinedfunc1)
    submit_button.grid(row=13, column=2)
    
    exit_button=Button(top,text="EXIT", command=top.destroy)
    exit_button.grid(row=1, column=4)

    

    mainmenu=Menu(top)
    m1=Menu(mainmenu,tearoff=0)
    m1.add_command(label="review",command=myfunc)
    m1.add_command(label="complain")
    m1.add_command(label="suggestion")
    top.config(menu=mainmenu)
    mainmenu.add_cascade(label="feedback",menu=m1)
    top.mainloop()


        
    #varun_1.title("DIET PLAN SYSTEM")
heading=Label(varun_1,text="LETS GET STARTED",bg="black",fg="white",padx=20,pady=20,font=("times",13),borderwidth=
              3,relief=SUNKEN).grid(row=1,column=2)
button=Button(varun_1,text='user',font=("times",13),command=open_toplevel)
button.grid(row=2,column=2)
lst=['admin','Admin@321']

uservalue=StringVar()
passvalue=StringVar()


    
def adminpage():
    varun_1.destroy()
    varun_2=Tk()
    varun_2.configure(bg="#F4A460")
    varun_2.minsize(800,500)
    varun_2.title("INFORMATION OF USERS")
    #sahil_15= Label(varun_2,text="INFORMATION OF USERS",bg="black",fg="white",padx=20,pady=20,font=("times",13),borderwidth=
                     #3,relief=SUNKEN).grid(row=1,column=2)
    
    sahil_16=Label(varun_2,text="NAME",bg="black",fg="white",padx=20,pady=20,font=("times",9))
    sahil_16.grid(row=1,column=1)
    
    sahil_17=Label(varun_2,text="AGE",bg="black",fg="white",padx=20,pady=20,font=("times",9))
    sahil_17.grid(row=1,column=2)

    sahil_18=Label(varun_2,text="GENDER",bg="black",fg="white",padx=20,pady=20,font=("times",9))
    sahil_18.grid(row=1,column=3)

    sahil_19=Label(varun_2,text="WEIGHT",bg="black",fg="white",padx=20,pady=20,font=("times",9))
    sahil_19.grid(row=1,column=4)

    sahil_20=Label(varun_2,text="DISEASES",bg="black",fg="white",padx=20,pady=20,font=("times",9))
    sahil_20.grid(row=1,column=5)

    sahil_21=Label(varun_2,text="VEG/NONVEG/VEGAN",bg="black",fg="white",padx=20,pady=20,font=("times",9))
    sahil_21.grid(row=1,column=6)

    exit_button=Button(varun_2,text="EXIT",font='times',command=varun_2.destroy)
    exit_button.grid(row=1,column=7)
    
    f1=open(r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\project.bin","rb")
    filename=r"C:\Users\DELL\OneDrive\Desktop\project work\cs project\project.bin"
    c=trying(filename)

    for i in range(2,c+2):
        try:
            v=pickle.load(f1)
            
            text1=Label(varun_2,text=v[0])
            text1.grid(row=i,column=1)
            
            text2=Label(varun_2,text=v[1])                                      # showing the data
            text2.grid(row=i,column=2)
            
            text3=Label(varun_2,text=v[2])
            text3.grid(row=i,column=3)
            
            text4=Label(varun_2,text=v[3])
            text4.grid(row=i,column=4)
            
            text5=Label(varun_2,text=v[4])
            text5.grid(row=i,column=5)
            
            text6=Label(varun_2,text=v[5])
            text6.grid(row=i,column=6)
        except:
            f1.close()
            print('error')
    
    varun_2.mainloop()

def login():
    if(uservalue.get()==lst[0] and passvalue.get()==lst[1]):
        sahil_15=Label(varun_1,text='WELCOME VARUN',font=13)
        sahil_15.grid(row=6,column=3)                                                                #checking username and password
        time.sleep(3)
        adminpage()

    else:
        sahil_16=Label(varun_1,text='INVALID ! LOGIN ERROR')
        sahil_16.grid(row=6,column=3)
  
    
    
def combinedfunc2():
    login()

    #adminpage()
def admin():
    
    sahil_13 = Label(varun_1,text="USERNAME",bg="black",fg="white",padx=20,pady=20,font=("times",13),borderwidth=
                     3,relief=SUNKEN)
    sahil_13.grid(row=3,column=2)
    
    sahil_14 = Label(varun_1,text="PASSWORD",bg="black",fg="white",padx=20,pady=20,font=("times",13),borderwidth=
                     3,relief=SUNKEN)
    sahil_14.grid(row=4,column=2)

    userentry=Entry(varun_1,textvariable=uservalue)                                                             # login interface
    userentry.grid(row=3,column=3)

    passentry=Entry(varun_1,textvariable=passvalue)
    passentry.grid(row=4,column=3)

    login_button=Button(varun_1,text='LOGIN',command=combinedfunc2)
    login_button.grid(row=5,column=2)

button1=Button(varun_1,text='admin',font=("times",13),command=admin)
button1.grid(row=2,column=3)

varun_1.mainloop()
