def isPrimeNumber(num):
   for i in range(1,num + 1):
      if  (num % i == 0) :
         if (num == i):
            return True
         elif( i !=1):
            return False
      else:            
            continue
   return False
        
      

def getPrimeFactors(numba):
   dividers_array = []
   divider = 2
  
   while ( isPrimeNumber(numba) == False):
      if (numba % divider ==0):
         numba = (int) (numba / divider)
         dividers_array.append(divider)
      else:
         divider += 1   
   dividers_array.append(numba)
   return dividers_array      

print(set(getPrimeFactors(600851475143)))
