import itertools

million = 1000000
counter = 0
myset = [0, 1 ,2,3,4,5,6,7,8,9]
permut =  itertools.permutations(myset, 10)
for i in permut:
    counter = counter + 1
    if counter == million:
        print (i)
