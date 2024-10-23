m = 3
n = 2

for i in range(m):
    for j in range(n):
        print("general: ", i, j)
        if i < m - 1:
            print("i<m: ", i*n+j, (i + 1) * n + j)
        if j < n - 1:
            print("j<n: ", i*n+j, i * n + j + 1)
        