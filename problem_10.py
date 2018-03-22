def isPrimeNumber(num):
   if (num == 2):
      return True
      
   for i in range(3,num + 1, 2):
      if  (num % i == 0) :
         if (num == i):
            return True
         elif( i !=1):
            return False
      else:            
            continue
   return False
        
      
        
s = 0
for i in range(2000001):
   if (isPrimeNumber(i)):
      #print(i)
      s += i

print(s)

