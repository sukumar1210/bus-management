from tkinter import *
from tkinter import messagebox as mb
root=Tk()
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))

#Add Bus Route Details function
def add_bd():
    if True:
        Label(options, text="7 Ruthiyai 5").grid(row=1,column=0, columnspan=11)
        mb.showinfo("Bus Route Details Entry", message="Bus Route Record Added")
    else:
        mb.showerror("DB insertion Error", message="Bus Route Record Already Exists")

#edit Bus Details funtion
def edit_bop():
    if True:
        Label(options, text="9 Ruthiyai 2").grid(row=1,column=0, columnspan=11)
        mb.showinfo("Bus Route Entry Updated", message="Bus Route Record updated Successfully")
    else:
        mb.showerror("Record Not Found", message="Bus Route Record does not Exists")

#basic Headings
bus=PhotoImage(file="./assets/Bus_for_project.png")
Label(root, image=bus).grid(row=0, column=0)
H=Label(root, text="Online Bus Booking System", fg="red", bg="lightblue", font=("Arial Bold", 40))
H.grid(row=1, column=0)
root.update()
a=w-H.winfo_width()
H.destroy()
H=Label(root, text="Online Bus Booking System", fg="red", bg="lightblue", font=("Arial Bold", 40))
H.grid(row=1, column=0, padx=a//2)

#Add Bus Operator Details to the Database
Label(root, text="Add Bus Route Details", fg="green", font=("Arial Bold", 30)).grid(row=2, column=0, pady=30)

options=Frame(root)
Label(options, text="Route id", font=("Arial", 15)).grid(row=0, column=0, padx=5)
rid=Entry(options, width=5, font=("Arial", 15)).grid(row=0, column=1, padx=5)
Label(options, text="Station Name", font=("Arial", 15)).grid(row=0, column=2, padx=5)
sname=Entry(options, width=25, font=("Arial", 15)).grid(row=0, column=3, padx=5)
Label(options, text="Station Id", font=("Arial", 15)).grid(row=0, column=4, padx=5)
Sid=Entry(options, font=("Arial", 15)).grid(row=0, column=5, padx=5)
Label(options, font=("Arial", 15)).grid(row=0, column=6, padx=40)
add=Button(options, text="Add Route", bg="#97ffa0", font=("Arial", 15)).grid(row=0, column=7, padx=5)
delete=Button(options, text="Delete Route", bg="#97ffa0", fg="red", font=("Arial", 15)).grid(row=0, column=8, padx=5)
hm=PhotoImage(file="./assets/home.png")
home=Button(options, image=hm).grid(row=1, column=6, pady=30)
options.grid(row=3, column=0, pady=50)

root.mainloop()