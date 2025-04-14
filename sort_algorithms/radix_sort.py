def counting_sort(lst, place):
    size = len(lst)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = lst[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = lst[i] // place
        output[count[index % 10] - 1] = lst[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        lst[i] = output[i]


def radix_sort(lst):
    if len(lst) <= 1:
        return lst

    place = 1
    max_value = max(lst)
    while max_value // place > 0:
        counting_sort(lst, place)
        place *= 10


data = list(map(int, input().split()))
radix_sort(data)
print(data)
