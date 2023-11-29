import numpy as np
from typing import List

class KNearestNeighbors:
    def __init__(self, num_neighbors:int, data:np.array=None) -> None:
        self.num_neighbors = num_neighbors
        self.data = data
    
    def _get_ties(self, distances:np.array) -> List[int]:
        """
        Identifies possible ties in the list of distances.
        Ties are identified only according to the k-th nearest neighbor.
        """
        distances_sorted = np.sort(distances)
        for i in range(1, len(distances_sorted)):
            if distances_sorted[i] != distances_sorted[i-1]:
                return list(range(i))


    def _return_neighbors(self, data_point:np.array) -> List[int]:
        """
        Return the index of the closest data point to the given data point.
        """
        distances = np.linalg.norm(self.data - data_point, axis=1)
        sorted_indices = np.argsort(distances)
        return sorted_indices[:self.num_neighbors]

        
