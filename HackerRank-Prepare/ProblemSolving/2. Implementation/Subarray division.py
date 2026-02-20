def birthday(s,d,m):
    counter=0
    for i in range(len(s)):
        if sum(s[i:i+m])==d:
            counter+=1
    return counter

s = [2,2,1,3,2]
d = 4
m = 2
print(birthday(s,d,m))
