def merge(a,b):
    len_a_ = len(a)
    len_a = len(a)
    len_b = len(b)
    i_a = 0
    i_b = 0
    c = []
    inversions_cnt = 0
    while len_a > 0 and len_b > 0:
        if b[i_b] >= a[i_a]:
            c.append(a[i_a])
            len_a -= 1
            i_a += 1
        else:
            c.append(b[i_b])
            len_b -= 1
            inversions_cnt += len_a_ - i_a
            i_b += 1
    if len_a == 0:
        for elem in b[i_b:]:
            c.append(elem)
    elif len_b == 0:
        for elem in a[i_a:]:
            c.append(elem)
    return c, inversions_cnt

def merge_sort(a, inv):
    from math import floor
    if len(a) < 2:
        return a, 0
    m = floor(len(a)/2)
    l = a[:m]
    r = a[m:]
    l_, inv_l = merge_sort(l, 0)
    r_, inv_r = merge_sort(r, 0)
    inv += inv_l + inv_r
    res, invs = merge(l_, r_)
    return res, inv+invs
    
def main():
    #input()
    #arr = list(map(int, input().split(" ")))
    arr = list(map(int, "2 3 9 2 9".split(" ")))
    #arr = list(map(int, "7 6 5 4 3 2 1".split(" ")))
    #arr = list(map(int, "6 5 8 6 0 4".split(" ")))
    print(merge_sort(arr, 0))

if __name__ == "__main__":
    main()