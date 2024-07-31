def main():
    expression = input("Expression: ")

    num1, operator, num2 = expression.split()

    num1 = int(num1)
    num2 = int(num2)

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error divedi by 0")
            return
    else:
        print("Error: Invalid operator!")
        return

    # Formatting the result to one decimal place as a string
    formatted_result = "{:.1f}".format(result)

    # Printing the formatted result
    print(formatted_result)

if __name__ == "__main__":
    main()
