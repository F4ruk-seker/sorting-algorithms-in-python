"""
## Bubble Sort

@f4rukseker

linkedin:https://www.linkedin.com/in/faruk-seker/
github:https://github.com/F4ruk-seker

"""
from typing import Any, Union


class BubbleSort:
    def __init__(self, _list: list):
        self.list: list = _list
    
    def get_result(self) -> list:
        self.sort()
        return self.list
    
    def sort(self) -> None:
        for first_index in range(len(self.list) - 1, 0, -1):
            for second_index in range(first_index):
                if self.list[second_index] > self.list[second_index + 1]:
                    _ = self.list[second_index]
                    self.list[second_index] = self.list[second_index + 1]
                    self.list[second_index + 1] = _


class BubbleSortTyper(BubbleSort):
    @staticmethod
    def str_to_number(obj: str):
        if obj.replace(',', '').replace('.', '').isnumeric():
            obj = obj.replace(',', '.')
            return int(obj) if float(obj).is_integer() else float(obj)
        return len(obj)

    def to_type(self, obj: Any) -> Union[int, float]:
        obj: Any = self.str_to_number(obj) if type(obj) is str else obj
        obj: Any = int(obj) if type(obj) is bool else obj
        return obj

    def sort(self) -> None:
        for first_index in range(len(self.list) - 1, 0, -1):
            for second_index in range(first_index):
                first_case: Any = self.to_type(self.list[second_index])
                second_case: Any = self.to_type(self.list[second_index + 1])

                if first_case > second_case:
                    _ = self.list[second_index]
                    self.list[second_index] = self.list[second_index + 1]
                    self.list[second_index + 1] = _


if __name__ == '__main__':
    import random
    random.seed(100)
    test_case = [random.randint(0, 100) for _ in list(range(0, 30))]
    bubble_sort: BubbleSort = BubbleSort(test_case)

    result: list[int] = bubble_sort.get_result()
    print(result)

    test_case += [True, False, True, '15a1', 'pars', 'parsS', '1453', '1453.50', '1453,55', 'f4ruk.seker']
    bubble_sort_other_objects: BubbleSort = BubbleSortTyper(test_case)

    result: list[Any] = bubble_sort_other_objects.get_result()

    print(result)

