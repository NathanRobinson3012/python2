import statistics as stat

data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

grades = data.split(",")
'''
for i in range (len(grades)):
    grades[i]=int(grades[i])
    '''

grades = list(map(int, grades))

maximum=max(grades)
minimum=min(grades)
print(f"max value is {maximum} and min value is {minimum}")

average =round((sum(grades)/len(grades)),2)

print(f"the average of grades is {average}")

mean = stat.mean(grades)
medium=stat.median(grades)

final="the min grade is {0:.2f} and the max is {1:.2f}. the average i calculated is {2:.2f} while stat says it is {3:.2f} and the medium is {4:.2f}"

print(final.format(minimum,maximum,average,mean,medium))