for _ in range(int(input())):
    n,m,k=map(int,input().split())
    if k%2==0:
        print(k//2)
    else:
        print(-1)