#!/run/current-system/sw/bin/env python3
# the import thing (dont read this line)
import math
import argparse

# for the debug flag
parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true', help='uses the debug mode')
args = parser.parse_args()

# the first part
bitch = input("choose pls (+,-,*,/ or sqrt )\n")
wth = input("enter the number (seperate it by spaces vro):\n").split()

try:
    numbers = [float(w) for w in wth]

    if args.debug:
        print("\n== DEBUG MODE ==")
        print("Operator chosen:", bitch)
        print("Input numbers:", numbers)

    # the second part
    def calculate(bitch, wth):
        if bitch == "+":
            return sum(wth)
        elif bitch == "-":
            result = wth[0]
            for num in wth[1:]:
                result -= num
            return result
        elif bitch == "*":
            result = 1
            for num in wth:
                result *= num
            return result
        elif bitch == "/" or bitch == ":":
            result = wth[0]
            for num in wth[1:]:
                if num == 0:
                    return "idk do it urself im not going to bug out bc of u"
                result /= num
            return result
        elif bitch == "sqrt" or bitch == "square root":
            return [round(math.sqrt(n), 2) for n in wth]
        else:
            return "i think you didnt hear my yapping [im crying huhu]"

    output = calculate(bitch, numbers)
    print("\nThe Result for the thing u want to calculate is", output)

except ValueError:
    print("What did u just typed in ???")
