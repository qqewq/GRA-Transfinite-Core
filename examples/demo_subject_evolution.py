from gra_transfinite import SubjectState, FiniteOrdinal, evolve_subject

class EgoState(SubjectState):
    def __init__(self, world, self_layer):
        super().__init__(world_model=world, self_layer=self_layer, action="think")
    def __repr__(self):
        return f"EgoState(W={self.M}, S={self.S})"

def step(state: EgoState) -> EgoState:
    # Улучшаем согласованность: повышаем S, если мир позволяет
    if state.M > 0:
        return EgoState(state.M - 1, state.S + 1)
    return EgoState(state.M, state.S)

def foam(state: EgoState) -> FiniteOrdinal:
    return FiniteOrdinal(state.M)  # пена = оставшийся беспорядок в мире

def limit(history):
    # Предельный субъект – с наилучшим S среди очищенных
    best = max(history, key=lambda s: s.S)
    return EgoState(0, best.S)  # мир обнулён, субъект сохранён

init = EgoState(world=8, self_layer=0)
final = evolve_subject(init, step, foam, limit, limit_period=3)
print(f"Финальный субъект: {final}")
