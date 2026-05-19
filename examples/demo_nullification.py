"""
Демонстрация трансфинитной обнулёнки: удаление противоречий.
"""

from gra_transfinite import State, FiniteOrdinal, transfinite_nullify

# Простое состояние: количество "грязных" узлов
class DirtyState(State):
    def __init__(self, dirt: int):
        super().__init__(world_model=dirt)
    def __repr__(self):
        return f"DirtyState(dirt={self.M})"

def step(state: DirtyState) -> DirtyState:
    # Каждый шаг очищаем один узел
    return DirtyState(max(0, state.M - 1))

def foam(state: DirtyState) -> FiniteOrdinal:
    return FiniteOrdinal(state.M)

def limit(history: list[State]) -> DirtyState:
    # Берем состояние с минимальной пеной (последнее стабильное)
    best = min(history, key=lambda s: foam(s))
    return DirtyState(best.M)

init = DirtyState(dirt=25)
final = transfinite_nullify(init, step, foam, limit, limit_period=5, verbose=True)
print(f"Итог: {final}, пена={foam(final)}")
