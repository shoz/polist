from polist import PartialOrderedList as POL
import unittest
import itertools

class PartialOrderedListTests(unittest.TestCase):
    def setUp(self):
        pass
    def _make_candidates(self, l):
        return [list(x) for x in itertools.product(l, repeat=len(l))]
    def test1(self):
        objects = []
        answers = []
        objects.append(POL([(0, 0), (1, 1)]))
        answers.append([[0, 1]])
        objects.append(POL([(0, 0), (1, 1), (2, 0)]))
        answers.append([[0, 1, 2], [2, 1, 0]])
        objects.append(POL([(0, 0), (1, 0), (2, 1), (3, 1), (4, 2), (5, 2)]))
        answers.append([[0, 1, 2, 3, 4, 5], [1, 0, 2, 3, 4, 5],
                        [0, 1, 3, 2, 4, 5], [1, 0, 3, 2, 4, 5],
                        [0, 1, 2, 3, 5, 4], [0, 1, 3, 2, 5, 4],
                        [1, 0, 2, 3, 5, 4], [1, 0, 3, 2, 5, 4]])
        objects.append(POL([(0, 0), (1, 1), (1, 1)]))
        answers.append([[0, 1, 1]])
        objects.append(POL([(0, 'A'), (1, 'A'), (2, 'B')]))
        answers.append([[0, 1, 2], [1, 0, 2]])
        for obj, answer in zip(objects, answers):
            for candidate in self._make_candidates(obj):
                if candidate in answer:
                    print obj, '==', candidate
                    assert obj == candidate
                else:
                    print obj, '!=', candidate
                    assert obj != candidate
