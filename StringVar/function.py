#learning how to create functions in python #
from tkinter import messagebox


def alkindy(first_number, second_number):
    sum1 = first_number + second_number
    messagebox.showinfo("Functions", sum1)


#alkindy(4, 5)
def return_values(x):
    return 350 * x


messagebox.showinfo("FUnctions example", return_values(5))
