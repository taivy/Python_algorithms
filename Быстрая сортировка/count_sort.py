
def a(dot, segments_l_sorted, segments_r_sorted):
    s_l = len(segments_l_sorted)
    a = 0
    b = 0
    for i in range(s_l-1, -1, -1):
        s = segments_l_sorted[i]
        if s[0] <= dot:
            a = i+1
            break
    for i in range(s_l-1, -1, -1):
        s = segments_r_sorted[i]
        if s[1] < dot:
            b = i+1
            break
    return a-b
        
def main():
    #segments_cnt, dots_cnt = list(map(int, input().split(" ")))
    #segments = [tuple(map(int, input().split(" "))) for i in range(segments_cnt)]
    #segments = [[2,3], [1,4], [1, 3], [3, 5], [3, 4]]
    segments = [[-2,3],[0,3],[-1,0], [-1,3], [0,1], [-2,-1], [1,3], [2,3], [1,2], [2,3]]
    #dots = list(map(int, input().split(" ")))
    #dots = [1,2,3,4,5,6]
    dots = [-3, -1, 0,2,3]
    segments_l_sorted = sorted(segments, key=lambda s: s[0])
    segments_r_sorted = sorted(segments, key=lambda s: s[1])
    for dot in dots:
        print(a(dot, segments_l_sorted, segments_r_sorted), end=" ")

if __name__ == "__main__":
    main()
