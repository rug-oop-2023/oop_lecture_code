from abc import ABC, abstractmethod
from typing import Any, List

from abc import ABC, abstractmethod
from typing import Any, List

# Abstract base class for ML Models
class MLModel(ABC):
    @abstractmethod
    def train(self, data: List[Any]) -> None:
        pass

    @abstractmethod
    def predict(self, input_data: Any) -> Any:
        pass

# Concrete implementation for Linear Regression Model
class LinearRegressionModel(MLModel):
    def train(self, data: List[Any]) -> None:
        # Simplified training logic for linear regression
        print("Training Linear Regression Model with data:", data)

    def predict(self, input_data: Any) -> Any:
        # Simplified prediction logic
        print("Predicting with Linear Regression Model for input:", input_data)
        return "predicted_value from Linear Regression Model"

# Concrete implementation for Decision Tree Model
class DecisionTreeModel(MLModel):
    def train(self, data: List[Any]) -> None:
        # Simplified training logic for decision tree
        print("Training Decision Tree Model with data:", data)

    def predict(self, input_data: Any) -> Any:
        # Simplified prediction logic
        print("Predicting with Decision Tree Model for input:", input_data)
        return "predicted_value from Decision Tree Model"


def main():
    # Dummy data for demonstration
    data = [1, 2, 3, 4, 5]
    input_data = 3

    # Linear Regression Model usage
    linear_model = LinearRegressionModel()
    linear_model.train(data)
    print(linear_model.predict(input_data))

    # Decision Tree Model usage
    tree_model = DecisionTreeModel()
    tree_model.train(data)
    print(tree_model.predict(input_data))

# Demonstration of usage
if __name__ == "__main__":
    main()
