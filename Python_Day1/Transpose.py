li=[[1,2,3], [4,5,6], [7,8,9]]
rows=len(li)
col=len(li[0])
transpose =[]
for i in range(col):
    row=[]
    for j in range(rows):
        row.append(li[j][i])
    transpose.append(row)
for row in transpose:
    print(row)
