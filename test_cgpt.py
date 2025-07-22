import math
import argparse
import tkinter as tk
from tkinter import messagebox

# --- Command line setup ---
parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true', help='uses the debug mode')
args = parser.parse_args()

# --- Console calculator ---
def console_calc():
    op = input("choose pls (+,-,*,/ or sqrt)\n")
    raw = input("enter the number (separate it by spaces vro):\n").split()

    try:
        nums = [float(x) for x in raw]

        if args.debug:
            print("ure on test mode")
            print("choose the operator (i hope ure not slow like a snail)")
            print("numbers received:", nums)

        def calculate(op, nums):
            if op == "+":
                return sum(nums)
            elif op == "-":
                result = nums[0]
                for n in nums[1:]:
                    result -= n
                return result
            elif op == "*":
                result = 1
                for n in nums:
                    result *= n
                return result
            elif op in ["/", ":"]:
                result = nums[0]
                for n in nums[1:]:
                    if n == 0:
                        return "division by 0 vro"
                    result /= n
                return result
            elif op in ["sqrt", "square root"]:
                return [round(math.sqrt(n), 2) for n in nums]
            else:
                return "idk what u meant"
        
        print("Result is:", calculate(op, nums))

    except ValueError:
        print("what did u just type in ???")

# --- GUI calculator ---
def gui_calc():
    root = tk.Tk()
    root.title("Vro Calculator")
    root.configure(bg="#2b2b2b")

    def gui_style(widget):
        widget.configure(
            bg="#2b2b2b",
            fg="#f0f0f0",
            insertbackground="white",
            highlightbackground="#444",
            font=("Helvetica", 12)
        )

    def pmtp_gui():
        try:
            val = float(entry.get())
            result = math.pi * val
            result_label.config(text=f"π × {val} = {round(result, 5)}")
        except ValueError:
            result_label.config(text="why do u want me to do ts vro")

    def calculate_gui():
        try:
            raw = entry.get()
            op = operator.get().strip()
            nums = [float(x) for x in raw.split()]

            if op == "+":
                res = sum(nums)
            elif op == "-":
                res = nums[0]
                for n in nums[1:]:
                    res -= n
            elif op == "*":
                res = 1
                for n in nums:
                    res *= n
            elif op in ["/", ":"]:
                res = nums[0]
                for n in nums[1:]:
                    if n == 0:
                        result_label.config(text="division by zero vro")
                        return
                    res /= n
            elif op in ["sqrt", "square root"]:
                res = [round(math.sqrt(n), 2) for n in nums]
            else:
                result_label.config(text="invalid operator")
                return

            result_label.config(text=f"Result: {res}")

        except ValueError:
            result_label.config(text="u gave me bad input 😭")

    # --- GUI widgets ---
    entry = tk.Entry(root, width=40)
    gui_style(entry)
    entry.pack(pady=10)

    operator = tk.Entry(root, width=20)
    gui_style(operator)
    operator.insert(0, "+")  # default operator
    operator.pack(pady=5)

    calc_btn = tk.Button(root, text="Calculate", command=calculate_gui, bg="#444", fg="white", font=("Helvetica", 12))
    calc_btn.pack(pady=5)

    pi_btn = tk.Button(root, text="π × number", command=pmtp_gui, bg="#555", fg="white", font=("Helvetica", 12))
    pi_btn.pack(pady=5)

    result_label = tk.Label(root, text="", bg="#2b2b2b", fg="white", font=("Helvetica", 13))
    result_label.pack(pady=10)

    root.mainloop()

# --- Main ---
if __name__ == "__main__":
    print("choose mode vro:\n1. CLI\n2. GUI")
    mode = input("enter 1 or 2: ").strip()

    if mode == "1":
        console_calc()
    elif mode == "2":
        gui_calc()
    else:
        print("u typed smth wrong")
