n=[50,40,23,56,70,12,5,10,7]
i=0
max=0
while i<len(n):
    if n[i]>max:
        secondmax=max
        max=n[i]
    i+=1
print(secondmax)