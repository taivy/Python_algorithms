'''
Задача на программирование: непрерывный рюкзак


Первая строка содержит количество предметов 1≤n≤10^3 и вместимость 
рюкзака 0≤W≤2⋅10^6. Каждая из следующих n строк задаёт стоимость 0≤ci≤2⋅10^6 и 
объём 0<wi≤2⋅10^6 предмета (n, W, ci, wi — целые числа). 

Выведите максимальную стоимость частей предметов 
(от каждого предмета можно отделить любую часть, стоимость и объём при этом 
пропорционально уменьшатся), помещающихся в данный рюкзак, с точностью не менее 
трёх знаков после запятой.
'''

def knapsack(items, volume):
    items.sort(key=lambda item: -item[0]/item[1])
    volume_filled = 0
    cur_cost = 0
    for cost, vol in items:
        if volume_filled + vol > volume:
            coef = (volume-volume_filled)/vol
            volume_filled += vol*coef
        else:
            volume_filled += vol
            coef = 1
        
        cur_cost += cost*coef
        if volume_filled == volume:
            break
    print(cur_cost)

def main():
    nums = list(map(int, input().split(" ")))
    item_cnt, volume = nums
    items = [tuple(map(int, input().split(" "))) for i in range(item_cnt)]
    knapsack(items, volume)

if __name__ == "__main__":
    main()