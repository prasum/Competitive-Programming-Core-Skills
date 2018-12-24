import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    p = [0] * (n + 1)
    s = [0] * (n + 1)
    
    for i in range(n):
        p[i + 1] = p[i] + a[i]
    for i in range(n - 1, -1, -1):
        s[i] = s[i + 1] + a[i]
        
    S = p[n]
    for i in range(n): 
        p[i + 1] = min(p[i + 1], p[i])
    for i in range(n - 1, -1, -1):
        s[i] = min(s[i + 1], s[i])
    
    print( ' '.join(map(lambda x: '%d' % (S - sum(x)), zip(p[:-1], s[1:]))) )

    
if __name__ == '__main__':
    solve()
