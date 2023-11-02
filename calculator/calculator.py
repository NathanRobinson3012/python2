print ("welcome to this calculator please enter one of the following options")
run = True

while run:
    calculation = input("""please select a calculation
     to add enter '+'
    to subtract enter '-'
    to multiply enter '*'
    to divide enter '/'
    to do to the power of enter '^'
    to exit, enter 'q'                    
    to use pythagoras enter 'p'
    please enter here :""")

    inputs = ["+","-","*","/","^"]

    if calculation in inputs:
        print(f"please enter the numbers in the order num1, the operation (+-*/^), num2")
        num1=float(input("please enter the first number "))
        num2 = float(input("please enter the second number"))
        print (f"{num1}{calculation}{num2}=")
        match calculation:
            case "+":
                print(num1+num2)
            case "-":
                print (num1-num2)
            case "*":
                print (num1*num2)
            case "/":
                print(num1/num2)
            case "^":
                print(num1**num2)
                
    elif calculation=="q":
        run=False
        
    elif calculation=="p":
        print("for a triangle of hight A, width B and hypotenuse C")
        side = input("using the other 2, are you trying to find A,B or C")
        try:
            match side.upper():
                case "A":
                    C=float(input("please enter the hypotenus C"))
                    B=float(input("please enter the width B"))
                    if C>B:
                        print(f"A has a length {(C**2-B**2)**0.5}")
                    else:
                        print("C must be larger than B")
                
                case "B":
                    C=float(input("please enter the hypotenus C"))
                    A=float(input("please enter the height A"))
                    if C>A:
                        print(f"B has a length {(C**2-A**2)**0.5}")
                    else:
                        print("C must be larger than A")
                
                case "C":
                    A=float(input("please enter the height A"))
                    B=float(input("please enter the width B"))
                    print(f"C has a length {(A**2+B**2)**0.5}")
                    
        except:
            print("there was an error please try again")
            
    else:
        print ("the details entered were not valid please try again")