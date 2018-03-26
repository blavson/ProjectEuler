def getPower(n):
    res = 1
    res <<= n 
    return res

def getSum(l):
    s = 0
    l1 = str(l)
    for i in l1:
        s += ord(i) -ord('0')
    return s    
    
ls = getPower(1000)    
print(getSum(ls))    
