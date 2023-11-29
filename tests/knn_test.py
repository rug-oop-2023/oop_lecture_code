import unittest

import numpy as np

import sys
sys.path.append('lab_assignments/01b.knn')
import knn

class KNearestNeighborsTest(unittest.TestCase):
    def test_init_k(self):
        num_neighbors = 3
        knn_model = knn.KNearestNeighbors(num_neighbors)
        self.assertEqual(knn_model.num_neighbors, num_neighbors)
    
    def test_init_data(self):
        num_neighbors = 3
        sample_data = np.array([[1,2,3],[4,5,6]])
        knn_model = knn.KNearestNeighbors(num_neighbors)
        self.assertEqual(knn_model.data, None)
        knn_model = knn.KNearestNeighbors(num_neighbors, sample_data)
        np.testing.assert_array_equal(knn_model.data, sample_data)