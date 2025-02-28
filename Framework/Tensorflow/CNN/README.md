# CIFAR-10 Image Classification using TensorFlow

## Overview
This project implements a **Convolutional Neural Network (CNN)** using TensorFlow to classify images from the CIFAR-10 dataset. The model is trained and evaluated using TensorFlow's Keras API.

## Dataset
The **CIFAR-10 dataset** consists of **60,000 color images** (32x32 pixels) divided into **10 classes**:
- Airplane
- Automobile
- Bird
- Cat
- Deer
- Dog
- Frog
- Horse
- Ship
- Truck

Each class contains **6,000 images**. The dataset is split into **50,000 training images** and **10,000 test images**.

## Code Explanation

### 1. Importing Required Libraries
```python
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np
```
This imports TensorFlow for building and training the model, Matplotlib for visualization, and NumPy for handling numerical operations.

### 2. Loading and Preprocessing the Dataset
```python
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

# Normalize pixel values to be between 0 and 1
x_train, x_test = x_train / 255.0, x_test / 255.0
```
The dataset is loaded using Keras' built-in function. The pixel values are normalized to range between 0 and 1 for better training stability.

### 3. Defining the CNN Model
```python
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])
```
The CNN consists of:
- **Three convolutional layers** with ReLU activation
- **Two max pooling layers** to reduce feature map size
- **Flatten layer** to convert feature maps into a 1D array
- **Dense layers** for classification, using softmax activation for multi-class probability output

### 4. Compiling the Model
```python
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
```
The model uses **Adam optimizer**, **sparse categorical cross-entropy** as the loss function, and accuracy as the metric.

### 5. Training the Model
```python
history = model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))
```
The model is trained for **10 epochs** using the training set and validated with the test set.

### 6. Evaluating the Model
```python
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f"Test accuracy: {test_acc:.4f}")
```
This evaluates the model’s performance on the test dataset.

### 7. Plotting Training History
```python
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()
```
The training and validation accuracy trends are visualized over the epochs.

## Conclusion
This CNN model effectively classifies CIFAR-10 images with decent accuracy. Further improvements can be made by **data augmentation, hyperparameter tuning, or using a deeper architecture**.
