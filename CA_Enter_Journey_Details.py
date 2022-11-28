from tkinter import *
from tkinter import messagebox as mb
root=Tk()
h=root.winfo_screenheight()
w=root.winfo_screenwidth()
root.geometry("%dx%d+0+0"%(w,h))
#Function for 'Show Bus'
def show():
    #Attributes
    Label(options,text="Select Bus", fg="green", font=("Arial Bold", 15)).grid(row=2,column=0, pady=40)
    Label(options,text="Operator", fg="green", font=("Arial Bold", 15)).grid(row=2,column=1)
    Label(options,text="Bus Type", fg="green", font=("Arial Bold", 15)).grid(row=2,column=2, padx=10)
    Label(options,text="Availability/Capacity", fg="green", font=("Arial Bold", 15)).grid(row=2,column=3)
    Label(options,text="Fare", fg="green", font=("Arial Bold", 15)).grid(row=2,column=4)
    
    #Query Result
    b=IntVar()
    boption=Radiobutton(options,text="Bus1", variable=b, value=1, bg="lightblue" , font=("Arial Bold", 15)).grid(row=3,column=0, pady=10)
    Label(options,text="Kamla", fg="blue", font=("Arial Bold", 15)).grid(row=3,column=1)
    Label(options,text="AC 2x2", fg="blue", font=("Arial Bold", 15)).grid(row=3,column=2)
    Label(options,text="25/30", fg="blue", font=("Arial Bold", 15)).grid(row=3,column=3)
    Label(options,text="1000", fg="blue", font=("Arial Bold", 15)).grid(row=3,column=4)
    proceed=Button(options, text="Proceed to Book", bg="seagreen2" , command=bticket, font=15).grid(row=3, column=6)

#Ticket Confirmation Dialog box
def farediag():
    mb.askyesno("Fare Confirm", message="Total Amount to be paid is Rs 3000.00")

#Function to "book ticket"
def bticket():
    Label(root, text="Fill Passenger Details to book the bus ticket", font=("Arial Bold", 30), fg="red", bg="lightblue").grid(row=4, column=0, columnspan=8, pady=30)
    book=Frame(root)
    Label(book, text="Name", font=15).grid(row=0, column=0, padx=10)
    name=Entry(book, font=15).grid(row=0, column=1, padx=10)
    Label(book, text="Gender", font=15).grid(row=0, column=2, padx=10)
    gender_var=StringVar()
    gender_var.set("Male")
    gender=OptionMenu(book, gender_var, "Male", "Female")
    gender.config(font="Arial 15")
    gender.grid(row=0, column=3, padx=20)
    Label(book, text="No of Seats", font=15).grid(row=0,column=4, padx=10)
    seats=Entry(book , width=3, font=15).grid(row=0, column=5,padx=30)
    Label(book, text="Mobile No", font=15).grid(row=0,column=6, padx=10)
    mobile=Entry(book, font=15).grid(row=0, column=7, padx=10)
    Label(book, text="Age", font=15).grid(row=0,column=8, padx=10)
    age=Entry(book , width=3, font=15).grid(row=0, column=9, padx=10)
    book_button=Button(book, text="Book Seat" , command=farediag, font=15).grid(row=0, column=10, padx=10)
    book.grid(row=5, column=0)


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
Label(options, text="To", font=("Arial Bold", 15)).grid(row=0, column=0, padx=5)
start=Entry(options ).grid(row=0, column=1)
Label(options, text="From", font=("Arial Bold", 15)).grid(row=0, column=2, padx=5)
end=Entry(options, width=25 ).grid(row=0, column=3)
Label(options, text="Journey Date", font=("Arial Bold", 15)).grid(row=0, column=4, padx=5)
date=Entry(options ).grid(row=0, column=5)
show=Button(options, text="Show Bus", bg="springgreen3", font=("Arial Bold", 15), command=show).grid(row=0, column=6, padx=5)
hm=PhotoImage(file="./assets/home.png")
home=Button(options, image=hm).grid(row=0, column=7, padx=5)
options.grid(row=3, column=0)
root.mainloop()