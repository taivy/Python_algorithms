'''
Задача на программирование: покрыть отрезки точками


По данным n отрезкам необходимо найти множество точек минимального размера, 
для которого каждый из отрезков содержит хотя бы одну из точек.

В первой строке дано число 1≤n≤100 отрезков. Каждая из последующих n строк 
содержит по два числа 0≤l≤r≤10^9, задающих начало и конец отрезка. 
Выведите оптимальное число m точек и сами m точек. 
Если таких множеств точек несколько, выведите любое из них.
'''

def func(segments_cnt):
    segments = [tuple(map(int, input().split(" "))) for i in range(segments_cnt)]
    segments.sort(key=lambda item: item[1])
    dots_cnt = 0
    dots = []
    prev_end = -1
    for s_start, s_end in segments:
        if prev_end < s_start:
            prev_end = s_end
            dots.append(s_end)
            dots_cnt += 1
    print(dots_cnt)
    print(*dots)

def main():
    segments_cnt = int(input())
    func(segments_cnt)

if __name__ == "__main__":
    main()