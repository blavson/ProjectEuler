
s1 = '37107287533902102798797998220837590246510135740250'
s2 = '46376937677490009712648124896970078050417018260538'

def addStrings(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)
    s3 = []
    reminder = 0
    
    for i in  range(s1_len -1, -1, -1):
        n1 = ord(s1[i]) - ord('0')
        n2 = ord(s2[i]) - ord('0')
        n3 = (n1 + n2 + reminder)% 10
        if (n1 + n2 >= 10):
            reminder = 1
        else:
            reminder = 0
        s3.append(str(n3))
        
    return ''.join(s3[::-1])
            
print(addStrings(s1,s2))
