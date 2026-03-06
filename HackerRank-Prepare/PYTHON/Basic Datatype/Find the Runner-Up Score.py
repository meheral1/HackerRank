n = 5
arr = [2,3,6,6,5]

Largest = float('-inf')
second_Largest = float('-inf')

for x in arr:
    if x > Largest:
        second_Largest = Largest
        Largest = x
    elif x > second_Largest and x < Largest:
        second_Largest = x
print(second_Largest)
        