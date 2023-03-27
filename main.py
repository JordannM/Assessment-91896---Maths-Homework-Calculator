#Maths Calculator - Perimeter and Area of Shapes

#imports
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import math

#window creation
window = tk.Tk()
window.title("Perimeter and Area Calculator of Shapes")
window.geometry("500x300")
window.config(bg="#D3E0E4")
window.resizable(width=False, height=False)
window.attributes('-fullscreen', True)

#GUI/drop down list for shape selection

#--design elements for user satisfaction--

title = tk.Label(window, text="Perimeter and Area Calculator!", font=("Georgia", 20, "bold"), fg="#5E737A", bg="#D3E0E4")
#shapes label

select_shape = tk.Label(window, text="Select a shape:",font=("Georgia", 12,"bold"),fg="#5E737A", bg="#D3E0E4")

user_input = ttk.Combobox(window, width=12, state="readonly")

user_input['values'] = ('', 'Triangle' ,'Rectangle' ,'Square' ,'Circle')  #combobox list
                          
#shapes list
shape_list=["", "Triangle", "Rectangle", "Square", "Circle"]

#function for getting shape
def get_shape():
  aShape = user_input.current()
  user_shape = tk.Label(window, text=f"{shape_list[aShape]}", width=12, font=('Georgia', 12, "bold"), fg="#5E737A", bg="#D3E0E4")
  user_shape.place(x=0, y=90)

  # -- selecting space/none -- #
  if aShape == 0: 
    messagebox.showerror("Invalid input", "Error select a shape")
    return

  # --- function triangle perim&area --- #
  if aShape == 1:
    print("Triangle")
  
    def get_triangle():
    #Declaring entrybox
      triangleSide1 = triangle1Entry.get()
      triangleSide2 = triangle2Entry.get()
      triangleSide3 = triangle3Entry.get()

    # Validate input for triangle side lengths
      if not triangleSide1.isnumeric() or not triangleSide2.isnumeric() or not triangleSide3.isnumeric():
        messagebox.showerror("Invalid input", "Please enter numeric values for all sides.")
        return
      
      if float(triangleSide1) <= 0 or float(triangleSide2) <= 0 or float(triangleSide3) <= 0:
        messagebox.showerror("Invalid input", "Please enter positive values for all sides.")
        return
  
      #Nested function of Area calculation
      def calculate_triangle_area():
        # Semi Perimeter calculation
        s = (float(triangleSide1) + float(triangleSide2) + float(triangleSide3)) / 2
        area = math.sqrt(s * (s - float(triangleSide1)) * (s - float(triangleSide2)) * (s - float(triangleSide3)))
        return area
        
      # Calculate triangle area and perimeter
      area = calculate_triangle_area()
      solvedAreaTriangle = tk.Label(window, text=(f"Area → {area:.2f}"), width=20, font=('Georgia', 15, "bold"), fg="#D3E0E4", bg="#5E737A")
      solvedAreaTriangle.place(x=0, y=300)
      perimeter = float(triangleSide1) + float(triangleSide2) + float(triangleSide3)
      solvedPerimeterTriangle = tk.Label(window, text=("Perimeter → ", perimeter), width=20, font=('Georgia', 15, "bold"), fg="#D3E0E4", bg="#5E737A")
      solvedPerimeterTriangle.place(x=0, y=350)


  triangleLabel1 = tk.Label(window,text="Triangle side 1 → ", width=17,font=('Georgia', 10, "bold"),fg="#5E737A",bg="#D3E0E4")



  isnum = tk.Label(window,text='')
  isnum.place(x=400,y=150)
  
  triangleLabel1.place(x=20, y=130)
  triangle1Entry = tk.Entry(window, width=10)
  triangle1Entry.place(x=185, y=130)
  
  triangleLabel2 = tk.Label(window,text="Triangle side 2 → ", width=17, font=('Georgia', 10, "bold"), fg="#5E737A",bg="#D3E0E4")
  
  triangleLabel2.place(x=20, y=170)
  triangle2Entry = tk.Entry(window, width=10)
  triangle2Entry.place(x=185, y=170)
  
  triangleLabel3 = tk.Label(window, text="Triangle side 3 → ", width=17,font=('Georgia', 10, "bold"),fg="#5E737A",bg="#D3E0E4")
  
  triangleLabel3.place(x=20, y=210)
  triangle3Entry = tk.Entry(window, width=10)
  triangle3Entry.place(x=185, y=210)
  
  TriangleSolveArea = tk.Button(window,text="Solve!",font=("Georgia", 13),command=get_triangle)
  TriangleSolveArea.place(x=450, y=50)
    
# --- function rectangle perim&area --- #                                       
  if aShape == 2:
    print("Rectangle")
  
    def get_rectangle():
      solvedAreaRectangle = tk.Label(window,text=("Area → ",float(rectangleWidth.get()) * float(rectangleLength.get())),width=20,font=('Georgia', 15, "bold"),fg="#D3E0E4", bg="#5E737A")
      solvedAreaRectangle.place(x=0, y=350)

      solvedPerimeterRectangle = tk.Label(window, text=("Perimeter → ", float(rectangleWidth.get()) + float(rectangleWidth.get()) + float(rectangleLength.get()) + float(rectangleLength.get())),width=20, font=('Georgia', 15, "bold"), fg="#D3E0E4", bg="#5E737A")  #Does the calculation for perimeter
      solvedPerimeterRectangle.place(x=0, y=450)

    rectangleLabel1 = tk.Label(window, text="Retangle Width →     ", width=18, font=('Georgia', 10, "bold"), fg="#5E737A", bg="#D3E0E4")
    rectangleLabel1.place(x=20, y=130)
    rectangleWidth = tk.Entry(window, width=10)
    rectangleWidth.place(x=185, y=130)

    rectangleLabel2 = tk.Label(window, text="Rectangle Length → ", width=18, font=('Georgia', 10, "bold"), fg="#5E737A", bg="#D3E0E4")
    rectangleLabel2.place(x=20, y=170)
    rectangleLength = tk.Entry(window, width=10)
    rectangleLength.place(x=185, y=170)

    rectangleSolveArea = tk.Button(window,text="Solve!",font=("Georgia", 13),command=get_rectangle)
    rectangleSolveArea.place(x=450, y=50)


  


# --- function square perim&area --- #
  if aShape == 3:
    print("Square")

    def get_square():
      solvedAreaSquare = tk.Label(window,text=("Area → ", float(squareWidth.get()) * float(squareLength.get())),width=20,font=('Georgia', 15, "bold"), fg="#D3E0E4", bg="#5E737A")
      solvedAreaSquare.place(x=0, y=350)
  
      solvedPerimeterSquare = tk.Label(window,text=("Perimeter → ",float(squareWidth.get()) + float(squareWidth.get()) + float(squareLength.get()) + float(squareLength.get())),width=20,font=('Georgia', 15, "bold"),fg="#D3E0E4", bg="#5E737A")  #Does the calculation
      solvedPerimeterSquare.place(x=0, y=450)
  
    squareLabel1 = tk.Label(window,text="Square Width → ",width=17 ,font=('Georgia', 10, "bold"), fg="#5E737A",bg="#D3E0E4")
    squareLabel1.place(x=20, y=130)
    squareWidth = tk.Entry(window, width=10)
    squareWidth.place(x=185, y=130)
  
    squareLabel2 = tk.Label(window,text="Square Length → ", width=18,font=('Georgia', 10, "bold"),fg="#5E737A",bg="#D3E0E4")
    squareLabel2.place(x=20, y=170)
    squareLength = tk.Entry(window, width=10)
    squareLength.place(x=185, y=170)
  
    squareSolveArea = tk.Button(window,text="Solve!",font=("Georgia", 13),command=get_square)
    squareSolveArea.place(x=450, y=50)

# --- function circle perim&area --- #
  if aShape == 4:
    print("Circle")

    def get_circle():
      solvedAreaCircle = tk.Label(window,text=("Area → ", math.pi * float(circleRadius.get())** 2 ),width=20,font=('Georgia', 15, "bold"), fg="#D3E0E4", bg="#5E737A")
      solvedAreaCircle.place(x=0, y=350)
      solvedCircumferenceCircle = tk.Label(window,text=("Circumference → ", math.pi * (2 * float(circleRadius.get())) ),width=20,font=('Georgia', 15, "bold"), fg="#D3E0E4", bg="#5E737A")
      solvedCircumferenceCircle.place(x=0,y=450)


    circleLabel1 = tk.Label(window,text="Circle Radius → ",width=17 ,font=('Georgia', 10, "bold"), fg="#5E737A",bg="#D3E0E4")
    circleLabel1.place(x=20, y=130)
    circleRadius = tk.Entry(window, width=10)
    circleRadius.place(x=185, y=130)

    circleSolveArea = tk.Button(window,text="Solve!",font=("Georgia", 13),command=get_circle)
    circleSolveArea.place(x=450, y=50)

    
  
#buttons -- confirm
button_confirm = tk.Button(window,text="Confirm shape.",font=("Georgia",13),command=get_shape)
#placements -- confirm
select_shape.place(x=5,y=60)
user_input.place(x=153, y=62)
button_confirm.place(x=280, y=50)
title.place(x=0, y=10)