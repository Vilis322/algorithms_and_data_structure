def insertion_sort(lst, interval):
    for i in range(interval, len(lst)):
        key = lst[i]
        j = i - interval
        while j >= 0 and key < lst[j]:
            lst[j + interval] = lst[j]
            j = j - interval
        lst[j + interval] = key


def shell_sort(lst):
    n = len(lst)
    interval = n // 2
    while interval > 0:
        insertion_sort(lst, interval)
        interval //= 2


data = list(map(int, input().split()))
shell_sort(data)
print(data)
