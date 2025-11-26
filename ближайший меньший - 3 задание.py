# ближайший меньший(код работает если в компиляторе есть отдельное окно для ввода)
from typing import List
def naersmall(nums: List[int]) -> List[int]:
    ind = []  
    result = [-1] * len(nums)  
    for i in range(len(nums) - 1, -1, -1):
        while ind and nums[ind[-1]] >= nums[i]:
            ind.pop()
        if ind:
            result[i] = nums[ind[-1]]
        ind.append(i)
    return result
nums = list(map(int, input().strip().split()))  
result = naersmall(nums)
print(' '.join(map(str, result)))