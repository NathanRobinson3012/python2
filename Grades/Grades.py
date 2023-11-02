run = True
while run:

    try:
        score = int(input("please enter the score"))
    except:
        print("Error in the input, please enter a number only")
        break
    

    level=input("please enter the students level")
    if level=="1":
        if 1<=score<50:
            print("fail")
        elif 50<=score<=60:
            print("pass")
        elif 61<=score<=70:
            print("merit")
        elif 71<=score<=100:
            print("distinction")
        else:
            print("number not in range")
            
    elif level =="2":
        if 1<=score<40:
            print("fail")
        elif 40<=score<=50:
            print("pass")
        elif 51<=score<=65:
            print("merit")
        elif 66<=score<=100:
            print("distinction")
        else:
            print("number not in range")
    