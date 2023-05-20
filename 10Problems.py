# 1. Search For Number Through Rugged Matrix
ruggedMatrix = [[1, 2, 3, 4], [1, 2, 3, 4], [2, 3], []]
n = 3
i = 0
j = 0
occurrences = 0
for i in range(len(ruggedMatrix)):
    for j in range(len(ruggedMatrix[i])):
        if ruggedMatrix[i][j] == n:
            occurrences += 1

print(occurrences)

# 2. Write a Python program to sort the numbers in a given list by the sum of their digits
digits = [23, 2, 9, 34, 8, 9, 10, 74]
sortedDigits = []

def sumDigits(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum

while len(digits) > 0:
    i = 0
    low = sumDigits(digits[i])
    lowIndex = 0
    while i < len(digits) - 1:
        i += 1
        if sumDigits(digits[i]) < low:
            low = sumDigits(digits[i])
            lowIndex = i
    sortedDigits.append(digits[lowIndex])
    digits.remove(digits[lowIndex])


print(sortedDigits)

# 3. Write a Python program to find all even palindromes up to n.
def numDigits(x):
    num = 0
    while x > 0:
        x = x // 10
        num += 1
    return num

def numreverse(x):
    num = 0
    while x > 0:
        num += (x % 10) * pow(10, numDigits(x) - 1)
        x = x // 10
    return num

n = input("Enter a number: ")
n = int(n)
palindrome = 0

while palindrome < n:
    if numDigits(palindrome) % 2 == 1:
        if palindrome // pow(10, numDigits(palindrome) // 2 + 1) == numreverse(
                palindrome % pow(10, numDigits(palindrome) // 2)):
            print(palindrome)
    else:
        if palindrome // pow(10, numDigits(palindrome) / 2) == numreverse(
                palindrome % pow(10, numDigits(palindrome) / 2)):
            print(palindrome)

    palindrome += 2

