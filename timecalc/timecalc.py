from decimal import ROUND_DOWN


while True:
    select = (input('''hello and welcome to the time calculator, please select an option
    1-	Add 2 times   
    2-	Find the difference between 2 times  
    3-	Convert to Hours  
    4-	Convert to Minutes  
    5-	Convert Minutes to Time  
    6-	Convert Hours to Time  
    7-	Convert Days to Time  
    8-	Exit  

    Enter an option:  
          '''))

    match(select):
        case "1":
            time1=input("please enter the first day time in the format dd:hh:mm").split(":")
            time2=input("please enter a second time in the same format").split(":")
            result=[]
            result.append(int(time1[0])+int(time2[0]))
            result.append(int(time1[1])+int(time2[1]))
            result.append(int(time1[2])+int(time2[2]))
            if result[2]>60:
                result[2]-=60
                result[1]+=1
                
            if result[1]>24:
                result[1]-=24
                result[0]+=1
                
            print (f"{result[0]}:{result[1]}:{result[2]}")
            
        case "2":
            time1=input("please enter the first (larger) day time in the format dd:hh:mm").split(":")
            time2=input("please enter a second time in the same format").split(":")
            result.append(int(time1[0])-int(time2[0]))
            result.append(int(time1[1])-int(time2[1]))
            result.append(int(time1[2])-int(time2[2]))
            if result[2]<0:
                result[1]-=1
                result[2]+=60
            if result[1]<0:
                result[0]-=1
                result[1]+=24
                
            print(result[0]+":"+result[1]+":"+result[2])
                
        case "3":
            time1=input("please enter the first day time in the format dd:hh:mm").split(":")
            hours=float(int(time1[0])*24 + int(time1[1]) + int(time1[2])/60 )
            print (hours)
            
        case "4":
            time1=input("please enter the first day time in the format dd:hh:mm").split(":")
            mins=int(int(time1[0])*24*60 + int(time1[1])*60 + int(time1[2]))
            print(mins)
            
        case "5":
            mins=float(input("enter the number of mins"))
            hours=0
            days=0
            while mins>=60:
                mins-=60
                hours+=1
                
            while hours>=24:
                hours -=24
                days +=1
                
            print(f"{days}:{hours}:{mins}")
            
        case "6":
            hours = float(input("enter number of hours"))
            mins=0
            days=0
            whole=ROUND_DOWN(hours)
            while hours >=24:
                hours-=24
                days+=1
                
            print(f"{days}:{whole}:{(hours-whole)*60}")
            
        case "7":
            days = float (input("enter number days"))
            hours=0
            mins=0
            wholeDay=ROUND_DOWN(days)
            hours=(days-wholeDay)*24
            wholeHour=ROUND_DOWN(hours)
            mins=(hours-wholeHour)*60
            print(f"{wholeDay}:{wholeHour}:{mins}")
            
        case "8":
            exit()
            
        case _:
            print("error invalid input")