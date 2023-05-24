def findwinner(m,n):
    if(m%2==0 or n%2==0):
        print("Player 1")
    else:
        print("Player 2")

m,n=map(int,input().split())
findwinner(m,n)
