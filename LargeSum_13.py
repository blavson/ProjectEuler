def readLineByLine():
   with open('task_13.txt') as f:
      slist = f.readlines()
   return slist
   
def addStrings(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)
    
    if (s1_len < s2_len):
       zeroes='' 
       dif = s2_len - s1_len
       for i in range(dif):
          zeroes ='0' + zeores
       s1 = zeroes + s1
    elif (s2_len < s1_len):
       zeroes='' 
       dif = s1_len - s2_len
       for i in range(dif):
          zeroes ='0' + zeroes
       s2 = zeroes + s2
   
    s3 = []
    reminder = 0
    
    for i in range(s1_len -1, -1, -1):
      n1 = ord(s1[i]) - ord('0')
      n2 = ord(s2[i]) - ord('0')
      n3 = (n1 + n2 + reminder)% 10
      reminder = (n1 + n2 + reminder) // 10
      s3.append(str(n3))
    if (reminder > 0):
       s3.append(str(reminder))  
    res = ''.join(s3[::-1])
    return  res

s = readLineByLine()
summary1 = s[0].strip()
for i in range(1, 100):
   summary = addStrings(summary1, s[i].strip())
   summary1 = summary

print(summary[:10])   


