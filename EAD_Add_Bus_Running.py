from tkinter import *
from tkinter import messagebox as mb
root=Tk()
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))

#Add Bus Running Details function
def add_bd():
    if True:
        Label(options, text="7 22/12/2022 2").grid(row=1,column=0, columnspan=11)
        mb.showinfo("Bus Running Details Entry", message="Bus Running Record Added")
    else:
        mb.showerror("DB insertion Error", message="Bus Record Already Exists")

#edit Bus Details funtion
def edit_bop():
    if True:
        Label(options, text="7 22/1/2023 30").grid(row=1,column=0, columnspan=11)
        mb.showinfo("Bus Running Entry Updated", message="Bus Running Record updated Successfully")
    else:
        mb.showerror("Record Not Found", message="Bus Running Record does not Exists")

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
Label(root, text="Add Bus Running Details", fg="green", font=("Arial Bold", 30)).grid(row=2, column=0, pady=30)

options=Frame(root)
Label(options, text="Bus id", font=("Arial", 15)).grid(row=0, column=0, padx=5)
bid=Entry(options, width=5, font=("Arial", 15)).grid(row=0, column=1, padx=5)
Label(options, text="Running Name", font=("Arial", 15)).grid(row=0, column=2, padx=5)
rdate=Entry(options, width=25, font=("Arial", 15)).grid(row=0, column=3, padx=5)
Label(options, text="Seat Available", font=("Arial", 15)).grid(row=0, column=4, padx=5)
seat=Entry(options, font=("Arial", 15)).grid(row=0, column=5, padx=5)
addr=Button(options, text="Add Run", bg="#97ffa0", font=("Arial", 15)).grid(row=0, column=6, padx=5)
editr=Button(options, text="Edit Run", bg="#97ffa0", font=("Arial", 15)).grid(row=0, column=7, padx=5)
hm=PhotoImage(file="./assets/home.png")
home=Button(options, image=hm).grid(row=1, column=6, pady=30)
options.grid(row=3, column=0, pady=50)

root.mainloop()