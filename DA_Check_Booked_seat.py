from tkinter import *
from tkinter import messagebox as mb
root=Tk()
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))

#Function to check the ticket
def chk_tkt():
    if True:
        ticket=Frame(root, borderwidth=5, relief="ridge")
        Label(ticket, text="Passengers: Mahesh Kumar", font=("Arial Bold", 15)).grid(row=0,column=0)
        Label(ticket, text="No of Seats: 3", font=("Arial Bold", 15)).grid(row=1,column=0)
        Label(ticket, text="Age: 45", font=("Arial Bold", 15)).grid(row=2,column=0)
        Label(ticket, text="Booking Ref: 9", font=("Arial Bold", 15)).grid(row=3,column=0)
        Label(ticket, text="Travel On: 24/12/2022", font=("Arial Bold", 15)).grid(row=4,column=0)
        Label(ticket, text="Gender Male", font=("Arial Bold", 15)).grid(row=5,column=0)
        Label(ticket, text="Phon3: 9988776655", font=("Arial Bold", 15)).grid(row=0,column=1)
        Label(ticket, text="Fare Rs: 3000.00 *", font=("Arial Bold", 15)).grid(row=1,column=1)
        Label(ticket, text="Bus Details: Kamla", font=("Arial Bold", 15)).grid(row=2,column=1)
        Label(ticket, text="Booked On: Oct31 2022", font=("Arial Bold", 15)).grid(row=3,column=1)
        Label(ticket, text="Boarding Point: Guna", font=("Arial Bold", 15)).grid(row=4,column=1)
        Label(ticket, text="*Total amount Rs 3000.00/- to be paid at the time of Boarding the Bus", font=10).grid(row=6,column=0, columnspan=2)
        ticket.grid(row=5,column=0, pady=10)
    else:
        mb.askyesno("No Booking Record", message="Do you wabt to book seat now?")

#Basic Headings
bus=PhotoImage(file="./assets/Bus_for_project.png")
Label(root, image=bus).grid(row=0, column=0)
h=Label(root, text="Online Bus Booking System", bg="Lightblue", fg="red", font=("Arial Bold", 40))
h.grid(row=0, column=0)
root.update()
a=w-h.winfo_width()
h.destroy()
h=Label(root, text="Online Bus Booking System", bg="Lightblue", fg="red", font=("Arial Bold", 40))
h.grid(row=1, column=0, padx=a//2)

#options
Label(root, text="Check your Booking", fg="green4", bg="springgreen2", font=("Arial Bold", 20)).grid(row=2, column=0, pady=40)
phone=Frame(root)
Label(phone, text="Enter Your Mobile No:", font=("Arial Bold", 15)).grid(row=0, column=0, padx=10)
phn=Entry(phone, font=("Arial Bold", 15)).grid(row=0, column=1, padx=10)
check=Button(phone, text="Check Booking", font=("Arial Bold", 20), command=chk_tkt).grid(row=0, column=3, padx=10)
phone.grid(row=3,column=0)

root.mainloop()