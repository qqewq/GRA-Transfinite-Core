"""
Рефлексивные слои GRA: самоулучшающаяся обнулёнка.
"""

from .nullification import transfinite_nullify
from .utils import State, FoamMeasure
from typing import Callable, List

class ReflectiveNullifier:
    """
    Обнулятор, способный модифицировать собственную процедуру обнуления.
    Каждый уровень рефлексии (reflection) усиливает оператор N или предельный переход L.
    """
    def __init__(self, step, foam, limit, limit_period=10):
        self.step = step
        self.foam = foam
        self.limit = limit
        self.limit_period = limit_period
        self.reflection_level = 0

    def reflect(self):
        """
        Повышает уровень рефлексии.
        В реальности здесь меняется сам оператор N на более мощный.
        Для демонстрации просто увеличиваем период предельных шагов,
        делая систему «терпеливее» к накоплению истории.
        """
        self.reflection_level += 1
        self.limit_period = max(1, self.limit_period - 1)  # ускоряем предельные переходы

    def run(self, initial: State) -> State:
        return transfinite_nullify(
            initial, self.step, self.foam, self.limit, self.limit_period
        )
