def breakingRecords(scores):
    counter = [0,0]
    min_score = scores[0]
    max_score = scores[0]
    for i in range(1, len(scores)):
        if max_score<scores[i]:    
            counter[0]+=1
            max_score = scores[i]
        if min_score>scores[i]:
            counter[1]+=1
            min_score = scores[i]
    return counter
        
scores = [12,24,10,24]
print(breakingRecords(scores))
