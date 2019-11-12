n=4
k=5
for i in range(0,n):
    for j in range(0,i):
        print(" ",end=' ')
    for j in range(0,k):
        print('*',end=' ')
    k=k-2
    print('\n')