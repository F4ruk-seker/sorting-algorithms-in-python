"""
## Bubble Sort

@f4rukseker

linkedin:https://www.linkedin.com/in/faruk-seker/
github:https://github.com/F4ruk-seker

"""
from typing import NoReturn
from sort import Sort
from performance import get_performance_metric


class BubbleSort(Sort):
    def sort(self) -> None:
        for first_index in range(len(self.list) - 1, 0, -1):
            for second_index in range(first_index):
                if self.to_type(self.list[second_index]) > self.to_type(self.list[second_index + 1]):
                    self.list[second_index], self.list[second_index + 1] = self.list[second_index + 1], self.list[second_index]

    @staticmethod
    @get_performance_metric
    def test(test_range: int = 30) -> NoReturn:
        import random
        test_case = [random.randint(0, 100) for _ in list(range(0, test_range))]

        bubble_sort: BubbleSort = BubbleSort(test_case.copy())

        result: list[int] = bubble_sort.get_result()
        # print(f"""| {'TEST-CASE:'.center(10)}|  {test_case}\n|{'   RESULT: '.center(10)}|  {result}""")

        # test_case += [True, False, True, '15a1', 'pars', 'parsS', '1453', '1453.50', '1453,55', 'f4ruk.seker']
        # bubble_sort_other_objects: BubbleSort = BubbleSort(test_case.copy()[:10])
        #
        # result: list[Any] = bubble_sort_other_objects.get_result()
        # print(f"""| {'TEST-CASE:'.center(10)}|  {test_case}\n|{'   RESULT: '.center(10)}|  {result}""")


