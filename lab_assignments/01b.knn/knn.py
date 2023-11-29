import numpy as np
from typing import List

class KNearestNeighbors:
    def __init__(self, num_neighbors:int, data:np.array=None) -> None:
        self.num_neighbors = num_neighbors
        self.data = data
    
    def _return_neighbors(self, data_point:np.array) -> List[int]:
        """
        Return the index of the closest data point to the given data point.
        """
        return [0]

        
