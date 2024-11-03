"""
## Bubble Sort

@f4rukseker

linkedin:https://www.linkedin.com/in/faruk-seker/
github:https://github.com/F4ruk-seker

"""
from typing import NoReturn
from sort import Sort
from performance import get_performance_metric


class InsertionSort(Sort):
    def sort(self):
        for key, index in zip(self.list, range(len(self.list))):
            index_pointer: int = index - 1

            while index_pointer >= 0 and self.list[index_pointer] < key:
                self.list[index_pointer + 1] = self.list[index_pointer]
                index_pointer -= 1
            self.list[index_pointer + 1] = key

    @staticmethod
    @get_performance_metric
    def test(test_range: int = 30) -> NoReturn:
        import random

        test_case = [random.randint(0, 200) for _ in list(range(0, test_range))]

        insertion_sort: InsertionSort = InsertionSort(test_case)
        # print(f"| {'TEST-CASE:'.center(10)}|  {test_case}")
        result: list = insertion_sort.get_result()
        # print(f"|{'   RESULT: '.center(10)}|  {result}")


        del result
        del insertion_sort

