# Числа из дерева
tree = [1, 3, 2, 4, 6, 15, 37, 8, 5, 16]
def merge_sort(tree):
    if len(tree) <= 1:
        return tree
    mid = len(tree) // 2
    left_half = merge_sort(tree[:mid])
    right_half = merge_sort(tree[mid:])
    return merge(left_half, right_half)

# Функция слияния двух отсортированных массивов
def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    return merged

merge_sorted_tree = merge_sort(tree.copy()) 

print(f"Отсортированные числа: {merge_sorted_tree}")
    