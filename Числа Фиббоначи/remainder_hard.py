'''
Задача на программирование повышенной сложности: огромное число Фибоначчи по модулю

Даны целые числа n, m, необходимо найти остаток от деления n-го числа Фибоначчи на m.
'''


def fib(n, m):
    a = 1
    b = 1
    i = 2
    n_limit = 10
    period_cnt = 0
    nums = [0, a, b]
    period_found = False
    while i < n_limit or not period_found:
        a, b = b, (a + b)%m
        i += 1
        if a%m == 0 and b%m == 1:
            period_cnt += 1
            if period_cnt == 1:
                period_start = i-1
            elif period_cnt == 2:
                period_end = i
                period_found = True
        nums.append(b % m)
    nums = nums[period_start:period_end-1]
    return nums[n%len(nums)]

def main():
    nums = input().split(" ")
    n = int(nums[0])
    m = int(nums[1])
    print(fib(n, m))

if __name__ == "__main__":
    main()