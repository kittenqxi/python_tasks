matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total_sum=0
i=0
while i<len(matrix):
    j=0
    while j<len(matrix[i]):
        total_sum+=matrix[i][j]
        j+=1
    i+=1
print(total_sum)