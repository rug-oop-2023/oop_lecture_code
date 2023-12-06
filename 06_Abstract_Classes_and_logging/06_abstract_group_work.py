
"""
Group Work Task:
Create an abstract base class called MLModel for machine learning models. 
This class should define an interface for train and predict methods, 
enforcing all subclasses to implement these methods. Also, use type hints 
to define the types of the parameters for these methods.
"""
from typing import Any, List
# Initial implementation of a Linear Regression Model
class LinearRegressionModel:
    def train(self, data: List[Any]) -> None:
        # Simplified training logic for linear regression
        print("Training Linear Regression Model with data:", data)

    def predict(self, input_data: Any) -> Any:
        # Simplified prediction logic
        print("Predicting with Linear Regression Model for input:", input_data)
        return "predicted_value from Linear Regression Model"

# Initial implementation of a Decision Tree Model
class DecisionTreeModel:
    def train(self, data: List[Any]) -> None:
        # Simplified training logic for decision tree
        print("Training Decision Tree Model with data:", data)

    def predict(self, input_data: Any) -> Any:
        # Simplified prediction logic
        print("Predicting with Decision Tree Model for input:", input_data)
        return "predicted_value from Decision Tree Model"

# Demonstration of usage
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

if __name__ == "__main__":
    main()
