# Importing necessary libraries
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Setting up Main Window
root = Tk()
root.title("Denomination Calculator")
root.geometry("650x450")
root.configure(bg="green1")

# Adding Image and Labels in the Main Window
cash_img = Image.open("app_img.jpeg")
cash_img = cash_img.resize((300, 300))
cash_image = ImageTk.PhotoImage(cash_img)

lbl1 = Label(root, image=cash_image, )
lbl1.place(x=180, y=20)

lbl2 = Label(root, text="Hey! Welcome to Denomination Calculator App", bg="orange", font=("Calibri", 14))
lbl2.place(relx=0.22, y=340)

# Function to display a messagebox and proceed if OK is clicked
def msg(): 
    msg = messagebox.showinfo("Alert", "Do you want to calculate the denomination")
    if msg == "ok":
        top_win()

# Adding Buttons to the main window
btn1 = Button(root, text="Let's get started", command=msg, bg="IndianRed1")
btn1.place(x=260, y=380)

# Function for opening new/top window
def top_win():
    top = Toplevel()
    top.geometry("600x350+50+50")
    top.title("Denomination Calculator")
    top.configure(bg="orange")

    # Centering Widgets in the Top Window
    top_lbl1 = Label(top, text="Enter the total amount", bg="yellow", fg="red", relief="ridge")
    entry = Entry(top)
    top_lbl2 = Label(top, text="Here are the number of notes for each denomination", bg="green3", fg="gray99", relief="groove")
    nl1 = Label(top, text="₹2000", bg="yellow", fg="red", relief="ridge", font=("Lucida Console", 9), height=1)
    nl2 = Label(top, text="₹500", bg="yellow", fg="red", relief="ridge", font=("Lucida Console", 9), height=1)
    nl3 = Label(top, text="₹100", bg="yellow", fg="red", relief="ridge", font=("Lucida Console", 9), height=1)
    e1 = Entry(top)
    e2 = Entry(top)
    e3 = Entry(top)
    def deno():
        try:
            global amount
            amount = int(entry.get())
            no2000 = amount // 2000
            amount %= 2000
            no500 = amount // 500
            amount %= 500
            no100 = amount // 100
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e1.insert(0, str(no2000))
            e2.insert(0, str(no500))
            e3.insert(0, str(no100))
        except ValueError:
            messagebox.showerror("Error", "Please Enter a Valid Number")
    cal_btn = Button(top, text="Calculate", bg="white", fg="black", command=deno)
    top_lbl1.place(x=230, y=20)
    entry.place(x=230, y=50)
    cal_btn.place(x=260, y=80)
    top_lbl2.place(x=150, y=160)
    nl1.place(x=150, y=200)
    e1.place(x=300, y=200)
    nl2.place(x=155, y=240)
    e2.place(x=300, y=240)
    nl3.place(x=155, y=280)
    e3.place(x=300, y=280)

root.mainloop()