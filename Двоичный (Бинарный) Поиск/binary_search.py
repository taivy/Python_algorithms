
def binary_search(arr, num):
    l = 0
    r = len(arr)-1
    while l <= r:
        m = (l+r)//2
        if arr[m] == num:
            return m
        elif arr[m] > num:
            r = m - 1
        else:
            l = m + 1
    return -1

def main():
    arr = list(map(int, input().split(" ")))[1:]
    arr_to_find = list(map(int, input().split(" ")))[1:]
    #arr = list(map(int, "5 1 5 8 12 13".split(" ")))[1:]
    #arr_to_find = list(map(int, "5 8 1 23 1 11".split(" ")))[1:]
    for num in arr_to_find:
        res = binary_search(arr, num)
        if res > -1:
            res += 1
        print(res, end=" ")

if __name__ == "__main__":
    main()