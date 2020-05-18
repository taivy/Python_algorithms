def f(s):
    s_len = len(s)
    d = [i+1 for i in range(s_len)]
    for i in range(s_len):
        d[i] = 1
        for j in range(i):
            if s[i] % s[j] == 0 and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    ans = max([0, *d])
    return ans

def main():
    #input()
    #seq = list(map(int, input().split(" ")))
    seq = list(map(int, "3 6 7 12".split(" ")))
    print(f(seq))

if __name__ == "__main__":
    main()
