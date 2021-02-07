import tkinter.messagebox
from tkinter import *

window = Tk()
window.title("Shipley Painters")
window.geometry('700x420')


#title

Label(window, text = "Shipley painters", font = "arial" ).grid(row = 1, column = 14, padx=10, pady=20)


#The different grids

Label(window, text = "Name and E-mail", fg = "dim grey").grid(row = 2, column = 1)

Label(window, text = "Name:").grid(row = 3)
name = Entry(window)
name.grid(row = 3, column = 1, padx=12, pady=12)

Label(window, text = "Email:").grid(row = 4)
height = Entry(window)
height.grid(row = 4, column = 1, padx=10, pady=10)



#Length

Label(window, text = "Length of walls", fg = "dim grey").grid(row = 2, column = 14)

Label(window, text = "Length 1:").grid(row = 3, column = 13)
length1 = Entry(window)
length1.grid(row = 3, column = 14, padx=10, pady=10)

Label(window, text = "Length 2:").grid(row = 4, column = 13)
length2 = Entry(window)
length2.grid(row = 4, column = 14, padx=10, pady=10)

Label(window, text = "Length 3:").grid(row = 5, column = 13)
length3 = Entry(window)
length3.grid(row = 5, column = 14, padx=10, pady=10)

Label(window, text = "Length 4:").grid(row = 6, column = 13)
length4 = Entry(window)
length4.grid(row = 6, column = 14, padx=10, pady=10)


#Height
Label(window, text = "Height of walls", fg = "dim grey").grid(row = 2, column = 16)

Label(window, text = "Height:").grid(row = 3, column = 15)
height = Entry(window)
height.grid(row = 3, column = 16,  padx=10, pady=15)


#The options
paint_choice = IntVar()
paint_choice.set(2)
Radiobutton(window, text = "Luxury", variable = paint_choice, value = 1).grid(row = 12, column = 13, padx=12, pady=12)
Radiobutton(window, text = "Standard", variable = paint_choice, value = 2).grid(row = 12, column = 14, padx=12, pady=12)
Radiobutton(window, text = "Economy", variable = paint_choice, value = 3).grid(row = 12, column = 15, padx=12, pady=12)


#Undercoat option
use_undercoat = IntVar()
undercoat = Checkbutton(window, text = "Undercoat", variable = use_undercoat)
undercoat.grid(row = 13, column = 14, padx=12, pady=12)

#Calculation
def perform_calc():
    print(use_undercoat.get())

    paint_quality = paint_choice.get()
    area1 = int(height.get()) * int(length1.get())
    area2 = int(height.get()) * int(length2.get())
    area3 = int(height.get()) * int(length3.get())
    area4 = int(height.get()) * int(length4.get())
    area = int(area1) + int(area2) + int(area3) + int(area4)
    print_cost = 0
    if paint_quality == 1:
       paint_cost = 1.90
    elif paint_quality == 2:
       paint_cost = 1.00
    else:
       paint_cost = 0.60

    if use_undercoat.get():
        paint_cost += 0.50

    total_paint_cost = paint_cost * area

    itemised_total = f"total area = {area} \n" #appears in the message box
    itemised_total += f"Paint cost = {total_paint_cost}" #appears in the message box

#Message box
    tkinter.messagebox.showinfo("Alert Message", itemised_total)


tkinter.Button(window, text = "Calculate", bg = "light grey", command = perform_calc).grid(row = 15, column = 14)


window.mainloop()
