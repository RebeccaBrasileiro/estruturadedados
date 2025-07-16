def two_sum_forca_bruta(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def quicksort(arr):
    _quicksort(arr, 0, len(arr) - 1)

def _quicksort(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        _quicksort(arr, left, pi - 1)
        _quicksort(arr, pi + 1, right)

def partition(arr, left, right):
    pivot = arr[right][0]
    i = left - 1
    for j in range(left, right):
        if arr[j][0] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def two_sum_sorted(nums, target):
    arr = [(num, idx) for idx, num in enumerate(nums)]
    quicksort(arr)
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left][0] + arr[right][0]
        if current_sum == target:
            return [arr[left][1], arr[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

def two_sum_hash(nums, target):
    indice_por_valor = {}
    for i, valor_atual in enumerate(nums):
        complemento = target - valor_atual
        if complemento in indice_por_valor:
            return [indice_por_valor[complemento], i]
        indice_por_valor[valor_atual] = i
    return []

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum_forca_bruta(nums, target))
    print(two_sum_sorted(nums, target))
    print(two_sum_hash(nums, target))
