# Числа из дерева
num = [2, 10, 15, 1, 3, 5, 9, 10, 4, 6]
def quick_sort(num):
    if len(num) <= 1:
        return num
    opora = num[len(num) // 2]
    less = [x for x in num if x < opora]
    equal = [x for x in num if x == opora]
    greater = [x for x in num if x > opora]
    return quick_sort(less) + equal + quick_sort(greater)
quick_sorted_num = quick_sort(num.copy())
print(f"Результат сортировки: {quick_sorted_num}")