import unittest
from gra_transfinite import FiniteOrdinal, transfinite_nullify

class State:
    def __init__(self, x): self.x = x

class TestNullification(unittest.TestCase):
    def test_reaches_zero(self):
        step = lambda s: State(s.x - 1) if s.x > 0 else s
        foam = lambda s: FiniteOrdinal(s.x)
        limit = lambda h: h[-1]
        final = transfinite_nullify(State(5), step, foam, limit, limit_period=3)
        self.assertEqual(foam(final).is_zero(), True)

    def test_foam_non_increasing(self):
        step = lambda s: State(max(0, s.x - 2))
        foam = lambda s: FiniteOrdinal(s.x)
        limit = lambda h: State(min(s.x for s in h))
        init = State(10)
        final = transfinite_nullify(init, step, foam, limit, limit_period=2)
        self.assertTrue(foam(final).is_zero())

if __name__ == '__main__':
    unittest.main()
