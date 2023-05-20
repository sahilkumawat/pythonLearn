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

