
def manipulator(max_limit = 100):
   summary = 0
   for i in range(max_limit):
      if (i % (3 * 5) ) == 0:
         summary += i
         continue
      if i % 3 == 0:
         summary += i                      
      elif i % 5 == 0:
         summary += i                      
   return summary
   
#print(manipulator(1000))

def fibo(n):
   if ( n  <=1 ):
      return 1
   else:
      return  fibo(n-1) + fibo(n-2)
      

def palindrom():
   mx = 0
   for i in range(1000):
      for j in range(1000):
         p = str(i*j)
         l = len(p)
         pldrom = True
         for k in range(0, l // 2):
            if (p[k] != p[l -1 -k]):
               pldrom = False
         if (pldrom):
            if (i*j > mx):
               mx = i*j
   print(mx)           
                           
               
palindrom()               
