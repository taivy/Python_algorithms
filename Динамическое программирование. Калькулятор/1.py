def calc(a):
    d = [float('Inf') for i in range(a+1)]
    d[0] = 0
    d_ =[-1 for i in range(a+1)] 
    for i in range(1, a+1):
        steps = d[i-1]+1
        #print(steps)
        print(d, i)
        if i*2-1 < a and d[i-1]+1 < d[i*2-1]:
            d[i*2-1] = steps
            d_[i*2-1] = i
        if i*3-1 < a and d[i-1]+1 < d[i*3-1]:
            d[i*3-1] = steps
            d_[i*3-1] = i
        if i < a and d[i-1]+1 < d[i]:
            d[i] = steps
            d_[i] = i
    steps = 0
    j = a
    seq = []
    print(j)
    print(d_)
    while j > 2:
        j = d_[j-1]
        print(j)
        seq.append(j-1)
        steps += 1
    seq.reverse()
    seq.append(a)
    return seq, d[a]
        
    


def main():
    #a = int(input())
    a = 96234
    seq, n = calc(a)
    print()
    print(n)
    print(*seq)

if __name__ == "__main__":
    main()
