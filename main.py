from sort import BubbleSort, SelectionSort, InsertionSort
from sort.base_sort import Sort


sorting_algorithms: list[Sort] = BubbleSort, SelectionSort, InsertionSort

for sorting_algorithm in sorting_algorithms:
    print(f'Algorithm run ({sorting_algorithm.__name__})')
    sorting_algorithm.test(test_range=10_000)
    print('.'*133)
