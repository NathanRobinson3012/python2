word = input("please enter your word(s) to check: ")
count = 0
for c in word:
    if c.lower() in ["a","e","i","o","u"]:
        count+=1
        
print (count)