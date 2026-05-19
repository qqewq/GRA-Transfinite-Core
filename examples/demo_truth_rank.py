from gra_transfinite import FiniteOrdinal, transfinite_nullify, TruthRank
from demo_nullification import DirtyState, step, foam, limit

init = DirtyState(dirt=12)
tracker = TruthRank(step, foam, limit, limit_period=5)
final = tracker.run_and_track(init)
print(f"Ранг истины (ординал): {tracker.rank_ordinal()}")
print(f"Последовательных шагов: {tracker.successor_steps}, предельных: {tracker.limit_steps}")
