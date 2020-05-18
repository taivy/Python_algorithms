M=10000

def count_sort(a):
    a_ = [0 for i in range(len(a))]
    b = [0 for i in range(M)]
    for j in range(len(a)):
        b[a[j]] += 1
    for i in range(1, M):
        b[i] += b[i-1]
    for j in range(len(a)-1, -1, -1):
        a_[b[a[j]]-1] = a[j]
        b[a[j]] -= 1
    return a_
        
def main():
    #input()
    #arr = list(map(int, input().split(" ")))
    arr = list(map(int, "2 3 9 2 9".split(" ")))
    print(*count_sort(arr))

if __name__ == "__main__":
    main()