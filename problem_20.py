
def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num -1)


def countSum(bignum):
    s = str(bignum)
    sum = 0
    for n in s:
        sum += ord(n)- ord('0')
    return sum


a = fact(100)

print(countSum(a))
