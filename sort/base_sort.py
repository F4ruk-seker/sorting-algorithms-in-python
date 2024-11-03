from typing import Any, Union, NoReturn
from performance import get_performance_metric


class Sort:
    def __init__(self, _list: list):
        self.list: list = _list

    def get_result(self) -> list:
        self.sort()
        return self.list

    def sort(self):
        raise 'Result Case Write To Here'

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
    @staticmethod
    @get_performance_metric
    def test(test_range: int = 30, *args, **kwargs) -> NoReturn:
        raise NotImplementedError()