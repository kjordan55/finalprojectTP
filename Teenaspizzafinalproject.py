from tkinter import *
import time
from sqlite3 import *
import random
from tkinter import messagebox
class Pizza:
    cartlist=[]
    amount=0
#--  page 1------
    def main(sf):
        try:
            sf.scr.destroy()
            sf.scr=Tk()
        except:
            try:
                sf.scr=Tk()
            except:
                pass

        sf.scr.geometry("1366x768")
        sf.scr.title("TEENA'S PIZZA")
        #sf.scr.resizable(False, False)
        sf.scr.iconbitmap('p.ico')
        sf.mainf1=Frame(sf.scr,height=150,width=1366)
        sf.logo=PhotoImage(file="pizzamain.jpg")
        sf.l=Label(sf.mainf1,image=sf.logo)
        sf.l.place(x=0,y=0)
        sf.mainf1.pack(fill=BOTH,expand=1)
        sf.mainf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.mainf2,height=618,width=1366)
        sf.c.pack()
        sf.back=PhotoImage(file="pizzamain.jpg")
        sf.c.create_image(683,284,image=sf.back)
        sf.lab=Button(sf.mainf2,text= "Click Here to enter the World of Pizzas",command=lambda:sf.Login(),cursor="hand2", bd=10 ,font=("cooper black",30, 'bold'),fg="white",bg="#0b1335")
        sf.lab.place(x=250,y=250)
        sf.mainf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

#------ page 2------
    def Login(sf):
        sf.cartlist=[]
        sf.amount=0
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("TEENA'S PIZZA")
        sf.scr.geometry("1366x768")
        #sf.scr.resizable(False, False)
        sf.loginf1=Frame(sf.scr,height=150,width=1366)
        sf.logo=PhotoImage(file="menu.jpg")
        sf.ba=Label(sf.loginf1,image=sf.logo,height=150).place(x=0,y=0)
        sf.home=Button(sf.loginf1,text="Home",command=lambda:sf.main(),bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))
        sf.home.place(x=800,y=100)
        sf.adlog=Button(sf.loginf1,text="Administrator Login",command=lambda:sf.Adminlogin(),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("cooper black",16))
        sf.adlog.place(x=925,y=100)
        sf.abt=Button(sf.loginf1,text="About Us",bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))
        sf.abt.config(command=lambda:sf.about())
        sf.abt.place(x=1210,y=100)
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.tim=Label(sf.loginf1,text=sf.localtime,fg="white",font=("default",16),bg="#0b1335")
        sf.tim.place(x=925,y=50)
        sf.loginf1.pack(fill=BOTH,expand=1)
        sf.loginf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.loginf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="pizzamain.jpg")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.c.create_rectangle(50,100,700,450,fill="#d3ede6",outline="white",width=6)
        sf.log=Label(sf.loginf2,text="LOGIN",fg="white",bg="#0b1335",width=26,font=("cooper black",27))
        sf.log.place(x=59,y=105)
        sf.lab1=Label(sf.loginf2,text="UserName",bg="#d3ede6",font=("cooper black",22))
        sf.lab1.place(x=100,y=180)
        sf.user=Entry(sf.loginf2,bg="white",font=("cooper black",22),bd=6 ,justify='left')
        sf.user.place(x=320,y=180)
        sf.lab2=Label(sf.loginf2,text="Password",bg="#d3ede6",font=("cooper black",22))
        sf.lab2.place(x=105,y=250)
        sf.pasd=Entry(sf.loginf2,bg="white",font=("cooper black",22),bd=6 ,justify='left')
        sf.pasd.place(x=320,y=250)
        sf.lg=Button(sf.loginf2,text="Login",cursor="hand2",command=lambda:sf.logindatabase(),fg="white",bg="#0b1335",font=("cooper black",20),bd=4)
        sf.lg.place(x=180,y=320)
        def clear(sf):
            sf.user.delete(0,END)
            sf.pasd.delete(0,END)
        sf.cl=Button(sf.loginf2,text="Clear",cursor="hand2",command=lambda:clear(sf),fg="white",bg="#0b1335",font=("cooper black",20),bd=4)
        sf.cl.place(x=450,y=320)
        sf.rg=Button(sf.loginf2,text="New to TEENA'S PIZZA",command=lambda:sf.Register(),fg="white",cursor="hand2",bg="#8c68c1",font=("cooper black",20),bd=6)
        sf.rg.place(x=200,y=390)
        sf.c.create_rectangle(850,120,1310,480,fill="#d3ede6",outline="white",width=4)
        sf.ext=PhotoImage(file="p4.png")
        sf.url=Label(sf.loginf2,image=sf.ext,cursor="hand2").place(x=855,y=125)
        sf.loginf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()
    def resultlog(sf):
        sf.loguser=sf.user.get()
        sf.logpass=sf.pasd.get()
        return sf.loguser,sf.logpass

    def about(sf):
        sf.scr1=Tk()
        sf.L=Label(sf.scr1,text="NEW PIZZA SHOP")
        sf.L.pack()
        sf.scr1.mainloop()
    #--  page 3------
    def Adminlogin(sf):
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("TEENA'S PIZZA")
        sf.scr.geometry("1366x768")
        #sf.scr.resizable(False, False)
        sf.adminf1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.adminf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="pizzamain.jpg")
        sf.c.create_image(683,75,image=sf.logo)
        sf.home=Button(sf.adminf1,text="Home",command=lambda:sf.main(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.home.place(x=1000,y=90)
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.c.create_text(1000,50,text=sf.localtime,fill="white",font=("default",16))
        sf.adminf1.pack(fill=BOTH,expand=1)
        sf.adminf2=Frame(sf.scr,height=618,width=1366)
        
        sf.c=Canvas(sf.adminf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="pizzamain.jpg")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.c.create_rectangle(350,100,1016,450,fill="#d3ede6",outline="white",width=6)
        sf.log=Label(sf.adminf2,text="ADMIN LOGIN",fg="white",bg="#0b1335",width=27,font=("cooper black",27))
        sf.log.place(x=357,y=110)
        sf.lab1=Label(sf.adminf2,text="UserName",bg="#d3ede6",font=("cooper black",22))
        sf.lab1.place(x=400,y=200)
        sf.usera=Entry(sf.adminf2,bg="white",font=("cooper black",22),bd=5)
        sf.usera.place(x=650,y=200)
        sf.lab2=Label(sf.adminf2,text="Password",bg="#d3ede6",font=("cooper black",22))
        sf.lab2.place(x=405,y=270)
        sf.pasda=Entry(sf.adminf2,bg="white",font=("cooper black",22),bd=5)
        sf.pasda.place(x=650,y=270)
        sf.lg=Button(sf.adminf2,text="Login",cursor="hand2",fg="white",bg="#0b1335",command=lambda:sf.admindatabase(),font=("copper black",20,'bold'),bd=5)
        sf.lg.place(x=650,y=350)
        sf.cl=Button(sf.adminf2,text="Back",cursor="hand2",fg="white",bg="#0b1335",command=lambda:sf.Login(),font=("copper black",20,'bold'),bd=5)
        sf.cl.place(x=400,y=350)
        def clear(sf):
            sf.usera.delete(0,END)
            sf.pasda.delete(0,END)
        sf.rg=Button(sf.adminf2,text="Clear",fg="white",cursor="hand2",bg="#0b1335",command=lambda:clear(sf),bd=5,font=("copper black",20,'bold'))
        sf.rg.place(x=900,y=350)
        
        sf.adminf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

    def resultadmin(sf):
        sf.loguser=sf.usera.get()
        sf.logpass=sf.pasda.get()
        return sf.loguser,sf.logpass

#--  page 4------
    def Register(sf):
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("TEENA'S PIZZA")
        sf.scr.geometry("1366x768")
        #sf.scr.resizable(False, False)
        sf.regf1=Frame(sf.scr,height=150,width=1366)
        sf.logo=PhotoImage(file="logo.PNG")
        sf.ba=Label(sf.regf1,image=sf.logo,height=150).place(x=0,y=0)
        sf.home=Button(sf.regf1,text="Home",command=lambda:sf.main(),bg="#0b1335",cursor="hand2",fg="white",font=("default",16))
        sf.home.place(x=800,y=100)
        sf.adlog=Button(sf.regf1,text="Administrator Login",command=lambda:sf.Adminlogin(),cursor="hand2",bg="#0b1335",fg="white",font=("default",16))
        sf.adlog.place(x=950,y=100)
        sf.abt=Button(sf.regf1,text="About Us",command=lambda:sf.about(),bg="#0b1335",cursor="hand2",fg="white",font=("default",16))
        sf.abt.place(x=1210,y=100)
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.tim=Label(sf.regf1,text=sf.localtime,fg="white",font=("default",16),bg="#0b1335")
        sf.tim.place(x=925,y=50)
        sf.regf1.pack(fill=BOTH,expand=1)
        
        sf.regf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.regf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="pizzamain.jpg")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.c.create_rectangle(150,100,1216,450,fill="#d3ede6",outline="white",width=6)
        sf.log=Label(sf.regf2,text="REGISTRATION",fg="white",bg="#0b1335",width=20,font=("cooper black",27))
        sf.log.place(x=480,y=120)
        sf.lab1=Label(sf.regf2,text="FirstName",bg="#d3ede6",font=("cooper black",18))
        sf.lab1.place(x=190,y=200)
        sf.first=Entry(sf.regf2,bg="white",width=15,font=("cooper black",18),bd=5)
        sf.first.place(x=430,y=200)
        sf.lab2=Label(sf.regf2,text="LastName",bg="#d3ede6",font=("cooper black",18))
        sf.lab2.place(x=730,y=200)
        sf.last=Entry(sf.regf2,bg="white",width=15,font=("cooper black",18),bd=5)
        sf.last.place(x=920,y=200)
        sf.lab3=Label(sf.regf2,text="Username",bg="#d3ede6",font=("cooper black",18))
        sf.lab3.place(x=190,y=250)
        sf.usern=Entry(sf.regf2,bg="white",width=15,font=("cooper black",18),bd=5)
        sf.usern.place(x=430,y=250)
        sf.lab4=Label(sf.regf2,text="Password",bg="#d3ede6",font=("cooper black",18))
        sf.lab4.place(x=730,y=250)
        sf.passd=Entry(sf.regf2,bg="white",width=15,font=("cooper black",18),bd=5)
        sf.passd.place(x=920,y=250)
        sf.lab5=Label(sf.regf2,text="Email",bg="#d3ede6",font=("cooper black",18))
        sf.lab5.place(x=190,y=300)
        sf.email=Entry(sf.regf2,bg="white",width=15,font=("cooper black",18),bd=5)
        sf.email.place(x=430,y=300)
        sf.lab6=Label(sf.regf2,text="Mobile No.",bg="#d3ede6",font=("cooper black",18))
        sf.lab6.place(x=730,y=300)
        sf.mob=Entry(sf.regf2,bg="white",width=15,font=("cooper black",18),bd=5)
        sf.mob.place(x=920,y=300)
        sf.bc=Button(sf.regf2,text="Back",cursor="hand2",command=lambda:sf.Login(),fg="white",bg="#0b1335",font=("cooper black",18),bd=5)
        sf.bc.place(x=370,y=370)
        sf.rg=Button(sf.regf2,text="Register",cursor="hand2",fg="white",bg="#0b1335",command=lambda:sf.Regdatabase(),font=("cooper black",18),bd=5)
        sf.rg.place(x=610,y=370)
        def clear(sf):
            sf.usern.delete(0,END)
            sf.passd.delete(0,END)
            sf.first.delete(0,END)
            sf.last.delete(0,END)
            sf.email.delete(0,END)
            sf.mob.delete(0,END)
        sf.cl=Button(sf.regf2,text="Clear",cursor="hand2",fg="white",bg="#0b1335",command=lambda:clear(sf),font=("cooper black",18),bd=5)
        sf.cl.place(x=910,y=370)
        sf.regf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()
    def resultreg(sf):
        sf.reguser=sf.usern.get()
        sf.regpasd=sf.passd.get()
        sf.firstname=sf.first.get()
        sf.lastname=sf.last.get()
        sf.Email=sf.email.get()
        sf.Mob=sf.mob.get()
        return sf.reguser,sf.regpasd,sf.firstname,sf.lastname,sf.Email,sf.Mob
#--  page 5------
    def adminmain(sf):
        sf.scr.destroy()
        sf.scr = Tk()
        #sf.scr.config(bg="#f2e8b8")
        sf.scr.title("TEENA'S PIZZA")
        sf.scr.geometry("1366x768")

        sf.admainf1=Frame(sf.scr,bg="#f2e8b8",height=150,width=1366)
        sf.admainf1.pack(side=TOP,fill=BOTH)
        sf.c=Canvas(sf.admainf1,height=150,bg="#f2e8b8",width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="pizzamain.jpg")
        sf.c.create_image(683,50,image=sf.logo)
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.c.create_text(900,50,text=sf.localtime,fill="white",font=("default",16))
        sf.c.create_text(683,125,font=( 'Cooper Black' ,25, 'bold','underline' ),text="Management System")
        sf.out=Button(sf.admainf1,text="Log Out",bg="#0b1335",cursor="hand2",command=lambda:sf.Adminlogin(),fg="white",bd=5,font=("default",16,'bold'))
        sf.out.place(x=1100,y=25)

        def Ref(sf):
            sf.con=connect("pizza.db")
##            sf.x=random.randint(100, 500)
##            sf.randomRef = str(sf.x)
            sf.cur=sf.con.cursor()
            try:
                 sf.cur.execute("create table orderdetail(id integer primary key,username varchar(50),name varchar(50),mobile varchar(50),money varchar(10) not null,address varchar ,orderdet varchar not null)")
                 sf.con.commit()
            except:
                pass
            x=sf.cur.execute("select count(*) from orderdetail")
            ordno=list(x)[0][0]+1
            sf.order.set(ordno)

            sf.v1=sf.vp1.get()
            if sf.v1=="Medium":
                sf.p1=float(sf.Deluxe_Veggie.get())*450
            elif sf.v1=="Large":
                sf.p1=float(sf.Deluxe_Veggie.get())*650
            else:
                sf.p1=float(sf.Deluxe_Veggie.get())*250
            sf.v2=sf.vp2.get()
            if sf.v2=="Medium":
                sf.p2= float(sf.Veg_Vaganza.get())*400
            elif sf.v2=="Large":
                sf.p2= float(sf.Veg_Vaganza.get())*600
            else:
                sf.p2= float(sf.Veg_Vaganza.get())*250
            sf.v3=sf.vp3.get()
            if sf.v3=="Medium":
                sf.p3= float(sf.Pepper.get())*385
            elif sf.v3=="Large":
                sf.p3= float(sf.Pepper.get())*550
            else:
                sf.p3= float(sf.Pepper.get())*225
            sf.v4=sf.vp4.get()
            if sf.v4=="Medium":
                sf.p4= float(sf.Margherita.get())*195
            elif sf.v4=="Large":
                sf.p4= float(sf.Margherita.get())*385
            else:
                sf.p4= float(sf.Margherita.get())*99
            sf.v5=sf.vp5.get()
            if sf.v5=="Medium":
                sf.p5= float(sf.Non_Veg_Supreme.get())*450
            elif sf.v5=="Large":
                sf.p5= float(sf.Non_Veg_Supreme.get())*650
            else:
                sf.p5= float(sf.Non_Veg_Supreme.get())*250
            sf.v6=sf.vp6.get()
            if sf.v6=="Medium":
                sf.p6= float(sf.Chicken_Tikka.get())*400
            elif sf.v6=="Large":
                sf.p6= float(sf.Chicken_Tikka.get())*600
            else:
                sf.p6= float(sf.Chicken_Tikka.get())*225
            sf.v7=sf.vp7.get()
            if sf.v7=="Medium":
                sf.p7= float(sf.Chicken_Sausage.get())*385
            elif sf.v7=="Large":
                sf.p7= float(sf.Chicken_Sausage.get())*550
            else:
                sf.p7= float(sf.Chicken_Sausage.get())*225
            sf.v8=sf.vp8.get()
            if sf.v8=="Medium":
                sf.p8= float(sf.Chicken_Peri.get())*195
            elif sf.v8=="Large":
                sf.p8= float(sf.Chicken_Peri.get())*385
            else:
                sf.p8= float(sf.Chicken_Peri.get())*99
            sf.p9= float(sf.Roasted_Chicken.get())*109
            sf.p10= float(sf.Chicken_Meatballs.get())*99
            sf.p11= float(sf.Boneles_sChicken.get())*139
            sf.p12= float(sf.Coke_Mobile.get())*45
            sf.p13= float(sf.Burger_Pizza.get())*99
            sf.p14= float(sf.White_Pasta.get())*135
            
            sf.costofmeal = "Rs.",str('%.2f'% (sf.p1+sf.p2+sf.p3+sf.p4+sf.p5+sf.p6+sf.p7+sf.p8+sf.p9+sf.p10+sf.p11+sf.p12+sf.p13+sf.p14))
            sf.PayTax=((sf.p1+sf.p2+sf.p3+sf.p4+sf.p5+sf.p6+sf.p7+sf.p8+sf.p9+sf.p10+sf.p11+sf.p12+sf.p13+sf.p14)*.05)
            sf.Totalcost=(sf.p1+sf.p2+sf.p3+sf.p4+sf.p5+sf.p6+sf.p7+sf.p8+sf.p9+sf.p10+sf.p11+sf.p12+sf.p13+sf.p14)
            sf.Ser_Charge=((sf.p1+sf.p2+sf.p3+sf.p4+sf.p5+sf.p6+sf.p7+sf.p8+sf.p9+sf.p10+sf.p11+sf.p12+sf.p13+sf.p14)/99)
            sf.Service="Rs."+str('%.2f'% sf.Ser_Charge)
            sf.OverAllCost="Rs."+str(int(sf.PayTax + sf.Totalcost + sf.Ser_Charge))
            sf.PaidTax="Rs."+str('%.2f'% sf.PayTax)
            sf.money=int(sf.PayTax + sf.Totalcost + sf.Ser_Charge)
            sf.Service_Charge.set(sf.Service)
            sf.cost.set(sf.costofmeal)
            sf.Tax.set(sf.PaidTax)
            sf.Total.set(sf.OverAllCost) 

        def reset(sf):
            sf.Deluxe_Veggie.set("0")
            sf.Veg_Vaganza.set("0")
            sf.Pepper.set("0")
            sf.Margherita.set("0")
            sf.Non_Veg_Supreme.set("0")
            sf.Chicken_Tikka.set("0")
            sf.Chicken_Sausage.set("0")
            sf.Chicken_Peri.set("0")
            sf.Coke_Mobile.set("0")
            sf.Burger_Pizza.set("0")
            sf.White_Pasta.set("0")
            sf.Roasted_Chicken.set("0")
            sf.Chicken_Meatballs.set("0")
            sf.Boneles_sChicken.set("0")
            sf.Total.set("0")
            sf.Service_Charge.set("0")
            sf.Tax.set("0")
            sf.cost.set("0")
            sf.order.set("0")
            sf.Cutomer_name.set("")
            sf.cusmob.set("")
            sf.vp1.set("Medium")
            sf.vp2.set("Medium")
            sf.vp3.set("Medium")
            sf.vp4.set("Medium")
            sf.vp5.set("Medium")
            sf.vp6.set("Medium")
            sf.vp7.set("Medium")
            sf.vp8.set("Medium")

            

        def price(sf):
            sf.roo = Tk()
            sf.roo.geometry("600x768+0+0")
            sf.roo.title("Price List")
            sf.lblinfo = Label(sf.roo, font=('aria', 18, 'bold'), text="ITEM", fg="black", bd=5)
            sf.lblinfo.grid(row=0, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15,'bold'), text="Veg Pizza", fg="black", anchor=W)
            sf.lblinfo.grid(row=1, column=1)
            sf.lblinfo = Label(sf.roo, font=('aria', 15), text="(Medium/Large/Regular)", fg="black", anchor=W)
            sf.lblinfo.grid(row=1, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 18, 'bold'), text="PRICE", fg="black", anchor=W)
            sf.lblinfo.grid(row=0, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Deluxe Veggie", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=2, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹450/₹650/₹250", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=2, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Veg Vaganza", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=3, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹400/₹600/₹250", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=3, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="5 sf.Pepper", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=4, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹385/₹550/₹225", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=4, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="sf.Margherita", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=5, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹195/₹385/₹99", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=5, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Non-Veg Pizza", fg="black", anchor=W)
            sf.lblinfo.grid(row=6, column=1)
            sf.lblinfo = Label(sf.roo, font=('aria', 15), text="(Medium/Large/Regular)", fg="black", anchor=W)
            sf.lblinfo.grid(row=6, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Non-Veg Supreme", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=7, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹450/₹650/₹250", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=7, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Chicken Tikka", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=8, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹400/₹600/₹250", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=8, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Chicken Suasage", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=9, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹385/₹550/₹225", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=9, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Chicken Peri", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=10, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹195/₹385/₹99", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=10, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Specialty Chicken", fg="black", anchor=W)
            sf.lblinfo.grid(row=11, column=1)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Roasted Chicken", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=12, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹109", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=12, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Chicken Meatballs", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=13, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹99", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=13, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Boneless Chicken", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=14, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹139", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=14, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Sides & Beverages", fg="black", anchor=W)
            sf.lblinfo.grid(row=15, column=1)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Coke Mobile", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=16, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹45", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=16, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Burger Pizza", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=17, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹99", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=17, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="White Pasta", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=18, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹135", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=18, column=2)

            sf.roo.mainloop()




        sf.admainf2 = Frame(sf.scr,width =1366,bg="#f2e8b8",height=618,relief=SUNKEN)
        sf.admainf2.pack(side=BOTTOM,fill=BOTH,expand=1)
        sf.Deluxe_Veggie= StringVar()
        sf.Veg_Vaganza = StringVar()
        sf.Pepper = StringVar()
        sf.Margherita= StringVar()
        sf.Non_Veg_Supreme = StringVar()
        sf.Chicken_Tikka = StringVar()
        sf.Chicken_Sausage= StringVar()
        sf.Chicken_Peri= StringVar()
        sf.Coke_Mobile = StringVar()
        sf.Burger_Pizza = StringVar()
        sf.White_Pasta = StringVar()
        sf.Roasted_Chicken= StringVar()
        sf.Chicken_Meatballs = StringVar()
        sf.Boneles_sChicken = StringVar()
        sf.Total = StringVar()
        sf.Service_Charge= StringVar()
        sf.Tax = StringVar()
        sf.cost = StringVar()
        sf.order=StringVar()
        sf.Cutomer_name =StringVar()
        sf.cusmob = StringVar()
        sf.vp1=StringVar()
        sf.vp2=StringVar()
        sf.vp3=StringVar()
        sf.vp4=StringVar()
        sf.vp5=StringVar()
        sf.vp6=StringVar()
        sf.vp7=StringVar()
        sf.vp8=StringVar()
        reset(sf)
        sf.l=["Medium","Large","Regular"]

        #veg pizza
        sf.non=Label(sf.admainf2,pady=2,text=(" "),font=( 'Cooper Black' ,20),bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=0,column=1)
        sf.lbl1 = Label(sf.admainf2,pady=2, font=( 'Cooper Black' ,20, 'bold','underline' ),bg="#f2e8b8",text="Veg Pizza",bd=10,anchor='w')
        sf.lbl1.place(x=180,y=0)
        sf.lbl11 = Label(sf.admainf2,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=6,bg="#f2e8b8",text="Items",bd=6,anchor='w')
        sf.lbl11.grid(row=1,column=0)
        sf.lbl12 = Label(sf.admainf2,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=7,bg="#f2e8b8",text="Size",bd=6,anchor='w')
        sf.lbl12.grid(row=1,column=1)
        sf.lbl13 = Label(sf.admainf2,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=8,bg="#f2e8b8",text="Quantity",bd=6,anchor='w')
        sf.lbl13.grid(row=1,column=2,padx=4)

        sf.lbldel= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Deluxe Veggie:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lbldel.grid(row=2,column=0)
        sf.opdel=OptionMenu(sf.admainf2,sf.vp1,*sf.l)
        sf.opdel.config(width=6)
        sf.opdel.grid(row=2,column=1)
        sf.txtdel= Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Deluxe_Veggie , bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txtdel.grid(row=2,column=2)

        sf.lblvaga = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Veg Vaganza:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblvaga.grid(row=3,column=0)
        sf.opvaga=OptionMenu(sf.admainf2,sf.vp2,*sf.l)
        sf.opvaga.config(width=6)
        sf.opvaga.grid(row=3,column=1)
        sf.txtvaga = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Veg_Vaganza , bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txtvaga.grid(row=3,column=2)

        sf.lblpep= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text=" 5 Pepper:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblpep.grid(row=4,column=0)
        sf.oppep=OptionMenu(sf.admainf2,sf.vp3,*sf.l)
        sf.oppep.config(width=6)
        sf.oppep.grid(row=4,column=1)
        sf.txtpep= Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Pepper ,bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txtpep.grid(row=4,column=2)

        sf.lblmag = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Margherita:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblmag.grid(row=5,column=0)
        sf.opmag=OptionMenu(sf.admainf2,sf.vp4,*sf.l)
        sf.opmag.config(width=6)
        sf.opmag.grid(row=5,column=1)
        sf.txtmag = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Margherita,width=4,bg="powder blue",bd=6 ,justify='right')
        sf.txtmag.grid(row=5,column=2)


        #sf.non veg
        sf.non=Label(sf.admainf2,pady=2,text=(" "),font=( 'Cooper Black' ,20),bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=6,column=1)
        sf.lbl2 = Label(sf.admainf2,pady=2, font=( 'Cooper Black' ,20, 'bold','underline' ),bg="#f2e8b8",text="Non-Veg Pizza",bd=10,anchor='w')
        sf.lbl2.place(x=150,y=290)
        sf.lbl21 = Label(sf.admainf2,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=6,bg="#f2e8b8",text="Items",bd=6,anchor='w')
        sf.lbl21.grid(row=7,column=0)
        sf.lbl22 = Label(sf.admainf2,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=7,bg="#f2e8b8",text="Size",bd=6,anchor='w')
        sf.lbl22.grid(row=7,column=1)
        sf.lbl23 = Label(sf.admainf2,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=8,bg="#f2e8b8",text="Quantity",bd=6,anchor='w')
        sf.lbl23.grid(row=7,column=2)

        sf.lblsup= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Non-Veg Supreme:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblsup.grid(row=8,column=0)
        sf.opsup=OptionMenu(sf.admainf2,sf.vp5,*sf.l)
        sf.opsup.config(width=6)
        sf.opsup.grid(row=8,column=1)
        sf.txtsup= Entry(sf.admainf2,width=4,font=('ariel' ,16,'bold'), textvariable=sf.Non_Veg_Supreme , bd=6,bg="powder blue" ,justify='right')
        sf.txtsup.grid(row=8,column=2)

        sf.lbltika = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Chicken Tikka:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lbltika.grid(row=9,column=0)
        sf.optika=OptionMenu(sf.admainf2,sf.vp6,*sf.l)
        sf.optika.config(width=6)
        sf.optika.grid(row=9,column=1)
        sf.txttika = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Chicken_Tikka , bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txttika.grid(row=9,column=2)

        sf.lblsaus= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Chicken Sausage:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblsaus.grid(row=10,column=0)
        sf.opsaus=OptionMenu(sf.admainf2,sf.vp7,*sf.l)
        sf.opsaus.config(width=6)
        sf.opsaus.grid(row=10,column=1)
        sf.txtsaus= Entry(sf.admainf2,width=4,font=('ariel' ,16,'bold'), textvariable=sf.Chicken_Sausage , bd=6,bg="powder blue" ,justify='right')
        sf.txtsaus.grid(row=10,column=2)

        sf.lblperi = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Chicken Peri:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblperi.grid(row=11,column=0)
        sf.opperi=OptionMenu(sf.admainf2,sf.vp8,*sf.l)
        sf.opperi.config(width=6)
        sf.opperi.grid(row=11,column=1)
        sf.txtperi= Entry(sf.admainf2,font=('ariel' ,16,'bold'),width=4, textvariable=sf.Chicken_Peri , bd=6,bg="powder blue" ,justify='right')
        sf.txtperi.grid(row=11,column=2)

        #Special
        sf.non=Label(sf.admainf2,pady=2,text=(" "),font=( 'Cooper Black' ,20),bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=0,column=5)
        sf.lbl3 = Label(sf.admainf2,pady=2, font=( 'Cooper Black' ,20, 'bold','underline' ),bg="#f2e8b8",text="Specialty",bd=10,anchor='w')
        sf.lbl3.place(x=550,y=0)
        sf.lbl31 = Label(sf.admainf2,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=6,bg="#f2e8b8",text="Items",bd=6,anchor='w')
        sf.lbl31.grid(row=1,column=4)
        sf.lbl33 = Label(sf.admainf2,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=8,bg="#f2e8b8",text="Quantity",bd=6,anchor='w')
        sf.lbl33.grid(row=1,column=5)

        sf.lblros= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Roasted Chicken:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblros.grid(row=2,column=4)
        sf.txtros= Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Roasted_Chicken , bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txtros.grid(row=2,column=5)

        sf.lblmeat = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Chicken Meatballs:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblmeat.grid(row=3,column=4)
        sf.txtmeat = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Chicken_Meatballs , bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txtmeat.grid(row=3,column=5)

        sf.lblbon= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Boneless Chicken:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblbon.grid(row=4,column=4)
        sf.txtbon= Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Boneles_sChicken,bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txtbon.grid(row=4,column=5)

        #Sides
        sf.non=Label(sf.admainf2,pady=2,text=(" "),font=( 'Cooper Black' ,20),bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=6,column=4)
        sf.lbl4 = Label(sf.admainf2,pady=2, font=( 'Cooper Black' ,20, 'bold','underline' ),bg="#f2e8b8",text="Sides & Beverages",bd=10,anchor='w')
        sf.lbl4.place(x=500,y=290)
        sf.lbl41 = Label(sf.admainf2,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=6,bg="#f2e8b8",text="Items",bd=6,anchor='w')
        sf.lbl41.grid(row=7,column=4)
        sf.lbl43 = Label(sf.admainf2,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=8,bg="#f2e8b8",text="Quantity",bd=6,anchor='w')
        sf.lbl43.grid(row=7,column=5)

        sf.lblcok= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Coke Mobile:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblcok.grid(row=8,column=4)
        sf.txtcok= Entry(sf.admainf2,width=4,font=('ariel' ,16,'bold'), textvariable=sf.Coke_Mobile , bd=6,bg="powder blue" ,justify='right')
        sf.txtcok.grid(row=8,column=5)

        sf.lblbur = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Burger Pizza:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblbur.grid(row=9,column=4)
        sf.txtbur = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Burger_Pizza , bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txtbur.grid(row=9,column=5)

        sf.lblpas= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="White Pasta:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblpas.grid(row=10,column=4)
        sf.txtpas= Entry(sf.admainf2,width=4,font=('ariel' ,16,'bold'), textvariable=sf.White_Pasta , bd=6,bg="powder blue" ,justify='right')
        sf.txtpas.grid(row=10,column=5)

        # customer
        sf.non=Label(sf.admainf2,pady=2,text=(" "),font=( 'Cooper Black' ,20),bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=0,column=8)
        sf.lbl6 = Label(sf.admainf2,pady=2, font=( 'Cooper Black' ,22, 'bold','underline' ),bg="#f2e8b8",text="Customer Detail",bd=10,anchor='w')
        sf.lbl6.place(x=970,y=0)
        
        sf.lblnam= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),width=10,text="    Name:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblnam.grid(row=1,column=7)
        sf.txtnam= Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Cutomer_name , bd=6,width=14,bg="powder blue" ,justify='left')
        sf.txtnam.grid(row=1,column=8)


        sf.lblmob = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Mobile No:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblmob.grid(row=2,column=7)
        sf.txtmob = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.cusmob,width=14,bd=6,bg="powder blue" ,justify='left')
        sf.txtmob.grid(row=2,column=8)

        #bill
        sf.non=Label(sf.admainf2,pady=2,text=(" "),font=( 'Cooper Black' ,20),bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=3,column=8)
        sf.lbl5 = Label(sf.admainf2,pady=2, font=( 'Cooper Black' ,22, 'bold','underline' ),bg="#f2e8b8",text="Bill Payment",bd=10,anchor='w')
        sf.lbl5.place(x=1000,y=140)

        sf.non=Label(sf.admainf2,pady=2,text=(" "),font=( 'Cooper Black' ,20),width=5,bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=4,column=6)
        sf.lblord= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),width=10,text="    Order No:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblord.grid(row=4,column=7)
        sf.txtord= Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.order , bd=6,width=14,bg="powder blue" ,justify='right')
        sf.txtord.grid(row=4,column=8)

        sf.lblco = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Subtotal:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblco.grid(row=5,column=7)
        sf.txtco = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.cost,width=14,bd=6,bg="powder blue" ,justify='right')
        sf.txtco.grid(row=5,column=8)

        sf.lblser= Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Service Charge:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblser.grid(row=6,column=7)
        sf.txtser= Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Service_Charge ,width=14,bd=6,bg="powder blue" ,justify='right')
        sf.txtser.grid(row=6,column=8)

        sf.lbltax = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Tax:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lbltax.grid(row=7,column=7)
        sf.txttax = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Tax, bd=6,width=14,bg="powder blue" ,justify='right')
        sf.txttax.grid(row=7,column=8)

        sf.lbltot = Label(sf.admainf2,pady=2, font=( 'aria' ,16, 'bold' ),text="Total:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lbltot.grid(row=8,column=7)
        sf.txttot = Entry(sf.admainf2,font=('ariel' ,16,'bold'), textvariable=sf.Total, bd=6,width=14,bg="powder blue" ,justify='right')
        sf.txttot.grid(row=8,column=8)

        sf.btnprice=Button(sf.admainf2,pady=2,bd=6 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="PRICE", bg="powder blue",command=lambda:price(sf))
        sf.btnprice.place(x=970,y=440)

        sf.btnTotal=Button(sf.admainf2,pady=2,bd=6,fg="black",font=('ariel' ,16,'bold'),width=6, text="TOTAL", bg="powder blue",command=lambda:Ref(sf))
        sf.btnTotal.place(x=1160,y=440)

        sf.btnreset=Button(sf.admainf2,pady=2,bd=6 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="RESET", bg="powder blue",command=lambda:reset(sf))
        sf.btnreset.place(x=970,y=500)

        sf.btnpay=Button(sf.admainf2,pady=2, bd=6 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="PAY", bg="powder blue",command=lambda:sf.adminorderdetail())
        sf.btnpay.place(x=1160,y=500)

        sf.scr.mainloop()

    def resultadminorder(sf):
        r1=sf.Deluxe_Veggie.get()
        r2=sf.Veg_Vaganza.get()
        r3=sf.Pepper.get()
        r4=sf.Margherita.get()
        r5=sf.Non_Veg_Supreme.get()
        r6=sf.Chicken_Tikka.get()
        r7=sf.Chicken_Sausage.get()
        r8=sf.Chicken_Peri.get()
        r9=sf.Coke_Mobile.get()
        r10=sf.Burger_Pizza.get()
        r11=sf.White_Pasta.get()
        r12=sf.Roasted_Chicken.get()
        r13=sf.Chicken_Meatballs.get()
        r14=sf.Boneles_sChicken.get()
        r20=sf.Cutomer_name.get()
        r21=sf.cusmob.get()
        r22=sf.vp1.get()
        r23=sf.vp2.get()
        r24=sf.vp3.get()
        r25=sf.vp4.get()
        r26=sf.vp5.get()
        r27=sf.vp6.get()
        r28=sf.vp7.get()
        r29=sf.vp8.get()
        r30=sf.txtdel.get()
        r31=sf.txtvaga.get()
        r32=sf.txtpep.get()
        r33=sf.txtmag.get()
        r34=sf.txtsup.get()
        r35=sf.txttika.get()
        r36=sf.txtsaus.get()
        r37=sf.txtperi.get()
        r38=sf.txtros.get()
        r39=sf.txtmeat.get()
        r40=sf.txtbon.get()
        r41=sf.txtcok.get()
        r42=sf.txtbur.get()
        r43=sf.txtpas.get()

        l1=[r1,r22,30]
        l2=[r2,r23,31]
        l3=[r3,r24,32]
        l4=[r4,r25,33]
        l5=[r5,r26,34]
        l6=[r6,r27,35]
        l7=[r7,r28,36]
        l8=[r8,r29,37]
        l9=[r12,r38]
        l10=[r13,r39]
        l11=[r14,r40]
        l12=[r9,r41]
        l13=[r10,r42]
        l14=[r11,r43]
        
        return r20,r21,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14
def adminorderdetail(sf):
        sf.credadmord=sf.resultadminorder()
        if sf.money!=0 and sf.credadmord[0]!="" and sf.credadmord[1]!="":
            if messagebox.askyesno("Pay","Want to make payment"):
                sf.con=connect("pizza.db")
                sf.cur=sf.con.cursor()
                od=[]
                try:
                    sf.cur.execute("create table orderdetail(id integer primary key,username varchar(50),name varchar(50),mobile varchar(50),money varchar(10) not null,address varchar ,orderdet varchar not null)")
                except:
                    pass
                for i in sf.credadmord[3:]:
                    if i[-1]!="0":
                        od.append(i)
                a=sf.credadmord[0]
                b=sf.credadmord[1]
                print(a,b,str(sf.money),od)
                s="insert into orderdetail(name,mobile,money,orderdet) values(%r,%r,%r,%r)"%(a,b,str(sf.money),str(od))
                sf.cur.execute(s)
                sf.con.commit()
                messagebox.showinfo("Pay","Successfully Paid")
        else:
            messagebox.showinfo("Pay","Enter Customer's Name and Mobile No  and  Order Something")
    #except:
         #   messagebox.showinfo("Pay","Enter Total button then Pay button")
def orderpay(sf,x):
        messagebox.showinfo("Pay","Payment Method is not available now")
        
x=Pizza()
x.main()
