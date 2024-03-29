"""


"""
from typing import NoReturn


class SelectionSort:
    def __init__(self, _list: list):
        self.list: list = _list
    
    def sort(self) -> NoReturn:
        for first_index in range(len(self.list)):
            min_index: int = first_index
            for second_index in range(first_index + 1, len(self.list)):
                if self.list[second_index] < self.list[min_index]:
                    min_index: int = second_index
            self.list[first_index], self.list[min_index] = self.list[min_index], self.list[first_index]

    @property
    def result(self) -> list:
        self.sort()
        return self.list


if __name__ == '__main__':
    import random

    random.seed(100)
    test_case = [random.randint(0, 100) for _ in list(range(0, 20))]

    selection_sort: SelectionSort = SelectionSort(test_case)
    result: list = selection_sort.result

    print(f"""\n{'TEST-CASE: '.center(14)}{test_case}\n{'  RESULT: '.center(14)}{result}""")

