#python2
def main():
    n, w = map(int, raw_input().split())
    a = sorted([map(int, raw_input().split()) + [[_]] for _ in xrange(n)])
    # print a
    total_v = 0
    result = []
    bits_w = map(int, bin(w)[2:])
    bits_w.reverse()
    for c in xrange(len(bits_w)):
        cur = map(tuple, filter(lambda x: x[0] == 2 ** c, a))
        cur.sort()
        cur.reverse()
        # print cur
        if bits_w[c] and cur:
            total_v += cur[0][1]
            result.extend(cur[0][2])
            cur = cur[1:]
        while len(cur) > 1:
            _x = (cur[0][0] + cur[1][0], cur[0][1] + cur[1][1], cur[0][2] + cur[1][2])
            a.append(_x)
            cur = cur[2:]
        if cur:
            _x = (cur[0][0] * 2, cur[0][1], cur[0][2])
            a.append(_x)
      
    print total_v
    # print len(result)
    # print " ".join(map(str, map(lambda x: x + 1, result)))


if __name__ == '__main__':
    main()
    