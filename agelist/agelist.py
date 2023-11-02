#from socket import ALG_SET_AEAD_ASSOCLEN


ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

length = len(ages)
print("ages as default")
for x in ages:
    print(x)

print("\n\nadd 1 to all ages \n\n")

for i in range(length):
    ages[i]+=1
    
for x in ages:
    print(x)
    
print("\n\n remove all values outside of range \n\n")
'''
for i in range (length):
    if ages[i]<16 or ages[i]>65:
        del(ages[i])
        length-=1
'''
#^^ was recieving out of range errors. unsure why but found alternative


index =0  
while index<length:
    if (ages[index]<16 or ages[index]>65):
        del(ages[index])
        length-=1
        index-=1
    index+=1

for x in ages:
    print(x)
    
count=0
print("\n\n\n")
for x in ages:
    if 16<=x<=25:
        count+=1
        
print(count)

ages.sort()
print("\n\n")
print (ages)

print("\n\n")

print(f"the proportion of 16-25 year olds is {count}/{length}={count/length}")