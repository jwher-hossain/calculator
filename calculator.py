while True:
        num1 = input("Enter first number (or type 'exit' to quit): ")
        if num1.lower() == "exit":
            print("Calculator stopped. Good bye.")
            break
        num1 = int(num1)
        oparetor = input("Enter an oparetor (+, -, *, /)")
        num2 = int(input("Enter second number: "))
        if oparetor == "+":
             result = num1 + num2
        elif oparetor == "-":
             result = num1 - num2
        elif oparetor == "*":
            result = num1 * num2
        elif oparetor == "/":
            if num2 != 0:
                 result = num1 / num2
            else:
                print("Error Division by zero is not allowed.")
                continue
        else:
            print("Invalid Oparetor. Try again.")
            continue
        
        print(f"{num1} {oparetor} {num2} = {result}")           

       


   

































































                                          


    

    
