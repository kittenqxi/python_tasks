matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n=0 
while n<len(matrix):
    n+=1
m=0
if n>0:
    while m<len(matrix[0]):
        m+=1
s=0
i=0
while i<n:
    j=0
    while j<m:
        if i==j:
            s+=matrix[i][j]
        j+=1
    i+=1
print(s)