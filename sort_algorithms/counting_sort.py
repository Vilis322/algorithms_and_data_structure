import pytest
from random import randint


def counting_sort(data: list) -> list:
    """Represents a counting sort algorithm.

    The algorithm works by counting the number of occurrences of each unique
    element in the input list, then using that count to determine the position
    of each element in the sorted list.

    The process consists of two main steps:
    - Counts the frequency of each element in the input list and store it in
    a list called 'count'. The index of 'count' represents the element
    value, and the value at each index represents the frequency of that element.
    - Construct the sorted list by iterating through the 'count' list. For each
    index, the element is added to the result list as many times as its
    frequency indicates.

    Args:
        data (list): A list of integers to be sorted.

    Returns:
        list: A new list containing the elements of 'data', sorted in ascending order.
    """
    if len(data) <= 1:
        return data

    max_value = max(data)
    count = [0] * (max_value + 1)
    for i in data:
        count[i] += 1

    sorted_data = []
    for i in range(len(count)):
        sorted_data.extend([i] * count[i])
    return sorted_data


def test_counting_sort():
    data = [randint(0, 100) for _ in range(10)]
    sorted_data = counting_sort(data)

    assert all(sorted_data[i] <= sorted_data[i + 1] for i in range(len(sorted_data) - 1))
    assert counting_sort([]) == []
    assert counting_sort([42]) == [42]
    assert counting_sort([5, 5, 5, 5]) == [5, 5, 5, 5]


if __name__ == "__main__":
    pytest.main()
