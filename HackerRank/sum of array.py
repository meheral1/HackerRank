def sum_of_array(ar):
    result = 0
    for num in range(len(ar)):
        result += ar[num]
    return result

ar = [1,2,3,4,5]
print(f"result: {sum_of_array(ar)}")