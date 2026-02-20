def sockMerchant(n, ar):
    hash = {}
    pairs = 0
    for i in ar:
        if i in hash:
            hash[i]+=1
        else:
            hash[i]=1
    for item in hash:
        pairsair+=(hash[item]//2)
    return pairs
            
        