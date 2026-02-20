def highestCandles(arr):
    count = 0
    for i in range(len(arr)):
        if max(arr)==arr[i]:
            count+=1
    return count


arr = [4,4,1,3]
print(highestCandles(arr))