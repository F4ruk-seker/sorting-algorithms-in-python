"""
## Bubble Sort

@f4rukseker

linkedin:https://www.linkedin.com/in/faruk-seker/
github:https://github.com/F4ruk-seker

"""


class BubbleSort:
    def __init__(self, _list: list):
        self.__list: list = _list
    
    def get_result(self) -> list:
        self.__sort()
        return self.__list
    
    def __sort(self) -> None:
        for first_index in range(len(self.__list) - 1, 0, -1):
            for second_index in range(first_index):
                if self.__list[second_index] > self.__list[second_index + 1]:
                    _ = self.__list[second_index]
                    self.__list[second_index] = self.__list[second_index + 1]
                    self.__list[second_index + 1] = _
        

if __name__ == '__main__':
    import random
    random.seed(100)
    test_case = [random.randint(0, 100) for _ in list(range(0, 50))]

    bubble_sort: BubbleSort = BubbleSort(test_case)
    result: list[int] = bubble_sort.get_result()
    print(result)

