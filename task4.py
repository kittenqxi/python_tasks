matrix=[[1, 2], [3, 4], [5, 6]]
n=0
while n<len(matrix):
    n+=1
m=0
if n>0:
    while m<len(matrix[0]):
        m+=1
i=n-1
while i>=0:
    print(matrix[i])
    i-=1 