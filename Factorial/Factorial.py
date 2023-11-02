from sys import set_int_max_str_digits

selecting=True
max = 150000
set_int_max_str_digits(1000000) 
while selecting:
    try:
        factorial = int(input("Please enter the number you want the factorial of"))
        if 0<=factorial<=max:
            selecting = False
        else:
            print("this number is invalid, please try again")
    
    except:
        print("invalid input. a facotial must always be formed from an integer")
        
# first with a while loop.

print("with a while loop")

x=0
total = 1
while x!=factorial:
    x+=1
    total*=x
    #print (total)
    
print(f"using the while loop we get{total}"+"\n\n")

print("with a for loop")
sum = 1
for i in range (factorial):
    sum*=(i+1)
    #print (sum)
    
print(f"using the for loop we get {sum}\n\n\n")

print(f"the length of this number in digits is {len(str(sum))}")