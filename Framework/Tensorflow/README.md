# TensorFlow Overview

TensorFlow is an open-source machine learning framework developed by Google Brain. It is widely used for deep learning applications and provides tools for training and deploying machine learning models.

## Features of TensorFlow
- **Scalability**: Supports CPUs, GPUs, and TPUs(Tensor Processing Units (TPUs) are Google's custom-developed application-specific integrated circuits (ASICs) used to accelerate machine learning workloads) for efficient computation.
- **Flexibility**: Works with deep learning, reinforcement learning, and traditional machine learning.
- **Ecosystem**: Includes TensorFlow Hub, TensorFlow Extended (TFX), and TensorFlow Lite.
- **Auto Differentiation**: Uses TensorFlow’s `tf.GradientTape` for automatic differentiation.
- **Pretrained Models**: Provides access to pre-trained models via TensorFlow Hub.

## Installation
To install TensorFlow using pip, run:
```sh
pip install tensorflow
```
For GPU support, use:
```sh
pip install tensorflow-gpu
```

## Basic Example
```python
import tensorflow as tf

# Define a simple computation
a = tf.constant(2.0)
b = tf.constant(3.0)
c = a + b
print(c.numpy())  # Output: 5.0
```

## TensorFlow Components
1. **Tensors**: Multi-dimensional arrays similar to NumPy arrays.
2. **Graphs and Sessions**: (TF1.x) Computational graphs for efficient execution.
3. **Keras API**: High-level deep learning API (`tf.keras`).
4. **Dataset API**: Handling large datasets efficiently (`tf.data`).
5. **TF Lite**: For deploying models on mobile and edge devices.
6. **TF Serving**: For serving trained models in production.

## Creating a Neural Network with TensorFlow/Keras
```python
from tensorflow import keras
from tensorflow.keras import layers

# Define model
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(10,)),
    layers.Dense(1, activation='sigmoid')
])

# Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Summary
model.summary()
```

## Training a Model
```python
import numpy as np

# Generate random data
X_train = np.random.rand(1000, 10)
y_train = np.random.randint(2, size=(1000,))

# Train model
model.fit(X_train, y_train, epochs=10, batch_size=32)
```

## TensorFlow Ecosystem
- **TensorFlow Hub**: Repository of pre-trained models.
- **TensorFlow Lite**: Lightweight ML models for mobile and IoT.
- **TensorFlow.js**: Running models in browsers using JavaScript.
- **TensorFlow Extended (TFX)**: End-to-end ML pipeline.

## Deployment with TensorFlow Serving
To serve a trained model:
```sh
tensorflow_model_server --rest_api_port=8501 --model_name=my_model --model_base_path=/models/my_model/
```

## Useful Resources
- [Official Documentation](https://www.tensorflow.org/)
- [GitHub Repository](https://github.com/tensorflow/tensorflow)
- [TensorFlow Hub](https://www.tensorflow.org/hub)

---

This file provides an overview of TensorFlow and its core functionalities. For more advanced usage, refer to the official TensorFlow documentation.
