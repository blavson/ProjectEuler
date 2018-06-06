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


def findMaxPrime():
    aandb = tuple()
    max_primes = 40
    for a in range (-1000, 1001):
        for b in range(-1000,1001):
#    a = -79
    #b = 1601
            prime_counter = 0
            for n in range(1, 100):
                pn = n*n + n *a + b
                if pn < 0 :
                    continue
                if isPrimeNumber(pn):
                    prime_counter += 1
                else:
                    break
                if prime_counter > max_primes:
                    max_primes = prime_counter
                    aandb = (a,) + (b,)
    return aandb

t = findMaxPrime()
if t is not None:
    print(t[0] * t[1])
