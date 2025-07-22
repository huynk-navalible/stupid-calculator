import tkinter as tk
from tkinter import font as tkFont
import math

def calculate():
    try:
        numbers = [float(n) for n in entry_numbers.get().split()]
        op = operator.get()
        result = None

        if op == "+":
            result = sum(numbers)
        elif op == "-":
            result = numbers[0]
            for n in numbers[1:]:
                result -= n
        elif op == "*":
            result = 1
            for n in numbers:
                result *= n
        elif op == "/" or op == ":":
            result = numbers[0]
            for n in numbers[1:]:
                if n == 0:
                    result_label.config(text="im not bugging out bc of u do it urself")
                    return
                result /= n
        elif op == "sqrt" or op == "square root":
            result = [round(math.sqrt(n), 2) for n in numbers]
        else:
            result_label.config(text="if u r typing squareroot pls just type it with spaces vro")
            return

        result_label.config(text=f"Result: {round(result, 2) if isinstance(result, float) else result}")

    except ValueError:
        result_label.config(text="i dont think you typed numbers...")

# pi multiply by user input
def pmtp_gui():
    try:
        so = float(solieu.get())
        ketqua = round(math.pi * so, 5)
        ketqua_nhan.config(text=f"pi * {so} = {ketqua}")
    except ValueError:
        ketqua_nhan.config(text="why do u want me to do ts vro")

# GUI setup
root = tk.Tk()
root.title("my stupid calculator")
root.configure(bg="#1e1e1e")

bigFont = tkFont.Font(family="Liberation Mono", size=23)
dRkM = "#1e1e1e"
lGhM = "#ffffff"
OoLC = "#00ffcc"
sObN = "#444444"

tk.Label(root, text="choose ur operator (+, -, *, /, sqrt):\n", bg=dRkM, fg=OoLC, font=bigFont).pack()
operator = tk.Entry(root, font=bigFont, bg="#2e2e2e", fg=lGhM, insertbackground=lGhM)
operator.pack(pady=10)

tk.Label(root, text="type numbers pls (separated by spaces):\n", bg=dRkM, fg=OoLC, font=bigFont).pack()
entry_numbers = tk.Entry(root, width=40, font=bigFont, bg="#2e2e2e", fg=lGhM, insertbackground=lGhM)
entry_numbers.pack(pady=10)

tk.Button(root, text="Calculate pls", command=calculate, font=bigFont, bg=sObN, fg=lGhM, activebackground="#616161", activeforeground=lGhM).pack(pady=10)
result_label = tk.Label(root, font=bigFont, text="u havent calculated this yet vro", bg=dRkM, fg=OoLC)
result_label.pack(pady=10)

ketqua_nhan = tk.Label(root, font=bigFont, text="\n enter the number that u wanna multiply by pi", bg=dRkM, fg=OoLC)
solieu = tk.Entry(root, font=bigFont, bg="#2e2e2e", fg=lGhM, insertbackground=lGhM)
solieu.pack(pady=10)
ketqua_nhan.pack(pady=10)

# the pi funcion
tk.Button(root, text="pi * ur number", command=pmtp_gui, font=bigFont, bg=sObN, fg=lGhM).pack(pady=10)

root.mainloop()
