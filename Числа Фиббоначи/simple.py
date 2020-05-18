'''
Дано целое число n, необходимо вычислить n-е число Фибоначчи 
'''


def fib(n):
    a = 1
    b = 1
    i = 2
    while i < n:
        a, b = b, a + b
        i += 1
    return b

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()