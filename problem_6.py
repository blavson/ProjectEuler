s = 0
for i in range(1, 101):
   s += i * i;
print(s)
   
s1 = 0   
for j in range(1, 101):
   s1 += j

s1 *= s1
print(s1)      

answer = s1 -s
print(answer)
