from random import randint
from timeit import timeit


def without_sort(lst_obj):
    temp = lst_obj
    left_list = []
    right_list = []
    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i] > temp[j]:
                left_list.append(temp[j])
            if temp[i] < temp[j]:
                right_list.append(temp[j])
            if temp[i] == temp[j] and i > j:
                left_list.append(temp[j])
            if temp[i] == temp[j] and i < j:
                right_list.append(temp[j])
        if len(left_list) == len(right_list):
            return temp[i]
        left_list.clear()
        right_list.clear()


# ---------------------------------------------------------------------------
m = 10
orig_list = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "without_sort(orig_list[:])",
        globals=globals(),
        number=100))

# ---------------------------------------------------------------------------
m = 100
orig_list = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "without_sort(orig_list[:])",
        globals=globals(),
        number=100))

# ---------------------------------------------------------------------------
m = 1000
orig_list = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "without_sort(orig_list[:])",
        globals=globals(),
        number=100))
# ---------------------------------------------------------------------------

"""
0.0028830660000000036
0.535382379
167.943498432
"""
