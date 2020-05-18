def knapsackTD(w, n, weights, H):
    if H[w] == -1:
        v = 0
        for i in range(n):
            if weights[i] <= w:
                v = max([0, knapsackTD(w-weights[i], i+1, weights, H) + weights[i]])
        H[w] = v
    return H[w]


def main():
    #w, n = list(map(int, input().split(" ")))
    #weights = list(map(int, input().split(" ")))
    w = 10
    n = 3
    H = [-1 for i in range(w+1)]
    weights = [1,4,8]
    print(knapsackTD(w, n, weights, H))

if __name__ == "__main__":
    main()
