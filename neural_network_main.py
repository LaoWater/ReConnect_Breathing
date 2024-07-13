import numpy as np


# Activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))


# Neural Network class
def compute_loss(predicted, actual):
    return np.mean((predicted - actual) ** 2)


class SimpleNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.final_input = None
        self.final_output = None
        self.hidden_output = None
        self.hidden_input = None
        self.weights_input_hidden = np.random.randn(input_size, hidden_size) * 0.01
        self.bias_hidden = np.zeros((1, hidden_size))
        self.weights_hidden_output = np.random.randn(hidden_size, output_size) * 0.01
        self.bias_output = np.zeros((1, output_size))

    def forward_pass(self, inputs):
        self.hidden_input = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = sigmoid(self.hidden_input)
        self.final_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        self.final_output = sigmoid(self.final_input)
        return self.final_output

    def backpropagate(self, inputs, actual, learning_rate):
        # Error in output
        error = self.final_output - actual

        # Gradients for hidden to output weights
        d_weights_hidden_output = np.dot(self.hidden_output.T, error * sigmoid_derivative(self.final_input))

        # Gradients for input to hidden weights
        error_hidden = np.dot(error * sigmoid_derivative(self.final_input), self.weights_hidden_output.T)
        d_weights_input_hidden = np.dot(inputs.T, error_hidden * sigmoid_derivative(self.hidden_input))

        # Update the weights and biases
        self.weights_hidden_output -= learning_rate * d_weights_hidden_output
        self.bias_output -= learning_rate * np.sum(error * sigmoid_derivative(self.final_input), axis=0, keepdims=True)
        self.weights_input_hidden -= learning_rate * d_weights_input_hidden
        self.bias_hidden -= learning_rate * np.sum(error_hidden * sigmoid_derivative(self.hidden_input), axis=0,
                                                   keepdims=True)

    def train(self, inputs, outputs, learning_rate, epochs):
        output, y = None, None
        for epoch in range(epochs):
            for x, y in zip(inputs, outputs):
                output = self.forward_pass(x)
                self.backpropagate(x, y, learning_rate)
            if epoch % 100 == 0:  # Print loss every 100 epochs
                loss = compute_loss(output, y)
                print("Epoch:", epoch, "Loss:", loss)


###################
###################
# Starting Script #
###################
###################




# Neural Network Initialization
nn = SimpleNeuralNetwork(input_size=6, hidden_size=10, output_size=1)
inputs_main = np.array(inputs_main).reshape(1, -1)  # Assuming 'inputs' is already normalized and reshaped correctly
outputs_main = np.array([[0.75]])  # Example target output

# Train the network
nn.train(inputs_main, outputs_main, learning_rate=0.01, epochs=1000)
