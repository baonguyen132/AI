import numpy as np

# Load dữ liệu
data = np.load('mnist.npz')
x_train, y_train = data['x_train'], data['y_train']
x_test, y_test = data['x_test'], data['y_test']

# Chuẩn hóa dữ liệu
x_train = x_train.reshape(-1, 784) / 255.0
x_test = x_test.reshape(-1, 784) / 255.0

# Chuyển nhãn thành one-hot vector
def to_categorical(y, num_classes=10):
    return np.eye(num_classes)[y]

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

input_size = 784   # 28 x 28 ảnh
hidden_size = 128  # số lượng nơ-ron trong lớp ẩn
output_size = 10   # 10 chữ số đầu ra

# Khởi tạo trọng số và bias
np.random.seed(42)
W1 = np.random.randn(input_size, hidden_size) * 0.01
b1 = np.zeros((1, hidden_size))
W2 = np.random.randn(hidden_size, output_size) * 0.01
b2 = np.zeros((1, output_size))

def relu(Z):
    return np.maximum(0, Z)

def softmax(Z):
    expZ = np.exp(Z - np.max(Z, axis=1, keepdims=True))
    return expZ / np.sum(expZ, axis=1, keepdims=True)

def compute_loss(Y, A2):
    m = Y.shape[0]
    logprobs = -np.log(A2[range(m), np.argmax(Y, axis=1)])
    loss = np.sum(logprobs) / m
    return loss

def forward_propagation(X):
    Z1 = np.dot(X, W1) + b1
    A1 = relu(Z1)
    Z2 = np.dot(A1, W2) + b2
    A2 = softmax(Z2)
    cache = (Z1, A1, Z2, A2)
    return A2, cache

def relu_derivative(Z):
    return Z > 0

def backward_propagation(X, Y, cache):
    global W1, b1, W2, b2
    Z1, A1, Z2, A2 = cache
    m = X.shape[0]

    dZ2 = A2 - Y
    dW2 = np.dot(A1.T, dZ2) / m
    db2 = np.sum(dZ2, axis=0, keepdims=True) / m

    dA1 = np.dot(dZ2, W2.T)
    dZ1 = dA1 * relu_derivative(Z1)
    dW1 = np.dot(X.T, dZ1) / m
    db1 = np.sum(dZ1, axis=0, keepdims=True) / m

    gradients = {"dW1": dW1, "db1": db1, "dW2": dW2, "db2": db2}
    return gradients

def update_parameters(gradients, learning_rate=0.01):
    global W1, b1, W2, b2
    W1 -= learning_rate * gradients["dW1"]
    b1 -= learning_rate * gradients["db1"]
    W2 -= learning_rate * gradients["dW2"]
    b2 -= learning_rate * gradients["db2"]


def train(X, Y, num_iterations=2000, learning_rate=0.01):
    for i in range(num_iterations):
        A2, cache = forward_propagation(X)
        loss = compute_loss(Y, A2)
        gradients = backward_propagation(X, Y, cache)
        update_parameters(gradients, learning_rate)

        if i % 100 == 0:
            print(f"Iteration {i}, loss: {loss}")


train(x_train[:2000], y_train[:2000], num_iterations=2000, learning_rate=0.01)
np.savez("mnist_digit_recognition_model.npz", W1=W1, b1=b1, W2=W2, b2=b2)
print("Model saved successfully!")

