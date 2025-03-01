# CNN Model Code
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
## Step 1
The model is sequential so the input image is passed through the first layer , The image shape is 32x32 pixels and 3 colors RGB to represent the image.
layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3))


The convolution 2D layer applies 32 filters of size 3x3 pixels and the output size is determined using the formula:

Output Size = ((Input Size - Filter Size + 2 × Padding)/Stride) + 1


Given:


Input Shape: (32, 32, 3)


Filter Size: (3×3)


Stride: 1 (default)


Padding: 0 (since no padding='same' is used)

Output Height = (32−3+0)+1=30


Output Width = (32−3+0) +1=30


Output Channels = 32


Output Channels=32 


So, the output shape of this layer is (30, 30, 32).


This means that each filter creates a new feature map of size 30x30.

## Step 2

The next layer is layers.MaxPooling2D((2, 2) . Here in this layer you are downscaling the spatial dimension of feature maps further while keeping the most important information.
Pool size = (2,2): This means we take the maximum value from each 2×2 region.
Stride = (2,2) (default): The window moves 2 pixels right/down at a time, reducing the size by half.
Output Size
=
Input Size
Pool Size
Output Size= 
Pool Size
Input Size
​
 
Output Height
=
30
2
=
15
Output Height= 
2
30
​
 =15
Output Width
=
30
2
=
15
Output Width= 
2
30
​
 =15
Output Channels
=
32
Output Channels=32
Final Output Shape:
(
15
,
15
,
32
)
(15,15,32)
