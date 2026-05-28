matrix=[[5, 1, 9], [2, 11, 3], [7, 4, 6]]
maxx=matrix[0][0]
i=0
while i<len(matrix):
    j=0
    while j<len(matrix[i]):
        if matrix[i][j]>maxx:
            maxx=matrix[i][j]
        j+=1
    i+=1
print(maxx)