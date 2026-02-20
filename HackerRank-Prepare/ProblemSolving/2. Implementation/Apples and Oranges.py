# countApplesAndOranges has the following parameter(s):
# s: integer, starting point of Sam's house location.
# t: integer, ending location of Sam's house location.
# a: integer, location of the Apple tree.
# b: integer, location of the Orange tree.
# apples: integer array, distances at which each apple falls from the tree.
# oranges: integer array, distances at which each orange falls from the tree.
# 7 11      values of s and t 
# 5 15      values of a and b
# 3 2       values of m(apples) and n(oranges)
# -2 2 1    respective distances which each apple dropped
# 5 -6      respective distances which each orange dropped

def countApplesAndOranges(s,t,a,b,apples,oranges):
    num_apple = 0
    num_orange = 0
    for i in range(len(apples)):
        apples[i]=a+apples[i]
        if apples[i]>=s and apples[i]<=t:
            num_apple+=1
    print(num_apple)
    
    for i in range(len(oranges)):
        oranges[i]=b+oranges[i]
        if oranges[i]>=s and oranges[i]<=t:
            num_orange+=1
    print(num_orange)

s=7
t=11
a=5
b=15
apples = [-2,2,1]
oranges = [5,-6]
countApplesAndOranges(s,t,a,b,apples,oranges)
    
            