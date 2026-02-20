def divisiblesumpair(n,k,ar):
    counter=0
    for i in range(n):
        for j in range(i+1,n):
            if (ar[i]+ar[j])%k==0:
                counter+=1
    return counter

ar = [1,2,3,4,5,6]
n = len(ar)
k = 5
print(divisiblesumpair(n,k,ar))

