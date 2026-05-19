from gra_transfinite import ReflectiveNullifier, DirtyState, FiniteOrdinal

def step(s):
    return DirtyState(max(0, s.M - 1))
def foam(s):
    return FiniteOrdinal(s.M)
def limit(hist):
    return DirtyState(min(s.M for s in hist))

ref = ReflectiveNullifier(step, foam, limit, limit_period=5)
print(f"Уровень рефлексии до: {ref.reflection_level}, период={ref.limit_period}")

# Запускаем обычное обнуление
init = DirtyState(20)
final = ref.run(init)
print(f"Обычный финал: {final}, пена={foam(final)}")

# Теперь рефлексируем
ref.reflect()
print(f"После отражения уровень: {ref.reflection_level}, период={ref.limit_period}")
init2 = DirtyState(20)
final2 = ref.run(init2)
print(f"После рефлексии: {final2}, пена={foam(final2)}")
