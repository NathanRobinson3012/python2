ALLOWANCE = 11850
TAXLIM1=34500
TAXLIM2=150000
BRACKET1=0.2
BRACKET2=0.4
BRACKET3=0.45

def GetIncomeTax (salary):
    tax=0.0
    if salary<=ALLOWANCE:
        print("income within personal allowence")
        
    elif ALLOWANCE<salary<=TAXLIM1:
        tax+=(salary-ALLOWANCE)*BRACKET1
        
    elif TAXLIM1<salary<=TAXLIM2:
        tax += (TAXLIM1-ALLOWANCE)*BRACKET1
        tax += (salary-TAXLIM1+1)*BRACKET2
        
    elif salary>TAXLIM2:
        tax+=(TAXLIM1-ALLOWANCE)*BRACKET1
        tax+=(TAXLIM2-TAXLIM1)*BRACKET2
        tax+=(salary-TAXLIM2)*BRACKET3
        
    return tax


salary=int(input("enter your income in whole pounds :£"))
print("you will pay £{0:.2f} in tax".format(GetIncomeTax(salary)))