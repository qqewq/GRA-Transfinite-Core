"""
Базовые ординальные структуры и GRA-состояния.
"""

from abc import ABC, abstractmethod
from typing import Any

class Ordinal(ABC):
    """Абстрактный ординал."""
    @abstractmethod
    def is_zero(self) -> bool:
        pass

    @abstractmethod
    def __lt__(self, other: 'Ordinal') -> bool:
        pass

    def __le__(self, other: 'Ordinal') -> bool:
        return self < other or self == other

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        pass

    def __gt__(self, other: 'Ordinal') -> bool:
        return not (self <= other)

class FiniteOrdinal(Ordinal):
    """Конечный ординал (натуральное число)."""
    def __init__(self, n: int):
        if n < 0:
            raise ValueError("Ordinal must be non-negative")
        self.n = n

    def is_zero(self) -> bool:
        return self.n == 0

    def __lt__(self, other: Ordinal) -> bool:
        if isinstance(other, FiniteOrdinal):
            return self.n < other.n
        elif isinstance(other, OmegaOrdinal):
            return True  # любое конечное < ω
        return NotImplemented

    def __eq__(self, other: object) -> bool:
        if isinstance(other, FiniteOrdinal):
            return self.n == other.n
        return False

    def __repr__(self):
        return str(self.n)

class OmegaOrdinal(Ordinal):
    """Ординал ω (первый бесконечный)."""
    def is_zero(self) -> bool:
        return False

    def __lt__(self, other: Ordinal) -> bool:
        if isinstance(other, OmegaOrdinal):
            return False
        return False  # ω не меньше любого конечного

    def __eq__(self, other: object) -> bool:
        return isinstance(other, OmegaOrdinal)

    def __repr__(self):
        return "ω"

# Мера пены – частный случай ординала
FoamMeasure = Ordinal

class State:
    """Базовое состояние GRA: (M, S, A)."""
    def __init__(self, world_model: Any = None, self_layer: Any = None, action: Any = None):
        self.M = world_model
        self.S = self_layer
        self.A = action
