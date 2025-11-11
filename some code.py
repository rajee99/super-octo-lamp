# digits_nn.py
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import accuracy_score

# Load dataset (8x8 images flattened to 64 features)
digits = load_digits()
X, y = digits.data, digits.target

# Normalize features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# One-hot encode labels
enc = OneHotEncoder(sparse_output=False)
y_encoded = enc.fit_transform(y.reshape(-1, 1))

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Network architecture
input_dim = X_train.shape[1]   # 64
hidden_dim = 64
output_dim = 10
lr = 0.1
epochs = 3000

# Xavier initialization
rng = np.random.default_rng(42)
W1 = rng.uniform(-np.sqrt(6/(input_dim+hidden_dim)), np.sqrt(6/(input_dim+hidden_dim)), (input_dim, hidden_dim))
b1 = np.zeros((1, hidden_dim))
W2 = rng.uniform(-np.sqrt(6/(hidden_dim+output_dim)), np.sqrt(6/(hidden_dim+output_dim)), (hidden_dim, output_dim))
b2 = np.zeros((1, output_dim))

# Activation functions
def relu(z): return np.maximum(0, z)
def drelu(a): return (a > 0).astype(float)
def softmax(z):
    e = np.exp(z - np.max(z, axis=1, keepdims=True))
    return e / e.sum(axis=1, keepdims=True)

def cross_entropy(y_true, y_pred):
    eps = 1e-12
    y_pred = np.clip(y_pred, eps, 1 - eps)
    return -np.mean(np.sum(y_true * np.log(y_pred), axis=1))

# Training loop
for epoch in range(1, epochs+1):
    # Forward
    z1 = X_train @ W1 + b1
    a1 = relu(z1)
    z2 = a1 @ W2 + b2
    y_hat = softmax(z2)

    # Loss
    loss = cross_entropy(y_train, y_hat)

    # Backpropagation
    m = X_train.shape[0]
    dz2 = (y_hat - y_train) / m
    dW2 = a1.T @ dz2
    db2 = dz2.sum(axis=0, keepdims=True)

    da1 = dz2 @ W2.T
    dz1 = da1 * drelu(a1)
    dW1 = X_train.T @ dz1
    db1 = dz1.sum(axis=0, keepdims=True)

    # Gradient update
    W2 -= lr * dW2
    b2 -= lr * db2
    W1 -= lr * dW1
    b1 -= lr * db1

    # Monitor progress
    if epoch % 500 == 0 or epoch == 1:
        preds = np.argmax(y_hat, axis=1)
        labels = np.argmax(y_train, axis=1)
        acc = accuracy_score(labels, preds)
        print(f"Epoch {epoch:4d} | Loss: {loss:.4f} | Train Acc: {acc:.3f}")

# Evaluate
z1 = X_test @ W1 + b1
a1 = relu(z1)
z2 = a1 @ W2 + b2
y_pred = softmax(z2)
acc_test = accuracy_score(np.argmax(y_test, axis=1), np.argmax(y_pred, axis=1))
print(f"\nTest Accuracy: {acc_test:.3f}")
