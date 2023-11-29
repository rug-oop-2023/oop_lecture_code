import unittest

import numpy as np

import sys
sys.path.append('lab_assignments/01b.knn')
import knn

class KNearestNeighborsTest(unittest.TestCase):
    def setUp(self):
        self.dataset = np.array([
                [0,0],
                [1,2],
                [2,0],
                [4,1],
                [5,0],
                [6,2]
            ])

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
    
    def test_return_single_neighbor(self):
        knn_model = knn.KNearestNeighbors(1, self.dataset)
        test_point = np.array([0,1])
        neighbor_index = knn_model._return_neighbors(test_point)[0]
        self.assertEqual(neighbor_index, 0)

        test_point = np.array([2,1])
        neighbor_index = knn_model._return_neighbors(test_point)[0]
        self.assertEqual(neighbor_index, 2)
    
    def test_return_two_neighbors(self):
        knn_model = knn.KNearestNeighbors(2, self.dataset)
        test_point = np.array([1,1])
        neighbor_indices = knn_model._return_neighbors(test_point)
        self.assertSetEqual(set(neighbor_indices), {0,1})

    def test_return_n_neighbors(self):
        knn_model = knn.KNearestNeighbors(3, self.dataset)
        test_point = np.array([1,1])
        neighbor_indices = knn_model._return_neighbors(test_point)
        self.assertSetEqual(set(neighbor_indices), {0,1,2})
        test_point = np.array([5,1])
        neighbor_indices = knn_model._return_neighbors(test_point)
        self.assertSetEqual(set(neighbor_indices), {3,4,5})
        
        knn_model = knn.KNearestNeighbors(5, self.dataset)
        test_point = np.array([3,2])
        neighbor_indices = knn_model._return_neighbors(test_point)
        self.assertSetEqual(set(neighbor_indices), {1,2,3,4,5})
    
    def test_get_ties(self):
        distances = np.array([0,0,1])
        knn_model = knn.KNearestNeighbors(1)
        ties_index = knn_model._get_ties(distances)
        self.assertListEqual(ties_index, [0,1])