def extend_array(arr):
    arr_len = len(arr)
    n = 1
    while n < arr_len:
        n *= 2
    return arr + [10000000000000000 for i in range(n-arr_len)]
    
def merge(a,b):
    len_a_ = len(a)
    len_b_ = len(b)
    len_a = len(a)
    len_b = len(b)
    i_a = 0
    i_b = 0
    c = []
    #print(a, b)
    inversions_cnt = 0
    while len_a > 0 and len_b > 0:
        if b[i_b] > a[i_a]:
            c.append(a[i_a])
            #inversions_cnt += len_a_ - i_a
            len_a -= 1
            
            #inversions_cnt += 1
            '''
            if len_a_ == 1 and len_b_ == 1:
                inversions_cnt += 1
                print(a, b)
            '''
            i_a += 1
        else:
            c.append(b[i_b])
            inversions_cnt += len_a_ - i_a
            len_b -= 1
            #inversions_cnt += 1
            #inversions_cnt += len_a_ - i_a
            
            #inversions_cnt += 1
            
            
            '''
            if len_a_ == 1 and len_b_ == 1:
                inversions_cnt += 1
                print(a, b)
            '''

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
        merged, inversions_cnt_ = merge(q.pop(0), q.pop(0))
        inversions_cnt += inversions_cnt_
        q.append(merged)
    print(q[0])
    return inversions_cnt

def main():
    #input()
    #arr = list(map(int, input().split(" ")))
    
    arr = list(map(int, "2 3 9 2 9".split(" ")))
    #arr = extend_array(arr)
    #print(arr)
    #arr = list(map(int, "7 6 5 4 3 2 1".split(" ")))
    print(merge_sort(arr))

if __name__ == "__main__":
    main()