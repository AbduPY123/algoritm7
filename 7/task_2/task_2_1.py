from random import randint
from timeit import timeit


def gnome_sort(sort_list):
    # https://upload.wikimedia.org/wikipedia/commons/3/37/Sorting_gnomesort_anim.gif
    """
    Сортировка списка методом gnome_sort
    Происходит просмотр массива слева-направо,
    при этом сравниваются (и меняются, если это неотсортированная пара)
    соседние элементы.
    Если происходит обмен элементов, то проиходит возвращение
    на один шаг назад.
    Если обменов не происходит, то алгоритм продолжает просмотр
    массива слева-направо
    в поиске неотсортированных пар.
    """
    i = 1
    while i < len(sort_list):
        if not i or sort_list[i - 1] <= sort_list[i]:
            i += 1
        else:
            sort_list[i], sort_list[i - 1] = sort_list[i - 1], sort_list[i]
            i -= 1
    return sort_list


# ---------------------------------------------------------------------------
m = 10
orig_list = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "gnome_sort(orig_list[:])",
        globals=globals(),
        number=100))

# ---------------------------------------------------------------------------
m = 100
orig_list = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "gnome_sort(orig_list[:])",
        globals=globals(),
        number=100))

# ---------------------------------------------------------------------------
m = 1000
orig_list = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "gnome_sort(orig_list[:])",
        globals=globals(),
        number=100))
# ---------------------------------------------------------------------------

"""
0.005938493999999989
0.5370326489999999
64.261741377
"""
