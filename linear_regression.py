import numpy as np

class SimpleLinearRegressor:
    def __init__(self, default_intercept:float, default_slope:float):
        self._intercept = default_intercept
        self._slope = default_slope
    
    def train(self, observations:np.ndarray, target:np.ndarray) -> None:
        '''
        observations is a 1d numpy array of length n
        target is a 1d numpy array of length n
        '''
        obs_mean = observations.mean()
        target_mean = target.mean()
        obs_residuals = observations - obs_mean
        target_residuals = target - target_mean
        optimal_weight = (obs_residuals * target_residuals).sum() / (obs_residuals**2).sum()
        self._slope = optimal_weight
        optimal_bias = target_mean - optimal_weight * obs_mean
        self._intercept = optimal_bias

    def predict(self, data:np.ndarray) -> np.ndarray:
        return self._intercept + self._slope * data

if __name__ == "__main__":
    model = SimpleLinearRegressor(0,0)
    model._intercept = 1.0
    print(f"Model intercept is {model._intercept}")