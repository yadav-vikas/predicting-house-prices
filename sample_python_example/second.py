n=4
k=2*n-2
for i in range(0,n):
    for j in range(0,k):
        print(" ",end='')
    k=k-2
    for j in range(0,i+1):
        if j%2==0:
            print('$',end=' ')
        else:
            print('#',end=' ')
    print('\n')
