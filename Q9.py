#F(M,N) = 1 if M = 0 or M ≥ N ≥ 1 , and, F(M, N) = F(M-1, N) + F(M-1, N-1), 
def is_perfect_number(n):
    if n <= 0:
        return False
    
    # Calculate the sum of proper divisors
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
            
    return sum == n   

a = int(input("enter a number : "))
print(is_perfect_number(a))

i=0
while(i<10):
    print("Jai Balayya")
    i+=1
