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

# Summary of the Model
model.summary()

# Code Breakdown

"""
Step 1: Input Layer & First Convolutional Layer

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

Step 2: Max Pooling Layer

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

# Additional layers follow the same pattern, progressively reducing spatial dimensions and increasing depth.
