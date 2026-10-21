import numpy as np

# Training data: [hours studied, previous score]
X = np.array([
    [1, 30],
    [2, 40],
    [3, 45],
    [4, 55],
    [5, 60],
    [6, 75],
    [7, 80],
    [8, 90]
], dtype=float)

# Labels: 0 = fail, 1 = pass
y = np.array([0, 0, 0, 0, 1, 1, 1, 1], dtype=float)

m = len(y)

# Feature scaling
mean = X.mean(axis=0)
std = X.std(axis=0)
X_scaled = (X - mean) / std

w = np.zeros(2)
b = 0.0

learning_rate = 0.1
epochs = 1000


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def cost(y, y_hat):
    # Binary cross-entropy
    eps = 1e-15
    y_hat = np.clip(y_hat, eps, 1 - eps)
    return -np.mean(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))


# Gradient Descent
for epoch in range(epochs):

    z = np.dot(X_scaled, w) + b
    y_hat = sigmoid(z)

    error = y_hat - y

    dw = np.dot(X_scaled.T, error) / m
    db = np.sum(error) / m

    w = w - learning_rate * dw
    b = b - learning_rate * db

    if epoch % 100 == 0 or epoch == epochs - 1:
        print("Epoch:", epoch, "Cost:", round(cost(y, y_hat), 4))

print("\nWeights:", w)
print("Bias:", b)

# Predictions (threshold 0.5)
probs = sigmoid(np.dot(X_scaled, w) + b)
predictions = (probs >= 0.5).astype(int)

print("\nPredictions:")
for x, p, label in zip(X, probs, predictions):
    print(x, "-> probability:", round(p, 3), "class:", label)

print("\nAccuracy:", np.mean(predictions == y) * 100, "%")
