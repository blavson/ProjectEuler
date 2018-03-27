letters = {
            "1" : "one",
            "2" : "two",
            "3" : "tree",
            "4" : "four",
            "5" : "five",
            "6" : "six",
            "7" : "seven",
            "8" : "eight",
            "9" : "nine",
            "10" : "ten",
            "11" : "evelen",
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
            "40" : "fourty",
            "50" : "fifty",
            "60" : "sixty",
            "70" : "seventy",
            "80" : "eighty",
            "90" : "ninety",
            "100" : "houdred",
            "1000" : "thousand" }   
            
def spellTheNumber (number):
   spell = []
   divider = 1000
   if (number // divider) == 1:
      spell.append(letters["1"])
      spell.append(letters["1000"])
      number %=1000;
   if number // 100 > 0:
         spell.append(letters[str(number // 100)])
         spell.append(letters["100"])
   number %=100                     
   if (number >20 ):
         spell.append(letters[str((number // 10) * 10)])
         spell.append(letters[str(number % 10)])
   else:
         spell.append(letters[str(number)])         
   print(spell)
   
   
spellTheNumber(200)
