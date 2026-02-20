a = [5,6,7]
b = [3,6,10]
score = []
for i in range(3):
    if a[i]>b[i] or a[i]<b[i]:
        score.append(1)
    else:
        continue
print(f"{score}")