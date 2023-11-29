import unittest
import sys
sys.path.append('lab_assignments/01b.knn')
import knn

class KNearestNeighborsTest(unittest.TestCase):
    def test_init(self):
        num_neighbors = 3
        knn_model = knn.KNearestNeighbors(num_neighbors)
        self.assertEqual(knn_model.num_neighbors, num_neighbors)