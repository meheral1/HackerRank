def getMoneySpent(keyboards, drives, budget):
    max_spent = -1
    
    for k in keyboards:
        for d in drives:
            total = k + d
            if total <= budget:
                if total > max_spent:
                    max_spent = total
                    
    return max_spent