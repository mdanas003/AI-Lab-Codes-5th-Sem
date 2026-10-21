import numpy as np

# Training data: [size in sq ft, bedrooms]
X = np.array([
    [1000, 2],
    [1500, 3],
    [1800, 3],
    [2400, 4],
    [3000, 4]
], dtype=float)

# House price (in thousands)
y = np.array([200, 280, 320, 420, 500], dtype=float)

m = len(y)

# Feature scaling (mean 0, std 1) so gradient descent converges
mean = X.mean(axis=0)
std = X.std(axis=0)
X_scaled = (X - mean) / std

# Initialize parameters
w = np.zeros(2)
b = 0.0

learning_rate = 0.1
epochs = 1000


def predict(X, w, b):
    # y_hat = w1*x1 + w2*x2 + b
    return np.dot(X, w) + b


def cost(X, y, w, b):
    # Mean Squared Error cost: J = (1/2m) * sum((y_hat - y)^2)
    error = predict(X, w, b) - y
    return np.sum(error ** 2) / (2 * m)


# Gradient Descent
for epoch in range(epochs):

    error = predict(X_scaled, w, b) - y

    # Gradients
    dw = np.dot(X_scaled.T, error) / m
    db = np.sum(error) / m

    # Parameter update
    w = w - learning_rate * dw
    b = b - learning_rate * db

    if epoch % 100 == 0 or epoch == epochs - 1:
        print("Epoch:", epoch, "Cost:", round(cost(X_scaled, y, w, b), 4))

print("\nWeights (scaled features):", w)
print("Bias:", b)

# Predict a new house: 2000 sq ft, 3 bedrooms
new_house = np.array([2000, 3], dtype=float)
new_scaled = (new_house - mean) / std

print("\nPredicted price for", new_house, "->",
      round(predict(new_scaled, w, b), 2))
