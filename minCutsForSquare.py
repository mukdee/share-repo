def minimumSquare(m, n):
    vertical_min = 10000000000
    horizontal_min = 10000000000
 
    if m == n:
        return 1

    if m>n:
        return minimumSquare(n, m)


    if dp[m][n] != 0:
        return dp[m][n]
 

    for i in range(1, m//2+1):
 

        horizontal_min = min(minimumSquare(i, n) +
                             minimumSquare(m-i, n), horizontal_min)
    for j in range(1, n//2+1):
 

        vertical_min = min(minimumSquare(m, j) +
                           minimumSquare(m, n-j), vertical_min)
 

    dp[m][n] = min(vertical_min, horizontal_min)
    return dp[m][n]

x=input()
y=x.split()
m=int(y[0])
n=int(y[1])
z=max(m,n)

dp = [[0 for i in range(z+1)] for i in range(z+1)]
print((minimumSquare(m, n))-1)
