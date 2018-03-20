def isPrimeNumber(num):
    for i in range(1,num + 1): 
        if (num % i == 0) : 
            if (num == i): 
                return True 
            elif( i !=1): 
                return False 
        else: continue 
    return False 


def mainLoop(upper_limit):
    counter = 0
    up_to_infinity = 2

    while (counter < upper_limit):
        if (isPrimeNumber(up_to_infinity)):
            counter +=1
            #print(up_to_infinity)
        up_to_infinity +=1

    print(up_to_infinity -1)
    
    
mainLoop(10001)
    
