#Maths Calculator - Perimeter and Area of Shapes

#imports
import tkinter as tk
#from tkinter import messagebox - may use a at a later date
#from tkinter import ttk - ""

#window creation
window = tk.Tk()
window.title("Perimeter and Area Calculator of Shapes")
window.geometry("475x300")
window.config(bg="#FFB6C1")
window.resizable(width=False, height=False)

#GUI
user_input = tk.Entry(window)
user_input.pack()

#shapes list
shape_list=[("Triangle", "Rectangle", "Square", "Circle")]

#functions


#calculator

#design elements for user satisfaction
select_shape = tk.Label(window,text="Select a shape:",font=("Georgia", 12,"bold"),fg="#B2AC88", bg="#FFB6C1")

select_shape.place(x=30,y=80)
user_input.place(x=180, y=80)
