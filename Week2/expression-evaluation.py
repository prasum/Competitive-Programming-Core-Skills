#python2
def sub(s):
    a = map(int, s.split('-'))
    return a[0] * 2 - sum(a)

def main():
    s = raw_input()
    add = s.split('+')
    print sum(map(sub, add))
    
    
if __name__ == '__main__':
    main()
    