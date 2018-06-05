
def getLineFromFile(filename):
    f = open(filename,"r")
    nameline =f.readline()
    splitline = nameline.split(",")
    sorted_names = sorted(splitline)
    f.close()
    return sorted_names

def calculateScore(the_string, _index):
    name = the_string[_index -1]
    sum = 0
    for each_letter in name:
        if each_letter == '"':
            continue
        sum += ord(each_letter) - ord('A') + 1
    return sum * _index

names = getLineFromFile('problem_22.txt')
big_sum = 0
for main_index in range(1, len(names) +1):
    big_sum += calculateScore(names, main_index)

print(big_sum)
