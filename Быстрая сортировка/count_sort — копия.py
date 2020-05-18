from bisect import bisect_left, bisect_right

def a(dot, segments_l_sorted, segments_r_sorted):
    a = bisect_right(segments_l_sorted, dot)+1
    b = bisect_left(segments_r_sorted, dot)+1
    return a-b
        
def main():
    #segments_cnt, dots_cnt = list(map(int, input().split(" ")))
    #segments = [tuple(map(int, input().split(" "))) for i in range(segments_cnt)]
    #segments = [[2,3], [0,5], [7,10]]
    #segments = [[2,3], [1,4], [1, 3], [3, 5], [3, 4]]
    segments = [[-2,3],[0,3],[-1,0], [-1,3], [0,1], [-2,-1], [1,3], [2,3], [1,2], [2,3]]
    #dots = list(map(int, input().split(" ")))
    #dots = [1,0,0]
    #dots = [1,2,3,4,5,6]
    dots = [-3, -1, 0,2,3]
    segments_l_sorted = sorted([s[0] for s in segments])
    segments_r_sorted = sorted([s[1] for s in segments])
    for dot in dots:
        print(a(dot, segments_l_sorted, segments_r_sorted), end=" ")

if __name__ == "__main__":
    main()









