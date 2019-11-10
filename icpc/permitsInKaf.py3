import sys
nums = []
linen = 0
numLines = 0
for line in sys.stdin:
    if linen == 0:
        numLines = int(line)
    else:
        nums.append(int(line))
    linen += 1
    if linen == numLines+1:
        break
# numLines = int(input())
# for i in range(0, numLines):
#     nums.append(int(input()))
numberOfSignatures = 0
sortedNums = sorted(nums)

timesThroughLine = 0

while len(sortedNums) != 0:
    timesThroughLine += 1
    for i in range(0, len(nums)):
        if nums[i] == sortedNums[0]:
            sortedNums.pop(0)
            if len(sortedNums) == 0:
                break

# print()
print(timesThroughLine)

exit(0)
