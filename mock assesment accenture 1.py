n=int(input("Enter the limit:"))
lt=[]
n1=3
n2=2
for i in range(0,n):
    i=int(input())
    lt.append(i)
def mine():
    mlt=[]
    for j in lt:
        if (j-n1)<n2:
            mlt.append(j+1)
        else:
            mlt.append(j)
    print(mlt)
mine()

