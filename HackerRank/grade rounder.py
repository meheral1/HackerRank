def graderounder(grades):
    n = len(grades) 
    for i in range(n):
        multiple = ((grades[i]//5)+1)*5
        if (multiple - grades[i])<3 and grades[i] > 38:
            grades[i] = multiple
        else:
            continue
    return grades

grades = [73,67,38,40]
print(graderounder(grades))


