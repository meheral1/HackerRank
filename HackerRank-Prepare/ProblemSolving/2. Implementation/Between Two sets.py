def getTotalX(a,b):
    counter = 0
    for x in range(1, max(b) + 1):
        condition1 = True
        for i in a:
            if x%i!=0:
                condition1 = False
                break
        condition2=True
        for j in b:
            if j%x!=0:
                condition2 = False
                break
        if condition1 and condition2:
            counter+=1
        
    return counter
        

a = [2,6]
b = [24,36]
print(getTotalX(a,b))