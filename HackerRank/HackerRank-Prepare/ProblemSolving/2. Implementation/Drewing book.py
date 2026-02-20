def pageCount(n,p):
    if p==n:
        return 0
    return min(p//2, (n//2)-(p//2))
    