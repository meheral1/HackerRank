def bonAppetit(bill,k,b):
    ate = []
    
    for i in range(len(bill)):
        if bill[i]!=k:
            ate.append(bill[i])
    
    if b==int(sum(ate)/2):
        print("Bon Appetit")
    else:
        print(b-(int(sum(ate)/2)))
          