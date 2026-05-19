"""
Ординальная эволюция субъектного слоя S^(α).
"""

from .utils import State, FoamMeasure
from .nullification import transfinite_nullify
from typing import Callable, List, Any

class SubjectState(State):
    """Состояние с явным субъектным слоем."""
    def __init__(self, world_model: Any, self_layer: Any, action: Any):
        super().__init__(world_model, self_layer, action)

def evolve_subject(
    initial: SubjectState,
    step: Callable[[SubjectState], SubjectState],
    foam: Callable[[SubjectState], FoamMeasure],
    limit: Callable[[List[SubjectState]], SubjectState],
    limit_period: int = 10,
    max_steps: int = 1000
) -> SubjectState:
    """
    Прогоняет субъектное состояние через трансфинитную обнулёнку.
    Возвращает финальное состояние с развившимся субъектным слоем.
    """
    result = transfinite_nullify(
        initial, step, foam, limit, limit_period, max_steps
    )
    return result
