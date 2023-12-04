class MLModel:
    def train(self, data):
        raise NotImplementedError("Train method needs to be implemented")

    def predict(self, input_data):
        raise NotImplementedError("Predict method needs to be implemented")

class DecisionTree(MLModel):
    def train(self, data):
        print("Training decision tree model with data")

    def predict(self, input_data):
        return "Decision tree prediction"

class NeuralNetwork(MLModel):
    def train(self, data):
        print("Training neural network model with data")

    def predict(self, input_data):
        return "Neural network prediction"

if __name__ == "__main__":

    # Creating instances of the models
    tree_model = DecisionTree()
    nn_model = NeuralNetwork()

    # Training the models
    training_data = [1,2,3] #This is just an example. Your data can have a different structure.
    tree_model.train(training_data)
    nn_model.train(training_data)

    # Making predictions
    test_data = [1,2,3]
    print(tree_model.predict(test_data))  # Outputs: Decision tree prediction
    print(nn_model.predict(test_data))    # Outputs: Neural network prediction