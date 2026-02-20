def ratio(arr):
    counter = [0,0,0]
    for i in range(len(arr)):
        if arr[i] > 0:
            counter[0]+=1
        if arr[i] < 0:
            counter[1]+=1
        if arr[i] == 0:
            counter[2]+=1
    for i in range(3):
        if i==0:
            print(f"positive ratio: {(counter[i]/len(arr)):.6f}")
        elif i==1:
            print(f"negative ratio: {(counter[i]/len(arr)):.6f}")
        else:
            print(f"zero ratio: {(counter[i]/len(arr)):.6f}")

    
    
    
    

arr = [-4,5,-9,0,1,2]
ratio(arr)
