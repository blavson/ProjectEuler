starting_number = 0
max_chain = 0

def chain(number):
   global starting_number 
   global max_chain

   s_number  = number
   train = 1
   while( number != 1):
      if (number % 2 == 0):
         number //= 2
      else:
         number = 3 * number + 1
      train +=1
   if (train > max_chain):
      max_chain = train
      starting_number = s_number      


for i in range(1000000, 1, -1):
   chains = chain(i)

      
print(starting_number, max_chain)



