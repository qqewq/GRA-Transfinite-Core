import unittest
from gra_transfinite.truth_theory import TruthRank
from gra_transfinite.utils import FiniteOrdinal

class MockState:
    def __init__(self, d): self.d = d

class TestTruthRank(unittest.TestCase):
    def test_finite_rank(self):
        step = lambda s: MockState(s.d - 1)
        foam = lambda s: FiniteOrdinal(s.d)
        limit = lambda h: h[-1]
        tracker = TruthRank(step, foam, limit, limit_period=10)
        tracker.run_and_track(MockState(5), max_steps=100)
        self.assertIsInstance(tracker.rank_ordinal(), FiniteOrdinal)
        self.assertEqual(tracker.successor_steps, 5)

if __name__ == '__main__':
    unittest.main()
