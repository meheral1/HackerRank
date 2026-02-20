def migratoryBirds(arr):
    count_map = [0] * 6
    for bird_id in arr:
        count_map[bird_id] += 1
    max_frequency = 0
    result_id = 0
    for i in range(1, 6):
        if count_map[i] > max_frequency:
            max_frequency = count_map[i]
            result_id = i
    return result_id

arr = [1, 4, 4, 4, 3, 5]
print(migratoryBirds(arr))