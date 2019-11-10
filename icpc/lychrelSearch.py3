import sys
import math


# def reverse(num):
#     return num[::1]

def toBaseN(num, base):
    baseN = []
    highestPower = 0
    while pow(base, highestPower) < num:
        highestPower += 1
    for i in range (highestPower, -1, -1):
        baseToPower = pow(base, i)
        baseN.append(math.floor(num/baseToPower))
        num = num % baseToPower
    while baseN[0] == 0:
        baseN.pop(0)
    intList = reverseIntList(baseN)
    return intList


def reverseIntList(intList):
    newIntList = []
    for i  in  range(len(intList) - 1, -1, -1):
        newIntList.append(intList[i])
    return newIntList


def toBase10(intList, base):
    sum = 0
    for i in range(0, len(intList)):
        sum += intList[i] * pow(base, i)
    return sum


def palindrome(num):
    rev = reverseIntList(num)
    if num == rev:
        return True
    return False

count = 0
length = 0

for line in sys.stdin:
    count = 0
    length = 0

    fields = line.split()
    base = int(fields[0])
    num = int(fields[1])
    intList = toBaseN(num, base)

    while (not palindrome(intList)) and (count <= 500):
        count += 1
        num = toBase10(intList, base)
        rev = reverseIntList(intList)
        num += toBase10(rev, base)
        intList = toBaseN(num, base)

    if count > 500:
        print(">500")
    else:
        print(count, len(intList))


exit(0)