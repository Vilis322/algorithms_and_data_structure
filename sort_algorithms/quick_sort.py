def quick_sort(data: list, low: int = 0, high: int = None) -> list:
    """Represents a quick sort algorithm.

    The function sorts data by using a median of three elements: the first, middle, and last element.
    It then creates two indices, `left` and `right`. The `left` index represents the position of
    an element greater than the pivot, and the `right` index represents an element
    less than the pivot. The function then enters a loop:
    - The `left` index increments until an element greater than the pivot is found.
    - The `right` index decrements until an element less than the pivot is found.
    If `left` is less than or equal to `right`, the elements at `left` and `right` are swapped.
    After partitioning, the function recursively sorts the left and right halves of the array.
    The time complexity is O(n log n) on averagely, and O(n²) in the worst case.

    Args:
        data (list): The data to be sorted.
        low (int) = The index of the first element in the data.
        high (int) = The index of the last element in the data. In first calling it is 'None'.

    Returns:
        list: The sorted list.

        Example:
        Initial array: [5, 2, 9, 1, 5]

        1. First, we pick the pivot using the median of three: [5, 9, 5] → Pivot = 5
        2. Partitioning step: [2, 1, 5, 9, 5] (After first swap)
        3. Left subarray: [2, 1, 5], Right subarray: [9, 5]

        Left recursion:
        4. Pivot for left subarray: [2, 1, 5] → Pivot = 2
        5. Partitioning left: [1, 2, 5]

        Right recursion:
        6. Pivot for right subarray: [9, 5] → Pivot = 5
        7. Partitioning right: [5, 9]

        Final sorted array: [1, 2, 5, 5, 9]
    """
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
