import unittest
from gra_transfinite import SubjectState, FiniteOrdinal, evolve_subject

class MyState(SubjectState): pass

class TestSubjectivity(unittest.TestCase):
    def test_evolve_raises_self_layer(self):
        step = lambda s: MyState(s.M - 1 if s.M > 0 else 0, s.S + 1, s.A)
        foam = lambda s: FiniteOrdinal(s.M)
        limit = lambda h: MyState(0, max(s.S for s in h), h[0].A)
        final = evolve_subject(MyState(3,0,'act'), step, foam, limit, limit_period=5)
        self.assertEqual(final.S, 3)  # все шаги увеличили S
        self.assertEqual(foam(final).is_zero(), True)

if __name__ == '__main__':
    unittest.main()
