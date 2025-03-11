def quick_sort(data: list, low: int = 0, high: int = None) -> list:
    """Быстрая сортировка in-place."""
    if high is None:
        high = len(data) - 1

    if low >= high:
        return data

    mid = (low + high) // 2
    pivot = sorted([data[low], data[mid], data[high]])[1]

    left, right = low, high

    while left <= right:
        while data[left] < pivot:
            left += 1
        while data[right] > pivot:
            right -= 1
        if left <= right:
            data[left], data[right] = data[right], data[left]
            left += 1
            right -= 1

    quick_sort(data, low, right)
    quick_sort(data, left, high)

    return data


if __name__ == "__main__":
    list1 = [int(x) for x in input("Unsorted List: ").split()]

    sorted_list = quick_sort(list1)
    print(f"Sorted List: {sorted_list}")
