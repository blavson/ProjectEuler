letters = {
            "1" : "one",
            "2" : "two",
            "3" : "three",
            "4" : "four",
            "5" : "five",
            "6" : "six",
            "7" : "seven",
            "8" : "eight",
            "9" : "nine",
            "10" : "ten",
            "11" : "eleven",
            "12" : "twelve",
            "13" : "thirteen",
            "14" : "fourteen",
            "15" : "fifteen",
            "16" : "sixteen",
            "17" : "seventeen",
            "18" : "eighteen",
            "19" : "nineteen",
            "20" : "twenty",
            "30" : "thirty",
            "40" : "forty",
            "50" : "fifty",
            "60" : "sixty",
            "70" : "seventy",
            "80" : "eighty",
            "90" : "ninety",
            "100" : "hundred",
            "1000" : "thousand" }   
            
def classify(n):
    spell = []
    divider = 1000
    while(divider >= 1):
        n1 = n // divider
        n2 = n % divider
        spell.append(n1)
        n = n2
        divider = divider // 10
    print(spell)        
    return spell

def spellIt(l):
    sp = []
    ln = len(l)

    if (l[0] != 0):
        sp.append(letters[str(l[0])])
        sp.append(letters["1000"])
    
    if ( l[1] != 0):
        sp.append(letters[str(l[1])])
        sp.append(letters["100"])
        sp.append("and")

    less20 = False    
    if ( l[2] != 0):
        if (l[2] >= 2):
            sp.append(letters[str(l[2] * 10)])
        else:
            less20 = True
            
    if (l[3] != 0):
        if less20:
            dex = 10 + l[3];
            print(dex)
            sp.append(letters[str(10 + l[3])])
        else:            
            sp.append(letters[str(l[3])])

    print(sp)
    sz = 0
    for i in sp:
        sz += len(i)
    print(sz)    
    return sz

s = 0    
#for index in range(1, 101):
lst = classify(110)
s += spellIt(lst)

print(s)    
