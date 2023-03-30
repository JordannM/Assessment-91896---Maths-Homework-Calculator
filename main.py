#Maths Calculator - Perimeter and Area of Shapes

#imports
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import math

#window creation
window = tk.Tk()
window.title("Perimeter and Area Calculator of Shapes")
window.geometry("800x500")
window.config(bg="#D3E0E4")
window.resizable(width=False, height=False)


#GUI/drop down list for shape selection

#--design elements for user satisfaction--

title = tk.Label(window, text="Perimeter and Area Calculator!", font=("Georgia", 25, "bold"), fg="#5E737A", bg="#D3E0E4")
#shapes label

select_shape = tk.Label(window, text="Select a shape:",font=("Georgia", 16,"bold"),fg="#5E737A", bg="#D3E0E4")

user_input = ttk.Combobox(window, width=12, state="readonly")

user_input['values'] = ('', 'Triangle' ,'Rectangle' ,'Square' ,'Circle')  #combobox list
                          
#shapes list
shape_list=["", "Triangle", "Rectangle", "Square", "Circle"]

#function for getting shape
def get_shape():
  aShape = user_input.current()
  user_shape = tk.Label(window, text=f"{shape_list[aShape]}", width=12, font=('Georgia', 12, "bold"), fg="#5E737A", bg="#D3E0E4")


  # -- selecting space/none -- #
  if aShape == 0: 
      messagebox.showerror("Invalid input", "Error select a shape")
      return
  
    # --- function triangle perim&area --- #
  if aShape == 1:
      def triExit():
        triangleWindow.destroy()

      print("Triangle")
      triangleWindow = tk.Toplevel()
      triangleWindow.title("**TRIANGLE**")
      triangleWindow.geometry("800x500")
      triangleWindow.config(bg="#D3E0E4")
      triangleWindow.resizable(width=False, height=False)

      user_shape = tk.Label(triangleWindow, text=f"{shape_list[aShape]}", width=10, font=('Georgia', 16, "bold"), fg="#5E737A", bg="#D3E0E4")
      user_shape.place(x=0, y=75)
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

        if (int(triangleSide1) + int(triangleSide2)) <= int(triangleSide3) or (int(triangleSide2) + int(triangleSide3)) <= int(triangleSide1) or (int(triangleSide3) + int(triangleSide1)) <= int(triangleSide2):
          messagebox.showerror("Error", "These side lengths will not create a valid triangle")
          return
    
        #Nested function of Area calculation
        def calculate_triangle_area():
          # Semi Perimeter calculation
          s = (float(triangleSide1) + float(triangleSide2) + float(triangleSide3)) / 2
          area = math.sqrt(s * (s - float(triangleSide1)) * (s - float(triangleSide2)) * (s - float(triangleSide3)))
          return area
          
        # Calculate triangle area and perimeter
        solvedAreaTriangle = calculate_triangle_area()
        solvedAreaTriangle = tk.Label(triangleWindow, text=(f"Area → {solvedAreaTriangle:.2f}"), width=20, font=('Georgia', 15, "bold"), fg="#D3E0E4", bg="#5E737A")
        solvedAreaTriangle.place(x=0, y=300)
        solvedPerimeterTriangle = float(triangleSide1) + float(triangleSide2) + float(triangleSide3)
        solvedPerimeterTriangle = tk.Label(triangleWindow, text=("Perimeter → ", solvedPerimeterTriangle), width=20, font=('Georgia', 15, "bold"), fg="#D3E0E4", bg="#5E737A")
        solvedPerimeterTriangle.place(x=0, y=350)
  

      triangleLabel1 = tk.Label(triangleWindow,text="Triangle side 1 → ", width=17,font=('Georgia', 10, "bold"),fg="#5E737A",bg="#D3E0E4")
      triangleLabel1.place(x=20, y=150)
      triangle1Entry = tk.Entry(triangleWindow, width=10)
      triangle1Entry.place(x=185, y=150)
      
      triangleLabel2 = tk.Label(triangleWindow,text="Triangle side 2 → ", width=17, font=('Georgia', 10, "bold"), fg="#5E737A",bg="#D3E0E4")
      
      triangleLabel2.place(x=20, y=190)
      triangle2Entry = tk.Entry(triangleWindow, width=10)
      triangle2Entry.place(x=185, y=190)
      
      triangleLabel3 = tk.Label(triangleWindow, text="Triangle side 3 → ", width=17,font=('Georgia', 10, "bold"),fg="#5E737A",bg="#D3E0E4")
      
      triangleLabel3.place(x=20, y=230)
      triangle3Entry = tk.Entry(triangleWindow, width=10)
      triangle3Entry.place(x=185, y=230)
      
      TriangleSolveArea = tk.Button(triangleWindow,text="Solve!",font=("Georgia", 16),command=get_triangle)
      TriangleSolveArea.place(x=183, y=70)
      triangleTitle = tk.Label(triangleWindow, text="Perimeter and Area Calculator!", font=("Georgia", 20, "bold"), fg="#5E737A", bg="#D3E0E4")
      triangleTitle.place(x=0, y=10)
      exitButton=tk.Button(triangleWindow,text="← Back to select",font=("Arial",13),command=triExit)
      exitButton.place(x=0,y=400)
# --- function rectangle perim&area --- #                                       
  if aShape == 2:
    print("Rectangle")
    rectangleWindow = tk.Toplevel()
    rectangleWindow.title("**RECTANGLE**")
    rectangleWindow.geometry("800x500")
    rectangleWindow.config(bg="#D3E0E4")
    rectangleWindow.resizable(width=False, height=False)

    user_shape = tk.Label(rectangleWindow, text=f"{shape_list[aShape]}", width=10, font=('Georgia', 16, "bold"), fg="#5E737A", bg="#D3E0E4")
    user_shape.place(x=0, y=75)

    def get_rectangle():
      #Declaring entrybox
      rectangleWidth = rectangle1Entry.get()
      rectangleLength = rectangle2Entry.get()
      #Validating input for rectangle length and width
      if not rectangleLength.isnumeric() or not rectangleWidth.isnumeric():
        messagebox.showerror("Invalid input", "Please enter numeric values for length and width.")
        return

      if float(rectangleLength) <= 0 or float(rectangleWidth) <= 0:
        messagebox.showerror("Invalid input", "Please enter positive values for length and width.")
        return
      
      solvedAreaRectangle = tk.Label(rectangleWindow,text=("Area → ",float(rectangleWidth) * float(rectangleLength)),width=20,font=('Georgia', 15, "bold"),fg="#D3E0E4", bg="#5E737A")
      solvedAreaRectangle.place(x=0, y=350)

      solvedPerimeterRectangle = tk.Label(rectangleWindow, text=("Perimeter → ", float(rectangleWidth) + float(rectangleWidth) + float(rectangleLength) + float(rectangleLength)),width=20, font=('Georgia', 15, "bold"), fg="#D3E0E4", bg="#5E737A")  #Does the calculation for perimeter
      solvedPerimeterRectangle.place(x=0, y=450)

    rectangleLabel1 = tk.Label(rectangleWindow, text="Retangle Width →     ", width=18, font=('Georgia', 10, "bold"), fg="#5E737A", bg="#D3E0E4")
    rectangleLabel1.place(x=20, y=150)
    rectangle1Entry = tk.Entry(rectangleWindow, width=10)
    rectangle1Entry.place(x=185, y=150)

    rectangleLabel2 = tk.Label(rectangleWindow, text="Rectangle Length → ", width=18, font=('Georgia', 10, "bold"), fg="#5E737A", bg="#D3E0E4")
    rectangleLabel2.place(x=20, y=190)
    rectangle2Entry = tk.Entry(rectangleWindow, width=10)
    rectangle2Entry.place(x=185, y=190)

    rectangleSolveArea = tk.Button(rectangleWindow,text="Solve!",font=("Georgia", 16),command=get_rectangle)
    rectangleSolveArea.place(x=183, y=70)
    rectangleTitle = tk.Label(rectangleWindow, text="Perimeter and Area Calculator!", font=("Georgia", 20, "bold"), fg="#5E737A", bg="#D3E0E4")
    rectangleTitle.place(x=0, y=10)


  


# --- function square perim&area --- #
  if aShape == 3:
    print("Square")
    squareWindow = tk.Toplevel()
    squareWindow.title("**RECTANGLE**")
    squareWindow.geometry("800x500")
    squareWindow.config(bg="#D3E0E4")
    squareWindow.resizable(width=False, height=False)

    user_shape = tk.Label(squareWindow, text=f"{shape_list[aShape]}", width=10, font=('Georgia', 16, "bold"), fg="#5E737A", bg="#D3E0E4")
    user_shape.place(x=0, y=75)

    def get_square():
      #Declaring entrybox
      squareWidth = square1Entry.get()
      squareLength = square2Entry.get()

      #Validating input for square length and width
      if not squareLength.isnumeric() or not squareWidth.isnumeric():
        messagebox.showerror("Invalid input", "Please enter numeric values for length and width.")
        return

      if float(squareLength) <= 0 or float(squareWidth) <= 0:
        messagebox.showerror("Invalid input", "Please enter positive values for length and width.")
        return
      
      solvedAreaSquare = tk.Label(squareWindow,text=("Area → ", float(squareWidth) * float(squareLength)),width=20,font=('Georgia', 15, "bold"), fg="#D3E0E4", bg="#5E737A")
      solvedAreaSquare.place(x=0, y=350)
  
      solvedPerimeterSquare = tk.Label(squareWindow,text=("Perimeter → ",float(squareWidth) + float(squareWidth) + float(squareLength) + float(squareLength)),width=20,font=('Georgia', 15, "bold"),fg="#D3E0E4", bg="#5E737A")  #Does the calculation
      solvedPerimeterSquare.place(x=0, y=450)
  
    squareLabel1 = tk.Label(squareWindow,text="Square Width → ",width=17 ,font=('Georgia', 10, "bold"), fg="#5E737A",bg="#D3E0E4")
    squareLabel1.place(x=20, y=150)
    square1Entry = tk.Entry(squareWindow, width=10)
    square1Entry.place(x=185, y=150)
  
    squareLabel2 = tk.Label(squareWindow,text="Square Length → ", width=18,font=('Georgia', 10, "bold"),fg="#5E737A",bg="#D3E0E4")
    squareLabel2.place(x=20, y=190)
    square2Entry = tk.Entry(squareWindow, width=10)
    square2Entry.place(x=185, y=190)
  
    squareSolveArea = tk.Button(squareWindow,text="Solve!",font=("Georgia", 16),command=get_square)
    squareSolveArea.place(x=183, y=70)
    squareTitle = tk.Label(squareWindow, text="Perimeter and Area Calculator!", font=("Georgia", 20, "bold"), fg="#5E737A", bg="#D3E0E4")
    squareTitle.place(x=0, y=10)

# --- function circle perim&area --- #
  if aShape == 4:
    print("Circle")
    circleWindow = tk.Toplevel()
    circleWindow.title("**CIRCLE**")
    circleWindow.geometry("800x500")
    circleWindow.config(bg="#D3E0E4")
    circleWindow.resizable(width=False, height=False)

    user_shape = tk.Label(circleWindow, text=f"{shape_list[aShape]}", width=10, font=('Georgia', 16, "bold"), fg="#5E737A", bg="#D3E0E4")
    user_shape.place(x=0, y=75)
    def get_circle():
      #Declaring entryboxes
      circleRadius = circle1Entry.get()

      #Validating input for circle radius
      if not circleRadius.isnumeric():
        messagebox.showerror("Invalid input", "Please enter numeric values for length and width.")
        return

      if float(circleRadius) <= 0:
        messagebox.showerror("Invalid input", "Please enter positive values for length and width.")
        return
      
      solvedAreaCircle = tk.Label(circleWindow,text=("Area → ", math.pi * float(circleRadius)** 2 ),width=20,font=('Georgia', 15, "bold"), fg="#D3E0E4", bg="#5E737A")
      solvedAreaCircle.place(x=0, y=350)
      solvedCircumferenceCircle = tk.Label(circleWindow,text=("Circumference → ", math.pi * (2 * float(circleRadius)) ),width=20,font=('Georgia', 15, "bold"), fg="#D3E0E4", bg="#5E737A")
      solvedCircumferenceCircle.place(x=0,y=450)


    circleLabel1 = tk.Label(circleWindow,text="Circle Radius → ",width=17 ,font=('Georgia', 10, "bold"), fg="#5E737A",bg="#D3E0E4")
    circleLabel1.place(x=20, y=150)
    circle1Entry = tk.Entry(circleWindow, width=10)
    circle1Entry.place(x=185, y=150)

    circleSolveArea = tk.Button(circleWindow,text="Solve!",font=("Georgia", 16),command=get_circle)
    circleSolveArea.place(x=183, y=70)
    circleTitle = tk.Label(circleWindow, text="Perimeter and Area Calculator!", font=("Georgia", 20, "bold"), fg="#5E737A", bg="#D3E0E4")
    circleTitle.place(x=0, y=10)
    
  
#buttons -- confirm
button_confirm = tk.Button(window,text="Confirm shape.",font=("Georgia",13),command=get_shape)
#placements -- confirm
select_shape.place(x=150,y=250)
user_input.place(x=360, y=256)
button_confirm.place(x=280, y=300)
title.place(x=100, y=200)