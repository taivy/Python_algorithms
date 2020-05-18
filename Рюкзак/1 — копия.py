def knapsackTD(W, n, weights):
    D = [[0 for _ in range(n)] for _ in range(W+2)]
    for i in range(n):
        for w in range(W+1):
            D[w][i] = D[w][i-1]
            if weights[i] <= w:
                D[w][i] = max([D[w][i], D[w-weights[i]][i-1]+weights[i]])
    print(D)
    return D[W][n-1]


def main():
    #w, n = list(map(int, input().split(" ")))
    #weights = list(map(int, input().split(" ")))
    w = 10
    n = 3
    weights = [1,4,8]
    print(knapsackTD(w, n, weights))

if __name__ == "__main__":
    main()
