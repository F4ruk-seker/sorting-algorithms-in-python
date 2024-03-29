"""
## Bubble Sort

@f4rukseker

linkedin:https://www.linkedin.com/in/faruk-seker/
github:https://github.com/F4ruk-seker

"""
from typing import NoReturn

from sort import Sort


class SelectionSort(Sort):
    def sort(self) -> NoReturn:
        for first_index in range(len(self.list)):
            min_index: int = first_index
            for second_index in range(first_index + 1, len(self.list)):
                if self.list[second_index] < self.list[min_index]:
                    min_index: int = second_index
            self.list[first_index], self.list[min_index] = self.list[min_index], self.list[first_index]


def main() -> None:
    import random

    test_case = [random.randint(0, 200) for _ in list(range(0, 20))]

    selection_sort: SelectionSort = SelectionSort(test_case)
    result: list = selection_sort.get_result()

    print(f"""| {'TEST-CASE:'.center(10)}|  {test_case}\n|{'   RESULT: '.center(10)}|  {result}""")

    del result
    del selection_sort


if __name__ == '__main__':
    print(f'|{"-" * 110}|')
    for test_count in range(5):
        main()
        print(f'|{"-"*110}|')


