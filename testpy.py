def isrect(f, fi, fj, ti, tj, fill):
    mini = minj = 201
    maxi = maxj = -1
    cnt = 0
    for i in range(fi, ti):
        for j in range(fj, tj):
            if f[i][j] != '.':
                mini = min(mini, i)
                maxi = max(maxi, i)
                minj = min(minj, j)
                maxj = max(maxj, j)
                f[i][j] = fill
                cnt += 1
    return cnt > 0 and (maxi - mini + 1) * (maxj - minj + 1) == cnt

def printans(f):
    print('YES')
    for s in f:
        print(''.join(s))
        
def solve(f, n, m):
    for i in range(n):
        if isrect(f, 0, 0, i, m, 'a') and isrect(f, i, 0, n, m, 'b'):
            printans(f)
            return
    for j in range(m):
        if isrect(f, 0, 0, n, j, 'a') and isrect(f, 0, j, n, m, 'b'):
            printans(f)
            return
    print("NO")
    
n, m = map(int, input().split)
f = []
for i in range(n):
    f.append(list(input()))
solve(f, n, m)