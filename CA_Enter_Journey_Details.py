import sqlite3
from datetime import date
tdate=date.today()
print(tdate)
from tkinter import *
from tkinter import messagebox as mb
conn=sqlite3.Connection("bus_booking.db")
cur=conn.cursor()
root=Tk()
h=root.winfo_screenheight()
w=root.winfo_screenwidth()
root.geometry("%dx%d+0+0"%(w,h))

#Connection Function
def home():
    root.destroy()
    import B


#Function for 'Show Bus'
def show():
    for i in options.winfo_children():
        i.destroy()
    #Function to transfer data to bticket function
    def transfer():
        if b.get()==0:
            mb.showerror("Select Bus", message="No Bus Selected")
        else:
            bticket(b.get(),istart, idate)
    
    #Attributes
    Label(options,text="Select Bus", fg="green", font=("Arial Bold", 15)).grid(row=2,column=0, pady=40, padx=20)
    Label(options,text="Operator", fg="green", font=("Arial Bold", 15)).grid(row=2,column=1, padx=20)
    Label(options,text="Bus Type", fg="green", font=("Arial Bold", 15)).grid(row=2,column=2, padx=20)
    Label(options,text="Availability/Capacity", fg="green", font=("Arial Bold", 15)).grid(row=2,column=3, padx=20)
    Label(options,text="Fare", fg="green", font=("Arial Bold", 15)).grid(row=2,column=4, padx=20)
    
    #Dummy Data
    # b=IntVar()
    # boption=Radiobutton(options,text="Bus1", variable=b, value=1, bg="lightblue" , font=("Arial Bold", 15)).grid(row=3,column=0, pady=10)
    # Label(options,text="Kamla", fg="blue", font=("Arial Bold", 15)).grid(row=3,column=1)
    # Label(options,text="AC 2x2", fg="blue", font=("Arial Bold", 15)).grid(row=3,column=2)
    # Label(options,text="25/30", fg="blue", font=("Arial Bold", 15)).grid(row=3,column=3)
    # Label(options,text="1000", fg="blue", font=("Arial Bold", 15)).grid(row=3,column=4)
    # proceed=Button(options, text="Proceed to Book", bg="seagreen2" , command=bticket, font=15).grid(row=3, column=6)
    
    
    #Query Result
    istart=start.get()
    iend=end.get()
    idate=date.get()
    data=cur.execute("""
                     select ONAME, TYPE, SEAT_AVAIL, FARE, BUS.BUSID
                     from OPERATOR, BUS, ROUTE AS start, ROUTE AS end, RUNS 
                     WHERE start.SNAME='{}'
                     AND end.SNAME='{}'
                     AND start.SID<end.SID
                     AND start.ROUTEID=end.ROUTEID
                     AND RUNS.DATE='{}'
                     AND BUS.BUSID=RUNS.BUSID
                     AND BUS.OPID=OPERATOR.OPID
                     AND SEAT_AVAIL>0
                     """.format(istart, iend, idate))
    data=data.fetchall()
    print(data)
    b=IntVar()
    i=0
    for i in range(len(data)):
        print("in for")
        boption=Radiobutton(options,text="{}".format("Bus"+str(i+1)), variable=b, value=data[i][4], bg="lightblue" , font=("Arial Bold", 15)).grid(row=i+3,column=0, pady=10)
        Label(options,text="{}".format(data[i][0]), fg="blue", font=("Arial Bold", 15)).grid(row=i+3,column=1)
        Label(options,text="{}".format(data[i][1]), fg="blue", font=("Arial Bold", 15)).grid(row=i+3,column=2)
        Label(options,text="{}".format(data[i][2]), fg="blue", font=("Arial Bold", 15)).grid(row=i+3,column=3)
        Label(options,text="{}".format(data[i][3]), fg="blue", font=("Arial Bold", 15)).grid(row=i+3,column=4)
    proceed=Button(options, text="Proceed to Book", bg="seagreen2" , command=transfer, font=15).grid(row=i+3, column=6)

    

    

#Function to "book ticket"
def bticket(bid, board, board_date):
    # Function to show confirmed Ticket
    def confirmed():
        phn_no=mobile.get()
        root.destroy()
        conf=Tk()
        w=conf.winfo_screenwidth()
        h=conf.winfo_screenheight()
        conf.geometry("%dx%d+0+0"%(w,h))

        #basic Headings
        bus=PhotoImage(file="./assets/Bus_for_project.png")
        Label(conf, image=bus).grid(row=0, column=0)
        H=Label(conf, text="Online Bus Booking System", fg="red", bg="lightblue", font=("Arial Bold", 40))
        H.grid(row=1, column=0)
        conf.update()
        a=w-H.winfo_width()
        H.destroy()
        H=Label(conf, text="Online Bus Booking System", fg="red", bg="lightblue", font=("Arial Bold", 40))
        H.grid(row=1, column=0, padx=a//2)

        #Ticket Information
        try:
            data=cur.execute("SELECT * FROM BOOKING_HISTORY WHERE REF_NO={}".format(phn_no))
            userdata=data.fetchall()
        except:
            mb.showerror("Invalid Input", message="Unacceptable Input.")
        print("out of if")
        if len(userdata)!=0:
            print("inside if", len(userdata))
            for i in range(len(userdata)):
                data=cur.execute("SELECT * FROM BUS WHERE BUSID={}".format(userdata[i][3]))
                busdata=data.fetchall()
                data=cur.execute("SELECT ONAME FROM OPERATOR WHERE OPID={}".format(busdata[0][4]))
                odata=data.fetchall()
                ticket=Frame(conf, borderwidth=5, relief="ridge")
                Label(ticket, text="Passengers: {}".format(userdata[i][1]), font=("Arial Bold", 15)).grid(row=0,column=0)
                Label(ticket, text="No of Seats: {}".format(userdata[i][4]), font=("Arial Bold", 15)).grid(row=1,column=0)
                Label(ticket, text="Age: {}".format(userdata[i][7]), font=("Arial Bold", 15)).grid(row=2,column=0)
                Label(ticket, text="Phone: {}".format(userdata[i][0]), font=("Arial Bold", 15)).grid(row=3,column=0)
                Label(ticket, text="Travel On: {}".format(userdata[i][6]), font=("Arial Bold", 15)).grid(row=4,column=0)
                Label(ticket, text="Gender: {}".format(userdata[i][2]), font=("Arial Bold", 15)).grid(row=5,column=0)
                # Label(ticket, text="Booking Ref: 9", font=("Arial Bold", 15)).grid(row=0,column=1)
                Label(ticket, text="Fare Rs: {} *".format(busdata[0][3]*userdata[i][4]), font=("Arial Bold", 15)).grid(row=1,column=1)
                Label(ticket, text="Bus Details: {}".format(odata[0][0]), font=("Arial Bold", 15)).grid(row=2,column=1)
                Label(ticket, text="Booked On: {}".format(userdata[i][5]), font=("Arial Bold", 15)).grid(row=3,column=1)
                Label(ticket, text="Boarding Point: {}".format(userdata[i][8]), font=("Arial Bold", 15)).grid(row=4,column=1)
                Label(ticket, text="*Total amount Rs {}/- to be paid at the time of Boarding the Bus".format(busdata[0][3]*userdata[i][4]), font=10).grid(row=6,column=0, columnspan=2)
                ticket.grid(row=2, column=0)
                Label(conf, text="Pess Any Key To Continue.", font=("Arial, Bold", 15)).grid(row=3, column=0, pady=30)
                mb.showinfo("Success", message="Seat Booked")
                def dummy(temp=0):
                    conf.destroy()
                    import B
                conf.bind("<KeyPress>", dummy)
        conf.mainloop()
    #Query
    def add_Bhistory():
        try:
            cur.execute("insert into BOOKING_HISTORY values({}, '{}', '{}', {}, {}, '{}', '{}', {}, '{}')".format(mobile.get(), name.get(), gender_var.get(), bid, seats.get(), tdate, board_date, age.get(), board))
            cur.execute("update RUNS SET SEAT_AVAIL=SEAT_AVAIL-{} where BUSID={} and DATE='{}'".format(seats.get(), bid, board_date))
            conn.commit()
            confirmed()
        except:
            mb.showerror("Failure", message="Invalid Input")
    #Ticket Confirmation Dialog box
    def farediag():
        fare=cur.execute("Select FARE from BUS where BUSID={}".format(bid))
        fare=fare.fetchall()
        flag=mb.askyesno("Fare Confirm", message="Total Amount to be paid is Rs {}".format(fare[0][0]*int(seats.get())))
        if flag:
            add_Bhistory()
    print(bid, board, board_date)
    
    
    Label(root, text="Fill Passenger Details to book the bus ticket", font=("Arial Bold", 30), fg="red", bg="lightblue").grid(row=5, column=0, columnspan=8, pady=30)
    book=Frame(root)
    Label(book, text="Name", font=15).grid(row=0, column=0, padx=10)
    name=Entry(book, font=15)
    name.grid(row=0, column=1, padx=10)
    Label(book, text="Gender", font=15).grid(row=0, column=2, padx=10)
    gender_var=StringVar()
    gender_var.set("Male")
    gender=OptionMenu(book, gender_var, "Male", "Female")
    gender.config(font="Arial 15")
    gender.grid(row=0, column=3, padx=20)
    Label(book, text="No of Seats", font=15).grid(row=0,column=4, padx=10)
    seats=Entry(book , width=3, font=15)
    seats.grid(row=0, column=5,padx=30)
    Label(book, text="Mobile No", font=15).grid(row=0,column=6, padx=10)
    mobile=Entry(book, font=15)
    mobile.grid(row=0, column=7, padx=10)
    Label(book, text="Age", font=15).grid(row=0,column=8, padx=10)
    age=Entry(book , width=3, font=15)
    age.grid(row=0, column=9, padx=10)
    book_button=Button(book, text="Book Seat" , command=farediag, font=15).grid(row=0, column=10, padx=10)
    book.grid(row=6, column=0)


#Basic Heading
bus=PhotoImage(file="./assets/Bus_for_project.png")
Label(root, image=bus).grid(row=0, column=0)
#rendering the widget once
a=Label(root, text="Online Bus Booking System", bg="light blue", fg="red",font=("Arial Bold", 40))
a.grid(row=1, column=0,padx=w//3)
#calculating the right amount of padding with respect of the width with which the widget is rendered
root.update()
x=w-a.winfo_width()
a.destroy() #destroying the widget
#creating the widget again with right amount of padding with centered position for every screen
a=Label(root, text="Online Bus Booking System", bg="light blue", fg="red",font=("Arial Bold", 40))
a.grid(row=1, column=0,padx=x//2)

#Heading for The Page
Label(root, text="Enter Journey Details", fg="green4", bg="springgreen2", font=("Arial Bold", 20)).grid(row=2, column=0, pady=30)

#Frame for Options
options=Frame(root)
option1=Frame(root)
Label(option1, text="To", font=("Arial Bold", 15)).grid(row=0, column=0, padx=5)
start=Entry(option1 )
start.grid(row=0, column=1)
Label(option1, text="From", font=("Arial Bold", 15)).grid(row=0, column=2, padx=5)
end=Entry(option1, width=25 )
end.grid(row=0, column=3)
Label(option1, text="Journey Date", font=("Arial Bold", 15)).grid(row=0, column=4, padx=5)
date=Entry(option1 )
date.grid(row=0, column=5)
show=Button(option1, text="Show Bus", bg="springgreen3", font=("Arial Bold", 15), command=show).grid(row=0, column=6, padx=5)
hm=PhotoImage(file="./assets/home.png")
homeb=Button(option1, image=hm, command=home).grid(row=0, column=7, padx=5)
option1.grid(row=3, column=0)
options.grid(row=4, column=0)
root.mainloop()
conn.commit()
conn.close()