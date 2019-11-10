# import sys
#
# for line in sys.stdin:

line = input()
line = line.upper()
lettersCount = []
for i in range(0, 26):
    lettersCount.append(0)

for char in line:

    if(char == "A"):
        lettersCount[0] += 1
    elif (char == "B"):
        lettersCount[1] += 1
    elif (char == "C"):
        lettersCount[2] += 1
    elif (char == "D"):
        lettersCount[3] += 1
    elif (char == "E"):
        lettersCount[4] += 1
    elif (char == "F"):
        lettersCount[5] += 1
    elif (char == "G"):
        lettersCount[6] += 1
    elif (char == "H"):
        lettersCount[7] += 1
    elif (char == "I"):
        lettersCount[8] += 1
    elif (char == "J"):
        lettersCount[9] += 1
    elif (char == "K"):
        lettersCount[10] += 1
    elif (char == "L"):
        lettersCount[11] += 1
    elif (char == "M"):
        lettersCount[12] += 1
    elif (char == "N"):
        lettersCount[13] += 1
    elif (char == "O"):
        lettersCount[14] += 1
    elif (char == "P"):
        lettersCount[15] += 1
    elif (char == "Q"):
        lettersCount[16] += 1
    elif (char == "R"):
        lettersCount[17] += 1
    elif (char == "S"):
        lettersCount[18] += 1
    elif (char == "T"):
        lettersCount[19] += 1
    elif (char == "U"):
        lettersCount[20] += 1
    elif (char == "V"):
        lettersCount[21] += 1
    elif (char == "W"):
        lettersCount[22] += 1
    elif (char == "X"):
        lettersCount[23] += 1
    elif (char == "Y"):
        lettersCount[24] += 1
    elif (char == "Z"):
        lettersCount[25] += 1

lettersCount = sorted(lettersCount)

sumLengths = -3

for i in range(0, 7):
    sumLengths += (14 * lettersCount[i])

for i in range(7, 15):
    sumLengths += (12 * lettersCount[i])

for i in range(15, 20):
    sumLengths += (10 * lettersCount[i])

for i in range(20, 23):
    sumLengths += (8 * lettersCount[i])

for i in range(23, 25):
    sumLengths += (6 * lettersCount[i])

sumLengths += 4 * lettersCount[25]

print(sumLengths)

exit(0)