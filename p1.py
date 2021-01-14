row=int(input("Enter number of rows:"))
col=int(input("Enter number of columns:"))
print("etnter matrix1 values:")
matrix1=[[int(input("enter value:"))for j in range(col)]for i in range(row) ]
print("enter matrix values2")
matrix2=[[int(input("enter value:"))for j in range(col)]for i in range(row) ]
result=[[0 for j in range(col)]for i in range(row) ]
for i in range(row):
    for j in range(col):
        result[i][j]=matrix1[i][j]+matrix2[i][j]


for i in range(row):
    for j in range(col):
        print(format(result[i][j],"<3"),end=" ")
    print()