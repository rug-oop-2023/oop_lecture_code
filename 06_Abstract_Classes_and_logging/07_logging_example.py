import logging
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Load Iris dataset
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Initialize a Decision Tree model
model = DecisionTreeClassifier()

# Manually train the model in steps to log accuracy
for depth in range(1, 10):
    model.set_params(max_depth=depth)
    model.fit(X_train, y_train)
    train_accuracy = accuracy_score(y_train, model.predict(X_train))
    test_accuracy = accuracy_score(y_test, model.predict(X_test))
    
    # Logging the accuracy
    logging.info(f"Training at depth {depth}, Train Accuracy: {train_accuracy}, Test Accuracy: {test_accuracy}")
