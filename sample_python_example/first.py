a=['$','#']
n=4
for i in range(0,n+1):
    for j in range(0,i):
        if i%2==0:
            print(a[1],end=' ')
        else:
            print(a[0],end=' ')
    print('\n')

