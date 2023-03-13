#Maths Calculator - Perimeter and Area of Shapes

#imports
import tkinter as tk
#from tkinter import messagebox
from tkinter import ttk

#window creation
window = tk.Tk()
window.title("Perimeter and Area Calculator of Shapes")
window.geometry("500x300")
window.config(bg="#D3E0E4")
window.resizable(width=False, height=False)

#function
def get_shape():
  aShape = user_input.current()
  user_shape = tk.Label(window, text=f"{shape_list[aShape]}", width=15, font=('Georgia', 12, "bold"), fg="#5E737A", bg="#D3E0E4")
  user_shape.place(x=0, y=60)

#GUI/drop down list for shape selection
user_input = ttk.Combobox(window, width=12, state="readonly")

user_input['values'] = ('Circle' ,'Square' ,'Rectangle' ,'triangle')  #combobox list
                          

#shapes list
shape_list=["Circle", "Square", "Rectangle", "Triangle"]

#design elements for user satisfaction
#shapes label
select_shape = tk.Label(window,text="Select a shape:",font=("Georgia", 12,"bold"),fg="#5E737A", bg="#D3E0E4")
#buttons -- confirm
button_confirm = tk.Button(window,text="Confirm shape.",font=("Georgia",10),command=get_shape)

select_shape.place(x=5,y=10)
user_input.place(x=150, y=12)
button_confirm.place(x=280, y=5)
