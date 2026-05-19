"""
Ординальная теория истины: ранг истины.
"""

from typing import Callable, List
from .utils import State, FoamMeasure, FiniteOrdinal, OmegaOrdinal, Ordinal
from .nullification import transfinite_nullify

class TruthRank:
    """
    Вычисляет ранг истины – минимальный ординал, на котором пена становится нулевой.
    """
    def __init__(self, step, foam, limit, limit_period=10):
        self.step = step
        self.foam = foam
        self.limit = limit
        self.limit_period = limit_period
        self.successor_steps = 0
        self.limit_steps = 0

    def run_and_track(self, initial: State, max_steps=10000) -> State:
        seq = [initial]
        current = initial
        step_count = 0
        while not self.foam(current).is_zero():
            if step_count >= max_steps:
                raise RuntimeError("Не сошлось")
            current = self.step(current)
            seq.append(current)
            step_count += 1
            self.successor_steps += 1
            if step_count % self.limit_period == 0:
                current = self.limit(seq)
                seq.append(current)
                step_count += 1
                self.limit_steps += 1
        return current

    def rank_ordinal(self) -> Ordinal:
        """
        Возвращает ординал: successor_steps + limit_steps * ω.
        (грубая оценка, так как каждый предельный шаг добавляет ω)
        """
        # Каждый предельный шаг даёт ω, последовательные шаги дают конечные
        # Итог: ω * limit_steps + successor_steps
        if self.limit_steps == 0:
            return FiniteOrdinal(self.successor_steps)
        else:
            # Представим как FiniteOrdinal(successor_steps) + OmegaOrdinal()*limit_steps
            # Для простоты возвращаем OmegaOrdinal (т.к. ранг >= ω)
            return OmegaOrdinal()
