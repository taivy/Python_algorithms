def diff(a, b):
    if a == b:
        return 0
    else:
        return 1

def editing_distance(str1, str2):
    n = len(str1)
    m = len(str2)
    d = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        d[i][0] = i
    for j in range(m+1):
        d[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            c = diff(str1[i-1], str2[j-1])
            d[i][j] = min([d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+c])
    return d[n][m]

def main():
    #str1 = input()
    #str2 = input()
    str1 = "short"
    str2 = "ports"
    print(editing_distance(str1, str2))

if __name__ == "__main__":
    main()
