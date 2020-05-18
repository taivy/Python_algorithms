'''
Дано число n, необходимо найти последнюю цифру n-го числа Фибоначчи.
'''

def fib(n):
    a = 1
    b = 1
    i = 2
    while i < n:
        a, b = b, (a + b) % 10
        i += 1
    return b

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()