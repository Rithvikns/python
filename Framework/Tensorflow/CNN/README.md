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
#### Explanation of Layers:
1. **`Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3))`**:
   - Applies **32 filters** of size **3x3** to detect features in the input image.
   - Uses **ReLU activation** to introduce non-linearity.
   - Takes input images of shape **(32, 32, 3)** (RGB image).

2. **`MaxPooling2D((2, 2))`**:
   - Performs **down-sampling** to reduce the spatial dimensions of feature maps.
   - Takes the maximum value in each **2x2** region, reducing computation and improving generalization.

3. **`Conv2D(64, (3, 3), activation='relu')`**:
   - Another convolutional layer with **64 filters** of size **3x3**.
   - Helps the network learn more complex patterns.

4. **`MaxPooling2D((2, 2))`**:
   - Further reduces the feature map size, preventing overfitting.

5. **`Conv2D(128, (3, 3), activation='relu')`**:
   - Third convolutional layer with **128 filters** of size **3x3**.
   - Extracts deeper image features.

6. **`Flatten()`**:
   - Converts the 2D feature maps into a **1D vector** so they can be processed by the fully connected layers.

7. **`Dense(128, activation='relu')`**:
   - A fully connected layer with **128 neurons** and **ReLU activation**.
   - Captures complex representations from extracted features.

8. **`Dense(10, activation='softmax')`**:
   - The output layer with **10 neurons** (one per class in CIFAR-10).
   - Uses **softmax activation** to output class probabilities.

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
