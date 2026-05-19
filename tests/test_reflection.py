import unittest
from gra_transfinite import ReflectiveNullifier, FiniteOrdinal

class State:
    def __init__(self, d): self.d = d

class TestReflection(unittest.TestCase):
    def test_reflection_works(self):
        step = lambda s: State(max(0, s.d-1))
        foam = lambda s: FiniteOrdinal(s.d)
        limit = lambda h: State(min(s.d for s in h))
        rn = ReflectiveNullifier(step, foam, limit, limit_period=10)
        self.assertEqual(rn.reflection_level, 0)
        rn.reflect()
        self.assertEqual(rn.reflection_level, 1)
        self.assertEqual(rn.limit_period, 9)
        final = rn.run(State(5))
        self.assertTrue(foam(final).is_zero())

if __name__ == '__main__':
    unittest.main()
