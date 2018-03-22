import math
counter = 1
s = []

while (counter <1001):
    s.append(counter * counter)
    counter += 1

for i in range(0, 996):
    for j in range (i + 1, 997):
        for k in range(j + 1, 998):
            if ( s[i] + s[j] == s[k] ):
                if (math.sqrt(s[i]) + math.sqrt(s[j]) + math.sqrt(s[k]) == 1000):
                    print(math.sqrt(s[i]) , math.sqrt(s[j]) , math.sqrt(s[k]))
                    print(math.sqrt(s[i]) * math.sqrt(s[j]) * math.sqrt(s[k]))



