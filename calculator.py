"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    user_input = input("Enter your equation > ")
    tokens = user_input.split(" ")
    
    #print(tokens)     # Testing to see if variable works

    if tokens[0] == "q":
        print("You have exited the calculator!")
        break
    
    else:
        
        if tokens[0] == "+":
            print(add(float(tokens[1]), float(tokens[2])))
        
        elif tokens[0] == "-":
            print(subtract(float(tokens[1]), float(tokens[2])))

        elif tokens[0] == "*":
            print(multiply(float(tokens[1]), float(tokens[2])))

        elif tokens[0] == "/":
            print(divide(float(tokens[1]), float(tokens[2])))

        elif tokens[0] == "square":
            print(square(float(tokens[1])))

        elif tokens[0] == "cube":
            print(cube(float(tokens[1])))
        
        elif tokens[0] == "pow":
            print(power(float(tokens[1]), float(tokens[2])))

        elif tokens[0] == "mod":
            print(mod(float(tokens[1]), float(tokens[2])))