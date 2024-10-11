num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
symbols = str(input("What operation would you like to use: "))

match symbols:
    case "+":
        result = num1 + num2
        print("The total is:", result)
    case "-":
        result2 = num1 - num2 
        print("The total is: ", result2)
    case "*":
        result3 = num1 * num2
        print("The total is: ", result3)
    case "/":
        result4 = num1 / num2
        print("The total is: ", result4)
    case "%":
        result5 = num1 % num2
        print("The total is: ", result5)
    case "^":
        result6 = num1 ^ num2
        print("The total is: ", result6)
    case _:
        print("Application is closing")
        break