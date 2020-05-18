'''
Задача на программирование: различные слагаемые


По данному числу 1≤n≤10^9 найдите максимальное число k, для которого n 
можно представить как сумму k различных натуральных слагаемых. 
Выведите в первой строке число k, во второй — k слагаемых.
'''

def func(a):
    s = 0
    num = 0
    nums = []
    i = 1
    while True:
        if a-(s+i) > i or s+i == a:
            nums.append(i)
            num += 1
            s += i
            if s == a:
                break
        i += 1
    print(num)
    print(" ".join(list(map(str, nums))))
    
def main():
    a = int(input())
    func(a)

if __name__ == "__main__":
    main()