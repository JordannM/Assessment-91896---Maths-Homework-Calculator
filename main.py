#Maths Calculator - Perimeter and Area of Shapes

#imports
import tkinter as tk
#from tkinter import messagebox
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

#shapes label

select_shape = tk.Label(window,text="Select a shape:",font=("Georgia", 12,"bold"),fg="#5E737A", bg="#D3E0E4")

user_input = ttk.Combobox(window, width=12, state="readonly")

user_input['values'] = ('', 'Triangle' ,'Rectangle' ,'Square' ,'Circle')  #combobox list
                          
#shapes list
shape_list=["", "Triangle", "Rectangle", "Square", "Circle"]

#function for getting shape
def get_shape():
  aShape = user_input.current()
  user_shape = tk.Label(window, text=f"{shape_list[aShape]}", width=15, font=('Georgia', 12, "bold"), fg="#5E737A", bg="#D3E0E4")
  user_shape.place(x=0, y=60)



  # --- function triangle perim&area ---
  if aShape == 1:
    print("Triangle")
  
    def get_triangle():
      def calculate_triangle_area(triangleSide1, triangleSide2, triangleSide3): #Nested function
        #Semi Perimeter calculation
        s =(float(triangleSide1.get()) + float(triangleSide2.get()) + float(triangleSide3.get())) / 2
  
        area = math.sqrt(s * (s - float(triangleSide1.get())) * (s - float(triangleSide2.get())) * (s - float(triangleSide3.get())))
  
        return area
  
      area = calculate_triangle_area(triangleSide1, triangleSide2, triangleSide3)
      solvedAreaTriangle = tk.Label(window,text=(f"Area --> {area:.2f}"),width=50,font=('Georgia', 10, "bold"),fg="white",  bg="#111121")
      solvedAreaTriangle.place(x=0, y=250)
      print(f"{area:.2f}")

      solvedPerimeterTriangle = tk.Label(window,text=("Perimeter --> ", float(triangleSide1.get()) + float(triangleSide2.get()) + float(triangleSide3.get())), width=50, font=('Georgia', 10, "bold"),fg="white", bg="#111121")  #Does the calculation
      solvedPerimeterTriangle.place(x=0, y=300)

    triangleLabel1 = tk.Label(window,text="Triangle side 1 --> ", width=17,font=('Georgia', 10, "bold"),fg="white",bg="#111121")

    triangleLabel1.place(x=20, y=100)
    triangleSide1 = tk.Entry(window, width=10)
    triangleSide1.place(x=185, y=100)

    triangleLabel2 = tk.Label(window,text="Triangle side 2 --> ", width=17, font=('Georgia', 10, "bold"), fg="white",bg="#111121")

    triangleLabel2.place(x=20, y=150)
    triangleSide2 = tk.Entry(window, width=10)
    triangleSide2.place(x=185, y=150)

    triangleLabel3 = tk.Label(window, text="Triangle side 3 --> ", width=17,font=('Georgia', 10, "bold"),fg="white",bg="#111121")
  
    triangleLabel3.place(x=20, y=200)
    triangleSide3 = tk.Entry(window, width=10)
    triangleSide3.place(x=185, y=200)

    TriangleSolveArea = tk.Button(window,text="solve!",font=("Arial", 13),command=get_triangle)
    TriangleSolveArea.place(x=300, y=125)

# --- function rectangle perim&area                                        
  if aShape == 2:
    print("Rectangle")
  
    def get_rectangle():
      solvedAreaRectangle = tk.Label(window,text=("Area --> ",float(rectangleWidth.get()) * float(rectangleLength.get())),width=50,font=('Georgia', 10, "bold"),fg="white", bg="#5E737A")
      solvedAreaRectangle.place(x=0, y=200)

      solvedPerimeterRectangle = tk.Label(window, text=("Perimeter --> ", float(rectangleWidth.get()) + float(rectangleWidth.get()) + float(rectangleLength.get()) + float(rectangleLength.get())),width=50, font=('Georgia', 10, "bold"), fg="white", bg="#5E737A")  #Does the calculation for perimeter
      solvedPerimeterRectangle.place(x=0, y=250)

    rectangleLabel1 = tk.Label(window, text="Retangle Width --> ", width=18, font=('Georgia', 10, "bold"), fg="white", bg="#5E737A")
    rectangleLabel1.place(x=20, y=100)
    rectangleWidth = tk.Entry(window, width=10)
    rectangleWidth.place(x=185, y=100)

    rectangleLabel2 = tk.Label(window, text="Rectangle Length --> ", width=18, font=('Georgia', 10, "bold"), fg="white", bg="#5E737A")
    rectangleLabel2.place(x=20, y=150)
    rectangleLength = tk.Entry(window, width=10)
    rectangleLength.place(x=185, y=150)

    rectangleSolveArea = tk.Button(window,text="solve!",font=("Arial", 13),command=get_rectangle)
    rectangleSolveArea.place(x=300, y=125)


  


# --- function square perim&area
  
#buttons -- confirm
button_confirm = tk.Button(window,text="Confirm shape.",font=("Georgia",10),command=get_shape)
#placements -- confirm
select_shape.place(x=5,y=10)
user_input.place(x=150, y=12)
button_confirm.place(x=280, y=5)