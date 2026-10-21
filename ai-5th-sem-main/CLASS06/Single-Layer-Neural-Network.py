import numpy as np

# Training data
X = np.array([
    [1, 1],
    [1, 2],
    [2, 1],
    [4, 4],
    [5, 4],
    [4, 5]
])

# Target labels
y = np.array([0, 0, 0, 1, 1, 1])

# Initialize weights and bias
weights = np.zeros(2)
bias = 0

# Learning rate
learning_rate = 0.1

# Number of epochs
epochs = 10


# Step activation function
def step_function(z):
    if z >= 0:
        return 1
    else:
        return 0


# Training
for epoch in range(epochs):

    for i in range(len(X)):

        # Linear combination
        z = np.dot(X[i], weights) + bias

        # Prediction
        y_pred = step_function(z)

        # Error
        error = y[i] - y_pred

        # Weight update
        weights = weights + learning_rate * error * X[i]

        # Bias update
        bias = bias + learning_rate * error

    print("Epoch:", epoch + 1)
    print("Weights:", weights)
    print("Bias:", bias)


# Testing
print("\nPredictions:")

for x in X:

    z = np.dot(x, weights) + bias

    prediction = step_function(z)

    print(x, "->", prediction)