#python2
import math

def abs(x):
    return x if x > 0 else -x

def main():
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split())
    m = max(a)
    
    b = [[0] * (m + 1) for _ in xrange(n + 1)]
    for i in xrange(1, n + 1):
        mn = b[i - 1][0]
        for j in xrange(m + 1):
            mn = min(mn, b[i - 1][j])
            b[i][j] = mn + abs(a[i - 1] - j)
            
    print min(b[n])
    

if __name__ == '__main__':
    main()
    