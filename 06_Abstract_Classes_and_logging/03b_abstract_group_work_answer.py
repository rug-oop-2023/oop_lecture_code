from abc import ABC, abstractmethod
from typing import Any, List

from abc import ABC, abstractmethod
from typing import Any, List

class MLModel(ABC):
    """
    Abstract base class for machine learning models.

    This class serves as a template for all machine learning models,
    ensuring that they implement the essential methods `train` and `predict`.

    Methods:
        train(data: List[Any]): Trains the model on the given dataset.
        predict(input_data: Any): Makes a prediction based on the input data.
    """

    @abstractmethod
    def train(self, data: List[Any]) -> None:
        """
        Trains the model on the given dataset.

        Parameters:
            data (List[Any]): The dataset to train the model on. This can be any
                              format that is suitable for the specific model, 
                              typically a list of features and labels.

        Returns:
            None
        """
        pass

    @abstractmethod
    def predict(self, input_data: Any) -> Any:
        """
        Makes a prediction based on the input data.

        Parameters:
            input_data (Any): The input data to make predictions on. The format 
                              of this data should be compatible with the model.

        Returns:
            Any: The prediction result, the format of which depends on the 
                 specific model implementation.
        """
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
