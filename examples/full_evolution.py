"""
Сквозной пример: от хаоса к истине с эволюцией субъекта и рефлексией.
"""

from gra_transfinite import SubjectState, FiniteOrdinal, evolve_subject, ReflectiveNullifier

class FullState(SubjectState):
    def __repr__(self):
        return f"FullState(W={self.M}, S={self.S})"

def step(s: FullState) -> FullState:
    # Убираем одну единицу беспорядка, усиливаем субъект
    return FullState(max(0, s.M - 1), s.S + 1)

def foam(s: FullState) -> FiniteOrdinal:
    return FiniteOrdinal(s.M)

def limit(hist):
    best = max(hist, key=lambda s: s.S)
    return FullState(0, best.S)  # мир очищен, субъект максимальный

# Запуск эволюции
init = FullState(world_model=15, self_layer=0)
final_subject = evolve_subject(init, step, foam, limit, limit_period=4, max_steps=100)
print(f"Итоговый субъект: {final_subject}")

# Добавляем рефлексивный слой
ref_null = ReflectiveNullifier(step, foam, limit, limit_period=4)
ref_null.reflect()  # усиливаем обнулёнку
final_ref = ref_null.run(init)
print(f"После рефлексивного обнуления: {final_ref}")
