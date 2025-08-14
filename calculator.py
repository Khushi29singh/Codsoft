import customtkinter as ctk
from tkinter import END, messagebox

# Functions
def clear():
    entryField.delete(0, END)

def click(number):
    entryField.insert(END, number)

def answer():
    expression = entryField.get()
    try:
        result = eval(expression)
        ans = round(result, 2)
        entryField.delete(0, END)
        entryField.insert(0, ans)
    except SyntaxError:
        messagebox.showerror("Error", "Invalid expression")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")

# Main Window
root = ctk.CTk()
root.title("Calculator")
root.geometry("300x400")
ctk.set_appearance_mode("light")  # Simple light theme

# Entry field
entryField = ctk.CTkEntry(
    root,
    font=("Arial", 20),
    justify="right",
    width=260,
    height=50,
    corner_radius=5
)
entryField.grid(row=0, column=0, padx=20, pady=20, columnspan=4)

# Function to create buttons
def create_button(text, command, row, col, colspan=1):
    ctk.CTkButton(
        root,
        text=text,
        font=("Arial", 16),
        width=60 * colspan,
        height=40,
        fg_color="#e0e0e0",
        hover_color="#cfcfcf",
        text_color="black",
        corner_radius=5,
        command=command
    ).grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)

# Buttons layout (clean arrangement)
buttons = [
    ('7', lambda: click('7'), 1, 0), ('8', lambda: click('8'), 1, 1), ('9', lambda: click('9'), 1, 2), ('+', lambda: click('+'), 1, 3),
    ('4', lambda: click('4'), 2, 0), ('5', lambda: click('5'), 2, 1), ('6', lambda: click('6'), 2, 2), ('-', lambda: click('-'), 2, 3),
    ('1', lambda: click('1'), 3, 0), ('2', lambda: click('2'), 3, 1), ('3', lambda: click('3'), 3, 2), ('*', lambda: click('*'), 3, 3),
    ('0', lambda: click('0'), 4, 0), ('.', lambda: click('.'), 4, 1), ('C', clear, 4, 2), ('/', lambda: click('/'), 4, 3),
    ('%', lambda: click('%'), 5, 0), ('=', answer, 5, 1, 3)
]

# Create all buttons
for btn in buttons:
    create_button(*btn)

# Keyboard binding
def key_input(event):
    key = event.char
    if key in '0123456789.+-*/%':
        click(key)
    elif event.keysym == 'Return':
        answer()
    elif event.keysym in ['BackSpace', 'Delete']:
        current = entryField.get()
        entryField.delete(0, END)
        entryField.insert(0, current[:-1])
    elif key.lower() == 'c':
        clear()

root.bind('<Key>', key_input)
root.mainloop()
