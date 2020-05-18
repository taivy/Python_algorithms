def merge(a,b):
    print(a,b)
    print()
    len_a = len(a)
    len_b = len(b)
    i_a = 0
    i_b = 0
    c = []
    while len_a > 0 and len_b > 0:
        if a[i_a] < b[i_b]:
            c.append(a[i_a])
            len_a -= 1
            i_a += 1
        else:
            c.append(b[i_b])
            len_b -= 1
            i_b += 1
    if len_a == 0:
        for elem in b[i_b:]:
            c.append(elem)
    elif len_b == 0:
        for elem in a[i_a:]:
            c.append(elem)
    return c

def merge_sort(a):
    from math import floor
    if len(a) < 2:
        return a
    m = floor(len(a)/2)
    l = a[:m]
    r = a[m:]
    return merge(merge_sort(l), merge_sort(r))
    
def main():
    #input()
    #arr = list(map(int, input().split(" ")))
    arr = list(map(int, "2 3 9 2 9".split(" ")))
    print(merge_sort(arr))

if __name__ == "__main__":
    main()