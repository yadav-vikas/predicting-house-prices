row=5
i=1
k=1
while i<=row:
    for j in range(1,row+1):
        if j%2==0:
            
            print(k,end='')
            k=k+1
        else:
            print('*',end='')

    row=row-1
    print('\n')