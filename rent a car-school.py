#rent a car
from tkinter import *
from tkcalendar import DateEntry
import datetime
import mysql.connector as mysql
from tkinter import ttk

mydb=mysql.connect(host='localhost',user='root',passwd='kenjacobjoshua',database='carlist')            #ERASE THE PASS
mycursor=mydb.cursor()

def configureWindow(window,rows,columns):
        for i in range(rows):
            window.rowconfigure(i,weight=1)
        for j in range(columns):
            window.columnconfigure(j,weight=1)
            
def display_existing_clients(event):
        for i in root.grid_slaves():
                i.destroy()

        mycursor.execute("Select * from client;")
        data=mycursor.fetchall()

        tree = ttk.Treeview(root,columns=(1,2,3,4,5,6,7,8,9,10), height = 5, show = "headings")
        tree.grid()

        tree.heading(1, text="Car ID",)
        tree.heading(2, text="Client Name")
        tree.heading(3, text="Age")
        tree.heading(4, text="Email")
        tree.heading(5, text="Contact No.")
        tree.heading(6, text="Car Name")
        tree.heading(7, text="Date of Issue")
        tree.heading(8, text="Date of Return")
        tree.heading(9, text="Credit Card No.")
        tree.heading(10, text="Passport No.")

        tree.column(1, width = 50)
        tree.column(2, width = 100)
        tree.column(3, width = 50)
        tree.column(4, width = 150)
        tree.column(5, width = 100)
        tree.column(6, width = 150)
        tree.column(7, width = 100)
        tree.column(8, width = 100)
        tree.column(9, width = 100)
        tree.column(10,width = 100)

        for val in data:
            tree.insert('', 'end', values = (val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7], val[8], val[9]))



        
def rent_a_car(event):

        def cars_available(event):
                def book_interface(event):
                        def cnntsql():
                            na1=l1.get()
                            nu2=l2.get()
                            em3=l3.get()
                            ag9=l9.get()
                            cn10=l10.get()
                            di5=l5.get()
                            dr6=l6.get()
                            crn7=l7.get()
                            pn8=l8.get()
                            mycursor.execute("insert into client VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);",(na1,ag9,em3,l2,cn10,di5,di6,crn7,pn8))
                        CAR_ID=car_id.get()
                        print (CAR_ID+10)
                        for i in root.grid_slaves():
                                i.destroy()

                        l1=StringVar()
                        l2=IntVar()
                        l3=StringVar()
                        l5=StringVar()
                        l6=StringVar()
                        l7=IntVar()
                        l8=IntVar()
                        l9=IntVar()
                        l10=IntVar()
                        l10.set(f'{CAR_ID}')

                        l_1=Label(root,text="Name:",)
                        l_1.grid(row=5, column=2)
                        name=Entry(root,textvar=l1)
                        name.grid(row=6,column=2)

                        l_2=Label(root, text="Number:")
                        l_2.grid(row=8, column=2)
                        numb=Entry(root,textvar=l2)
                        numb.grid(row=9, column=2)


                        l_3=Label(root, text="Email Id:")
                        l_3.grid(row=5, column=5)
                        email=Entry(root,textvar=l3)
                        email.grid(row=6, column=5)

                        l_9=Label(root, text="Age:")
                        l_9.grid(row=5, column=8)
                        age=Entry(root,textvar=l9)
                        age.grid(row=6, column=8)

                        l_10=Label(root,text="Car ID")
                        l_10.grid(row=8,column=8)
                        cnam=Entry(root,textvar=l10)                                                # car_id comes in string, need it in int
                        cnam.grid(row=9,column=8)

                        l_5=Label(root, text="Date of Issue:")
                        l_5.grid(row=5, column=11)
                        dis=Entry(root,textvar=l5)
                        dis.grid(row=6, column=11)

                        l_6=Label(root, text="Date of Return:")
                        l_6.grid(row=8, column=11)
                        dret=Entry(root,textvar=l6)
                        dret.grid(row=9, column=11)

                        l_7=Label(root, text="Credit Card Number:")
                        l_7.grid(row=5, column=14)
                        cnum=Entry(root,textvar=l7)
                        cnum.grid(row=6, column=14)

                        l_8=Label(root, text="Passport Number:")
                        l_8.grid(row=8, column=14)
                        pnum=Entry(root,textvar=l8)
                        pnum.grid(row=9, column=14)

                        checkout=Button(root, text='CHECKOUT')
                        checkout.bind('<Button-1>',cnntsql)
                        checkout.grid(row=14, column=8)

                money=price.get()
                for i in root.grid_slaves():
                        i.destroy()
                        
                tree = ttk.Treeview(root,columns = (1,2,3,4,5,6,7,8,9,10),height=15,show="headings")
                tree.grid(column=9)

                tree.heading(1,text="Car ID",)
                tree.heading(2,text="Car Name")
                tree.heading(3,text="Brand")
                tree.heading(4,text="Model")
                tree.heading(5,text="Category")
                tree.heading(6,text="Capacity")
                tree.heading(7,text="Fuel")
                tree.heading(8,text="Cost")
                tree.heading(9,text="Weekly cost")
                tree.heading(10,text="Monthly cost")

                tree.column(1,width=50)
                tree.column(2,width=100)
                tree.column(3,width=100)
                tree.column(4,width=50)
                tree.column(5,width=100)
                tree.column(6,width=60)
                tree.column(7,width=50)
                tree.column(8,width=50)
                tree.column(9,width=100)
                tree.column(10,width=100)

                book_now=Button(root,text='Book now')
                book_now.bind('<Button-1>',book_interface)
                book_now.grid(row=17,column=9)

                car_id=Entry(root,textvar=IntVar())
                car_id.grid(row=16,column=9)

                car_ID=Label(root,text='Enter Car ID :')
                car_ID.grid(row=15,column=9)

                lt_brand=[]

                for i in lt_checkbox:
                            if i.get()==1:
                                    lt_brand.append(lt_brand_name.get(str(i)))
                if lt_brand!=[]:
                        lt_brand.extend(['Kia','Mazda','Mercedes','Tesla','Mitsubishi','Lamborghini'])   
                        for i in lt_brand:
                            m='i'
                            mycursor.execute("insert into random_1 VALUES (%s,%s);",(i,m))
                            
                else:
                        lt_brand=['Nissan','BMW','Toyota','Chevrolet','Renault','Ford','Hyundai','Audi','Infinity','Kia','Mazda','Mercedes','Tesla','Mitsubishi','Lamborghini']
                        for i in lt_brand:
                            m='i'
                            mycursor.execute("insert into random_1 VALUES (%s,%s);",(i,m))
                            

                                    
                if var.get()=='Any' and var_1.get()=='Any':
                        if money!=0:    
                                    mycursor.execute(f"select * from carlist where Category=ANY(select Category from random where cond_='i') and Fuel=ANY(select Fuel from random where cond_='i') and Brand=ANY(select Brand from random_1 where cond_='i') and Car_ID=ANY(select Car_ID from cardeals where Cost<='{money}');")
                                    x=mycursor.fetchall()
                                    for i in x:
                                            m='i'
                                            mycursor.execute("Insert into random_2 values(%s,%s);",(i[0],m))
                                    mycursor.execute('select Cost,cost_w,cost_m from cardeals where Car_ID=ANY(select Car_ID from random_2 where cond_="i");')
                                    y=mycursor.fetchall()
                                    d=0
                                    for val in x:
                                        for i in range(d,len(y)):
                                                tree.insert('', 'end', values=(val[0], val[1], val[2], val[3], val[4], val[5], val[6],y[d][0],y[d][1],y[d][2]))
                                                d=d+1
                                                break
                        else:
                                    mycursor.execute(f"select * from carlist where Category=ANY(select Category from random where cond_='i') and Fuel=ANY(select Fuel from random where cond_='i') and Brand=ANY(select Brand from random_1 where cond_='i');")
                                    x=mycursor.fetchall()
                                    for i in x:
                                            m='i'
                                            mycursor.execute("Insert into random_2 values(%s,%s);",(i[0],m))
                                    mycursor.execute('select Cost,cost_w,cost_m from cardeals where Car_ID=ANY(select Car_ID from random_2 where cond_="i");')
                                    y=mycursor.fetchall()
                                    d=0
                                    for val in x:
                                        for i in range(d,len(y)):
                                                tree.insert('', 'end', values=(val[0], val[1], val[2], val[3], val[4], val[5], val[6],y[d][0],y[d][1],y[d][2]))
                                                d=d+1
                                                break

                elif var.get()=='Any' and var_1.get()!='Any':
                        if money!=0:    
                                    mycursor.execute(f"select * from carlist where Category=ANY(select Category from random where cond_='i') and Fuel='{var_1.get()}' and Brand=ANY(select Brand from random_1 where cond_='i') and Car_ID=ANY(select Car_ID from cardeals where Cost<='{money}');")
                                    x=mycursor.fetchall()
                                    for i in x:
                                            m='i'
                                            mycursor.execute("Insert into random_2 values(%s,%s);",(i[0],m))
                                    mycursor.execute('select Cost,cost_w,cost_m from cardeals where Car_ID=ANY(select Car_ID from random_2 where cond_="i");')
                                    y=mycursor.fetchall()
                                    d=0
                                    for val in x:
                                        for i in range(d,len(y)):
                                                tree.insert('', 'end', values=(val[0], val[1], val[2], val[3], val[4], val[5], val[6],y[d][0],y[d][1],y[d][2]))
                                                d=d+1
                                                break
                        else:
                                    mycursor.execute(f"select * from carlist where Category=ANY(select Category from random where cond_='i') and Fuel='{var_1.get()}' and Brand=ANY(select Brand from random_1 where cond_='i');")
                                    x=mycursor.fetchall()
                                    for i in x:
                                            m='i'
                                            mycursor.execute("Insert into random_2 values(%s,%s);",(i[0],m))
                                    mycursor.execute('select Cost,cost_w,cost_m from cardeals where Car_ID=ANY(select Car_ID from random_2 where cond_="i");')
                                    y=mycursor.fetchall()
                                    d=0
                                    for val in x:
                                        for i in range(d,len(y)):
                                                tree.insert('', 'end', values=(val[0], val[1], val[2], val[3], val[4], val[5], val[6],y[d][0],y[d][1],y[d][2]))
                                                d=d+1
                                                break 
                
                            
                elif var.get()!='Any' and var_1.get()=='Any':
                         if money!=0:   
                                    mycursor.execute(f"select * from carlist where Category='{var.get()}' and Fuel=ANY(select Fuel from random where cond_='i') and Brand=ANY(select Brand from random_1 where cond_='i') and Car_ID=ANY(select Car_ID from cardeals where Cost<='{money}');")
                                    x=mycursor.fetchall()
                                    for i in x:
                                            m='i'
                                            mycursor.execute("Insert into random_2 values(%s,%s);",(i[0],m))
                                    mycursor.execute('select Cost,cost_w,cost_m from cardeals where Car_ID=ANY(select Car_ID from random_2 where cond_="i");')
                                    y=mycursor.fetchall()
                                    d=0
                                    for val in x:
                                        for i in range(d,len(y)):
                                                tree.insert('', 'end', values=(val[0], val[1], val[2], val[3], val[4], val[5], val[6],y[d][0],y[d][1],y[d][2]))
                                                d=d+1
                                                break
                         else:
                                    mycursor.execute(f"select * from carlist where Category='{var.get()}' and Fuel=ANY(select Fuel from random where cond_='i') and Brand=ANY(select Brand from random_1 where cond_='i');")
                                    x=mycursor.fetchall()
                                    for i in x:
                                            m='i'
                                            mycursor.execute("Insert into random_2 values(%s,%s);",(i[0],m))
                                    mycursor.execute('select Cost,cost_w,cost_m from cardeals where Car_ID=ANY(select Car_ID from random_2 where cond_="i");')
                                    y=mycursor.fetchall()
                                    d=0
                                    for val in x:
                                        for i in range(d,len(y)):
                                                tree.insert('', 'end', values=(val[0], val[1], val[2], val[3], val[4], val[5], val[6],y[d][0],y[d][1],y[d][2]))
                                                d=d+1
                                                break
                            
                elif var.get()!='Any' and var_1.get()!='Any':
                        if money!=0:    
                                    mycursor.execute(f"select * from carlist where Category='{var.get()}' and Fuel='{var_1.get()}' and Brand=ANY(select Brand from random_1 where cond_='i') and Car_ID=ANY(select Car_ID from cardeals where Cost<='{money}');")
                                    x=mycursor.fetchall()
                                    for i in x:
                                            m='i'
                                            mycursor.execute("Insert into random_2 values(%s,%s);",(i[0],m))
                                    mycursor.execute('select Cost,cost_w,cost_m from cardeals where Car_ID=ANY(select Car_ID from random_2 where cond_="i");')
                                    y=mycursor.fetchall()
                                    d=0
                                    for val in x:
                                        for i in range(d,len(y)):
                                                tree.insert('', 'end', values=(val[0], val[1], val[2], val[3], val[4], val[5], val[6],y[d][0],y[d][1],y[d][2]))
                                                d=d+1
                                                break
                        else:
                                    mycursor.execute(f"select * from carlist where Category='{var.get()}' and Fuel='{var_1.get()}' and Brand=ANY(select Brand from random_1 where cond_='i');")
                                    x=mycursor.fetchall()
                                    for i in x:
                                            m='i'
                                            mycursor.execute("Insert into random_2 values(%s,%s);",(i[0],m))
                                    mycursor.execute('select Cost,cost_w,cost_m from cardeals where Car_ID=ANY(select Car_ID from random_2 where cond_="i");')
                                    y=mycursor.fetchall()
                                    d=0
                                    for val in x:
                                        for i in range(d,len(y)):
                                                tree.insert('', 'end', values=(val[0], val[1], val[2], val[3], val[4], val[5], val[6],y[d][0],y[d][1],y[d][2]))
                                                d=d+1
                                                break
                                    
                mycursor.execute("delete from random_1;")
                mycursor.execute("delete from random_2;")

                      
        for i in root.grid_slaves():
                i.destroy()
                
        label=Label(root,text='Rent a car')
        label.grid(row=0,column=6)

        category=Label(root,text='Category :',font=('Eras Medium ITC',30))
        category.grid(row=3,column=3)

        var=StringVar(root)
        var.set('Any')
        
        category_e=OptionMenu(root,var,'Any','Hatch back','Sedan','SUV','Sport')
        category_e.configure(bg='white',activebackground='white',relief=GROOVE,width=10,height=2)
        category_e.grid(row=3,column=4)

        fuel=Label(root,text='Fuel :',font=('Eras Medium ITC',30))
        fuel.grid(row=3,column=7)

        var_1=StringVar(root)
        var_1.set('Any')

        fuel_e=OptionMenu(root,var_1,'Any','Petrol','Diesel','Electric',)
        fuel_e.configure(bg='white',activebackground='white',relief=GROOVE)
        fuel_e.grid(row=3,column=8)

        cal=Label(root,text='Start date :',font=('Eras Medium ITC',30))
        cal.grid(row=5,column=3)

        now=datetime.datetime.now()

        cal_e = DateEntry(root, width=12, month=now.month, year=now.year, day=now.day, 
                background='darkblue', foreground='white', borderwidth=2)
        cal_e.grid(row=5,column=4)

        cal1=Label(root,text='End date:',font=('Eras Medium ITC',30) )
        cal1.grid(row=5,column=7)

        cal1_e = DateEntry(root, width=12, month=now.month, year=now.year, day=now.day+1, 
                 background='darkblue', foreground='white', borderwidth=2)
        cal1_e.grid(row=5,column=8)

        price=Label(root,text='Price range :',font=('Eras Medium ITC',30))
        price.grid(row=7,column=4) 


        var_cost=StringVar(root)
        var_cost.set('day')
        
        price=Scale(root,from_=0,to=1000,orient=HORIZONTAL)
        price.config(length=150,width=20,troughcolor='white')
        price.grid(row=7,column=6)
        

        submit=Button(root,text='Submit',width=20,height=2,font=('Helvetica',20,'bold'))
        submit.bind('<Button-1>',cars_available)
        submit.grid(row=15,column=6)

        var_3=IntVar(root)      

        nissan=Checkbutton(root,text='Nissan      ',variable=var_3)
        nissan.grid(row=10,column=4)

        var_4=IntVar(root)

        BMW=Checkbutton(root,text='BMW    ',variable=var_4)
        BMW.grid(row=10,column=6)

        var_5=IntVar(root)

        toyota=Checkbutton(root,text='Toyota',variable=var_5)
        toyota.grid(row=10,column=8)

        var_6=IntVar(root)

        chevrolet=Checkbutton(root,text='Chevrolet  ',variable=var_6)
        chevrolet.grid(row=11,column=4)

        var_7=IntVar(root)

        renault=Checkbutton(root,text='Renault',variable=var_7)
        renault.grid(row=11,column=6)

        var_8=IntVar(root)

        ford=Checkbutton(root,text='Ford   ',variable=var_8)
        ford.grid(row=11,column=8)

        var_9=IntVar(root)

        hyundai=Checkbutton(root,text='Hyundai   ',variable=var_9)
        hyundai.grid(row=12,column=4)

        var_10=IntVar(root)

        audi=Checkbutton(root,text='Audi    ',variable=var_10)
        audi.grid(row=12,column=6)

        var_11=IntVar(root)

        infiniti=Checkbutton(root,text='Infinity',variable=var_11)
        infiniti.grid(row=12,column=8)

        lt_checkbox=[var_3,var_4,var_5,var_6,var_7,var_8,var_9,var_10,var_11]
        lt_brand_name={f'{var_3}':'Nissan',f'{var_4}':'BMW',f'{var_5}':'Toyota',f'{var_6}':'Chevrolet',f'{var_7}':'Renault',f'{var_8}':'Ford',f'{var_9}':'Hyundai',f'{var_10}':'Audi',f'{var_11}':'Infinity'}
        

        
        

root=Tk()
root.title('Rent a Car')
configureWindow(root,20,20)

label=Label(root,text="NikilSahelMathew enterprises") 
label.grid(row=0,column=9) 

button=Button(root,text='Rent a car')
button.bind('<Button-1>',rent_a_car)
button.grid(row=10,column=5)

button1=Button(root,text='Display clients')
button1.bind('<Button-1>',display_existing_clients)
button1.grid(row=10,column=15)


root.mainloop()

