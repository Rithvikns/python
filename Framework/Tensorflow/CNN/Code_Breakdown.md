# CNN Model Code

import tensorflow as tf
from tensorflow.keras import layers, models

# Define the CNN Model
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

# Code Breakdown

## Step 1: Input Layer & First Convolutional Layer

- The model is sequential, so the input image is passed through the first layer.
- The image shape is (32,32,3), meaning 32x32 pixels with 3 color channels (RGB).

Code: layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3))

The convolutional layer applies 32 filters of size 3x3 pixels. The output size is determined by:

    Output Size = ((Input Size - Filter Size + 2 * Padding) / Stride) + 1

Given:
- Input Shape: (32, 32, 3)
- Filter Size: (3×3)
- Stride: 1 (default)
- Padding: 0 (since padding='same' is not used)

Output Height = (32 - 3 + 0) + 1 = 30
Output Width = (32 - 3 + 0) + 1 = 30
Output Channels = 32

So, the output shape of this layer is (30, 30, 32).
Each filter creates a new feature map of size 30x30.

## Step 2: Max Pooling Layer

- The next layer, layers.MaxPooling2D((2,2)), reduces the spatial dimensions of feature maps.
- Pool size = (2,2): It takes the maximum value from each 2×2 region.
- Stride = (2,2) (default): The window moves 2 pixels right/down at a time, reducing the size by half.

Formula:
    Output Size = Input Size / Pool Size

Output Height = 30 / 2 = 15
Output Width = 30 / 2 = 15
Output Channels = 32 (unchanged)

Final Output Shape: (15, 15, 32)
"""

## Step 3 : layers.Conv2D(64, (3, 3), activation='relu')

This would be the same as first step but the input is (15,15,32)
Output Height = (15 - 3 + 0) + 1 = 13
Output Width = (15 - 3 + 0) + 1 = 13
Output Channels = 64
So, the output shape of this layer is (13, 13, 64).

## Step 4 : layers.MaxPooling2D((2, 2))

This would be the same as first step but the input is (15,15,32)
If the input size is not divisible by maxpooling layer it excludes the last row and column and make it divisible 
Output Height = 13 / 2 = 6
Output Width = 13 / 2 = 6
Output Channels = 64 (unchanged)
So, the output shape of this layer is (6, 6, 64).

## Step 5 : layers.Conv2D(128, (3, 3), activation='relu')

Output Height = (6 - 3 + 0) + 1 = 4
Output Width = (6 - 3 + 0) + 1 = 4
Output Channels = 128
So, the output shape of this layer is (4, 4, 128).

## Step 6 : layers.Flatten()

It removes the spatial structure and reshapes the tensor into a 1D array.

The total number of elements is calculated as: 4×4×128=2048
The output shape becomes (2048,) which is a 1D vector with 2048 elements.

## Step 7: Dense Layer with ReLU Activation

Code: layers.Dense(128, activation='relu')

- The `Dense(128)` layer contains 128 neurons, fully connected to the previous 2048 inputs.
- Computes: `Z = W * X + B` where:
    - **X** = input vector (2048 values)
    - **W** = weight matrix (2048 × 128)
    - **B** = bias vector (128 values)
    - **Z** = output vector (128 values)
- ReLU Activation:
    - If `Z > 0`, it remains unchanged.
    - If `Z <= 0`, it becomes 0.
- Output Shape: (128,)

This prepares the model for further classification or output layers.
"""
## Step 8: Final Dense Layer with Softmax Activation

Code: layers.Dense(10, activation='softmax')

- This is the final layer, typically used for **multi-class classification**.
- The **10 neurons** correspond to **10 possible classes** (e.g., CIFAR-10 dataset).
- Computes: `Z = W * X + B`, where:
    - **X** = input vector (128 values)
    - **W** = weight matrix (128 × 10)
    - **B** = bias vector (10 values)
    - **Z** = output vector (10 values)

- **Softmax Activation Function**:
    - Converts raw scores (**logits**) into **probabilities**.
    - Formula:

      \[
      P_i = \frac{e^{Z_i}}{\sum_{j=1}^{10} e^{Z_j}}
      \]

    - Ensures that all outputs sum to **1**, making it a **valid probability distribution**.

- Example Output:
  ```
  [0.02, 0.01, 0.05, 0.10, 0.07, 0.03, 0.20, 0.30, 0.12, 0.10]
  ```
  - The **highest probability** determines the predicted class.



