def graderounder(grades):
    n = len(grades) 
    for i in range(n):
        multiple = ((grades[i]//5)+1)*5
        if (multiple - grades[i])<3 and grades[i] >= 38:
            grades[i] = multiple
        else:
            continue
    return grades

grades = [22,86,30,0,16,51,53,42,48,22,69,12,27,34,24,95,16,32,22,52]
print(graderounder(grades))


