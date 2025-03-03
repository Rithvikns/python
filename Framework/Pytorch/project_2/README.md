# PyTorch CIFAR-10 Classifier: Code Explanation

## Overview
This project implements a Convolutional Neural Network (CNN) with residual connections to classify images from the CIFAR-10 dataset using PyTorch. The model includes data augmentation, learning rate scheduling, checkpoint saving/loading, and TensorBoard logging.

## Dependencies
- `torch`, `torchvision` for deep learning and dataset handling
- `matplotlib`, `numpy` for visualization and numerical operations
- `tensorboard` for logging and tracking model performance

## Code Explanation

### 1. Device Configuration
```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")
```
The model automatically detects GPU availability and runs on CUDA if available. Otherwise, it defaults to CPU.

### 2. Data Preprocessing
```python
transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])
```
- Randomly flips images horizontally and rotates them by up to 10 degrees to introduce variations.
- Converts images to tensors.
- Normalizes pixel values to be in the range [-1, 1].

### 3. Loading CIFAR-10 Dataset
```python
train_dataset = torchvision.datasets.CIFAR10(root='./data', train=True, transform=transform, download=True)
test_dataset = torchvision.datasets.CIFAR10(root='./data', train=False, transform=transform, download=True)
```
- Downloads and loads the CIFAR-10 dataset.
- Applies transformations defined earlier.

```python
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)
```
- Uses `DataLoader` to iterate over the dataset in batches of 64.
- Shuffles training data for randomness.

### 4. Defining the Residual Block
```python
class ResidualBlock(nn.Module):
    def __init__(self, in_channels, out_channels, downsample=False):
```
- Implements a **residual block**, a key component of ResNet architectures.
- If `downsample=True`, it reduces the spatial dimensions using a strided convolution.

```python
identity = x if self.downsample is None else self.downsample(x)
out = F.relu(self.bn1(self.conv1(x)))
out = self.bn2(self.conv2(out))
out += identity
return F.relu(out)
```
- The block adds the original input (`identity`) to the output of two convolutional layers, helping with gradient flow and training deeper networks.

### 5. Defining the CNN Model
```python
class CNN(nn.Module):
```
- Defines a CNN model with batch normalization and residual connections.

```python
self.res1 = ResidualBlock(32, 32)
self.res2 = ResidualBlock(32, 64, downsample=True)
```
- Stacks two residual blocks for feature extraction.

```python
self.pool = nn.AdaptiveAvgPool2d((1, 1))
```
- Adapts pooling to ensure the output has a fixed size regardless of input dimensions.

```python
self.fc = nn.Linear(64, 10)
```
- Fully connected layer with 10 outputs for CIFAR-10’s 10 classes.

### 6. Defining Loss, Optimizer, and Scheduler
```python
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)
```
- Uses **cross-entropy loss** for multi-class classification.
- **Adam optimizer** updates weights efficiently.
- **StepLR scheduler** reduces learning rate by 10× every 10 epochs.

### 7. Training Loop
```python
def train(epoch):
    model.train()
    running_loss = 0.0
```
- Sets model to training mode (`model.train()`).
- Iterates over batches, computes loss, performs backpropagation (`loss.backward()`), and updates weights (`optimizer.step()`).
- Logs loss every 100 mini-batches.

### 8. Testing Loop
```python
def test():
    model.eval()
    correct = 0
    total = 0
```
- Switches to evaluation mode (`model.eval()`).
- Uses `torch.no_grad()` to disable gradient tracking for efficiency.
- Computes accuracy over the test dataset.

### 9. Checkpointing (Saving & Loading)
```python
def save_checkpoint():
    torch.save({'model_state_dict': model.state_dict(), 'optimizer_state_dict': optimizer.state_dict()}, checkpoint_path)
```
- Saves model and optimizer state.

```python
def load_checkpoint():
    if os.path.exists(checkpoint_path):
        checkpoint = torch.load(checkpoint_path)
        model.load_state_dict(checkpoint['model_state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        print("Checkpoint Loaded!")
```
- Loads a saved model and optimizer state if available.

### 10. Training Execution
```python
load_checkpoint()
num_epochs = 20
for epoch in range(num_epochs):
    train(epoch)
    acc = test()
    writer.add_scalar('accuracy', acc, epoch)
    save_checkpoint()
```
- Loads a checkpoint (if available), trains for 20 epochs, evaluates after each epoch, logs accuracy, and saves the model.

---

## Input & Output

### **Input:**
- **CIFAR-10 dataset** (60,000 images, 10 classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck)
- 32×32 RGB images

### **Output:**
- A trained model that classifies images into one of 10 categories.
- Checkpoints (`model_checkpoint.pth`) for resuming training.
- Training logs in TensorBoard (`runs/cifar10_experiment`).
- Final test accuracy (printed in the console, typically around **70-80%**).

---

## Summary of Features Covered
✔ **GPU Acceleration** (`cuda`)  
✔ **Data Augmentation** (`transforms`)  
✔ **Custom Residual Blocks** (`nn.Module`)  
✔ **Adam Optimizer & LR Scheduling** (`optim.Adam`, `StepLR`)  
✔ **Training & Evaluation Loops**  
✔ **Checkpointing & Model Persistence**  
✔ **TensorBoard Logging** (`SummaryWriter`)

This implementation demonstrates a complete deep learning workflow using PyTorch. 🚀

