from random import randint
from timeit import timeit


def another_way(lst_obj):
    """
    Возвращает медиану массива путем удаления максимальных элементов
    """
    temp_list = lst_obj
    for i in range(len(lst_obj) // 2):
        temp_list.remove(max(temp_list))
    return max(temp_list)


# ---------------------------------------------------------------------------
m = 10
orig_list = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "another_way(orig_list[:])",
        globals=globals(),
        number=100))

# ---------------------------------------------------------------------------
m = 100
orig_list = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "another_way(orig_list[:])",
        globals=globals(),
        number=100))

# ---------------------------------------------------------------------------
m = 1000
orig_list = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "another_way(orig_list[:])",
        globals=globals(),
        number=100))
# ---------------------------------------------------------------------------

"""
0.0007911750000000051
0.043091434
3.8958528349999995
"""
