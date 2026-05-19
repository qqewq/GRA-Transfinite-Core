"""
Трансфинитный оператор обнуления N.
"""

from typing import Callable, List, Optional
from .utils import State, FoamMeasure

def transfinite_nullify(
    initial: State,
    step: Callable[[State], State],
    foam: Callable[[State], FoamMeasure],
    limit: Callable[[List[State]], State],
    limit_period: int = 10,
    max_steps: int = 10000,
    verbose: bool = False
) -> State:
    """
    Итеративно применяет оператор N с предельными шагами каждые limit_period итераций.
    Останавливается, когда Φ(Ψ) = 0.
    """
    seq: List[State] = [initial]
    current = initial
    step_count = 0

    while not foam(current).is_zero():
        if step_count >= max_steps:
            raise RuntimeError(f"Превышен лимит шагов {max_steps}, пена не обнулилась.")

        current = step(current)
        seq.append(current)
        step_count += 1

        # Предельный шаг (эмуляция предельного ординала)
        if step_count % limit_period == 0 and step_count > 0:
            if verbose:
                print(f"[L] Предельный шаг на шаге {step_count}")
            current = limit(seq)
            seq.append(current)
            step_count += 1  # считаем предельный шаг как один шаг

    return current
