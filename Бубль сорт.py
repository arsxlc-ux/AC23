# Числа из дерева
numbers = [1,6,8,2,5,3,4,9,7]
def bubble_sort (num):
    n = len(num)
    for i in range (n):
        swapped = False
        for j in range (0, n - i - 1):
            if num[j] > num[j+1]:
                num[j], num[j+1]= num[j+1], num[j]
                swapped = True
        if not swapped:
            break
bubble_sort(numbers)
print("Отсортированные числа:",numbers)
