"""
## Bubble Sort

@f4rukseker

linkedin:https://www.linkedin.com/in/faruk-seker/
github:https://github.com/F4ruk-seker

"""
from typing import Any
from sort import Sort


class InsertionSort(Sort):
    def sort(self):
        for key, index in zip(self.list, range(len(self.list))):
            index_pointer: int = index - 1

            while index_pointer >= 0 and self.list[index_pointer] < key:
                self.list[index_pointer + 1] = self.list[index_pointer]
                index_pointer -= 1
            self.list[index_pointer + 1] = key


if __name__ == '__main__':
    import random

    test_case = [random.randint(0, 200) for _ in list(range(0, 20))]

    insertion_sort: InsertionSort = InsertionSort(test_case)
    print(f"| {'TEST-CASE:'.center(10)}|  {test_case}")
    result: list = insertion_sort.get_result()
    print(f"|{'   RESULT: '.center(10)}|  {result}")

