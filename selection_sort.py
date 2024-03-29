"""


"""
from typing import NoReturn


class SelectionSort:
    def __init__(self, _list: list):
        self.__list: list = _list
    
    def sort(self) -> NoReturn:
        for first_index in range(len(self.__list)):
            min_index: int = first_index
            for second_index in range(first_index + 1, len(self.__list)):
                if self.__list[second_index] < self.__list[min_index]:
                    min_index: int = second_index
            self.__list[first_index], self.__list[min_index] = self.__list[min_index], self.__list[first_index]

    @property
    def result(self) -> list:
        self.sort()
        return self.__list


def main() -> None:
    import random

    test_case = [random.randint(0, 200) for _ in list(range(0, 20))]

    selection_sort: SelectionSort = SelectionSort(test_case)
    result: list = selection_sort.result

    print(f"""| {'TEST-CASE:'.center(10)}|  {test_case}\n|{'   RESULT: '.center(10)}|  {result}""")

    del result
    del selection_sort


if __name__ == '__main__':
    print(f'|{"-" * 110}|')
    for test_count in range(5):
        main()
        print(f'|{"-"*110}|')


