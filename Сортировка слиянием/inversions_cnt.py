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
            #inversions_cnt += len_a_ - i_a
            if len_a_ != 1:
                inversions_cnt += len_a_ - i_a
            i_b += 1
    if len_a == 0:
        for elem in b[i_b:]:
            c.append(elem)
    elif len_b == 0:
        for elem in a[i_a:]:
            c.append(elem)
    return c, inversions_cnt

def merge_sort(arr):
    q = []
    inversions_cnt = 0
    for i in range(len(arr)):
        q.append([arr[i]])
    while len(q) > 1:
        merged, inversions_cnt_ = merge(q[0], q[1])
        print(q[0], q[1])
        inversions_cnt += inversions_cnt_
        del q[0]
        del q[0]
        #print(merged)
        q.append(merged)
    print(q[0])
    return inversions_cnt

def main():
    #input()
    #arr = list(map(int, input().split(" ")))
    arr = list(map(int, "2 3 9 2 9".split(" ")))
    arr = list(map(int, "7 6 5 4 3 2 1".split(" ")))
    print(merge_sort(arr))

if __name__ == "__main__":
    main()