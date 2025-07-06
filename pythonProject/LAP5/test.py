import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys

def load_model(filename):
    data = np.load(filename)
    W1, b1, W2, b2 = data['W1'], data['b1'], data['W2'], data['b2']
    return W1, b1, W2, b2

def relu(Z):
    return np.maximum(0, Z)

def softmax(Z):
    expZ = np.exp(Z - np.max(Z, axis=1, keepdims=True))
    return expZ / np.sum(expZ, axis=1, keepdims=True)

def forward_propagation(X, W1, b1, W2, b2):
    Z1 = np.dot(X, W1) + b1
    A1 = relu(Z1)
    Z2 = np.dot(A1, W2) + b2
    A2 = softmax(Z2)
    return np.argmax(A2, axis=1)

def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Error: Unable to load image.")
        sys.exit(1)
    img = cv2.resize(img, (28, 28))
    img = img.astype(np.float32) / 255.0
    img = img.flatten().reshape(1, -1)  # Chuyển về dạng phù hợp với mô hình
    return img

def predict(image_path, model_path="mnist_digit_recognition_model.npz"):
    W1, b1, W2, b2 = load_model(model_path)
    img = preprocess_image(image_path)
    prediction = forward_propagation(img, W1, b1, W2, b2)
    return prediction[0]

def show_image_with_prediction(image_path, prediction):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    plt.imshow(img, cmap='gray')
    plt.title(f'Predicted: {prediction}')
    plt.axis('off')
    plt.show()

# Chạy thử nghiệm với một ảnh
test_image_path = "bw_0.jpg"  # Đổi thành đường dẫn ảnh thực tế
pred = predict(test_image_path)
show_image_with_prediction(test_image_path, pred)