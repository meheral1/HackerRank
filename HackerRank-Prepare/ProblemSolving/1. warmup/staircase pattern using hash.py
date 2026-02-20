def staircase(n):
    for i in range(n):
        print(" "*((n-1)-i), end="")
        print("#"*(i+1))
        
        
n=6 
staircase(n)