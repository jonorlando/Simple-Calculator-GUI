# Importing the required module for GUI creation
import tkinter as tk
from tkinter import StringVar

# Create the main application window
main_window = tk.Tk()

# Set up the initial size of the calculator window (width x height)
main_window.geometry('312x324')

# Set the title that appears in the window's title bar
main_window.title('My_Calculator')

# Global variables to manage the calculator's state
expression = ""  # Stores the current mathematical expression as a string
input_text = StringVar()  # Special Tkinter variable that automatically updates the display

# Function to handle number and operator button clicks
def btn_click(item):
    global expression
    # Append the clicked button's value to the current expression
    expression = expression + str(item)
    # Update the display to show the current expression
    input_text.set(expression)

# Function to clear the calculator's input field and reset the expression
def btn_clear():
    global expression
    # Reset the expression to empty string
    expression = ""
    # Clear the display
    input_text.set("")

# Function to evaluate the mathematical expression and display the result
def btn_equal():
    global expression
    try:
        # Evaluate the mathematical expression using Python's eval() function
        result = str(eval(expression))
        # Display the calculated result
        input_text.set(result)
        # Reset the expression for new calculations
        expression = ""
    except:
        # Handle any errors that occur during evaluation (division by zero, invalid syntax, etc.)
        input_text.set('Error')
        # Reset the expression after an error
        expression = ""

# Creating frames to organize the calculator interface into logical sections

# Top frame: Contains the display where numbers and results are shown
input_frame = tk.Frame(main_window, width=312, height=50, bd=0, highlightbackground='black',
                       highlightcolor='black', highlightthickness=1)
# Position the input frame at the top of the main window
input_frame.pack(side='top')

# Create an Entry widget (input field) for displaying the current expression and results
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'),
                       textvariable=input_text, width=50, bg="#eee", bd=0, justify='right')

# Position the input field within the input_frame using grid layout
input_field.grid(row=0, column=0)
# Add internal padding to make the display area taller and more visible
input_field.pack(ipady=10)

# Bottom frame: Contains all the calculator buttons arranged in a grid
btns_frame = tk.Frame(main_window, width=312, height=272.5, bg="grey")
# Position the buttons frame below the input frame
btns_frame.pack()

# First row of buttons: Clear button (spans 3 columns) and Division button
btn_clearing = tk.Button(btns_frame, text="Clear", fg="black", width=32, height=3, bd=0,
                       cursor="hand2", command=btn_clear)
# Position the Clear button to span across first three columns
btn_clearing.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

# Division operator button
btn_div = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee",
                  cursor="hand2", command=lambda: btn_click("/"))
# Position the Division button in the fourth column
btn_div.grid(row=0, column=3, padx=1, pady=1)

# Second row: Number buttons 7, 8, 9 and Multiplication operator
# Each button is created and positioned in a single line for compact code
tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee",
          cursor="hand2", command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

# Third row: Number buttons 4, 5, 6 and Subtraction operator
tk.Button(btns_frame, text='4', fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
tk.Button(btns_frame, text='5', fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
tk.Button(btns_frame, text='6', fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
tk.Button(btns_frame, text='-', fg="black", width=10, height=3, bd=0, bg="#eee",
          cursor="hand2", command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

# Fourth row: Number buttons 1, 2, 3 and Addition operator
tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee",
          cursor="hand2", command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

# Fifth and final row: Zero button (spans 2 columns), Decimal point, and Equals button
tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee",
          cursor="hand2", command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee",
          cursor="hand2", command=btn_equal).grid(row=4, column=3, padx=1, pady=1)

# Start the Tkinter event loop to display the window and handle user interactions
main_window.mainloop()
