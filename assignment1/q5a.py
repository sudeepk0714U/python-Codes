def F(M,N):
    if M == 0:
        return 1
    if(N>= 1 and N <= M):
        return 1
    else:
        return F(M-1, N) + F(M-1, N-1)

m = int(input("enter m :"))
n = int(input("enter n : "))
a = F(m,n)
print(a)