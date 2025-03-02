# **🔍 Understanding Image Processing with PyTorch & ResNet-50**

## **📌 Project Overview**
This project demonstrates how deep learning models process images using **PyTorch** and **ResNet-50** (a pre-trained convolutional neural network). The code:

- Loads an image from a local machine into **Google Colab**
- Preprocesses it (resizing, converting to tensor, normalizing)
- Passes it through a **pre-trained ResNet-50 model**
- Extracts **feature maps** from intermediate layers
- **Visualizes** how the model interprets the image

This helps understand **how convolutional neural networks (CNNs) "see" images** at different layers.

---

## **🛠 What This Code Does**
✅ Uploads and displays the **original image** 📷
✅ Shows the **transformed image** (after resizing & normalization) 🎨
✅ Uses a **pre-trained ResNet-50** model to extract features 🔥
✅ **Visualizes feature maps** from intermediate convolutional layers 👀

---

## **🎯 What Problem Does This Solve?**
### **1️⃣ Understanding How Neural Networks Process Images**
- Instead of treating deep learning as a black box, this code helps visualize **how a CNN extracts features**.
- Early layers detect **edges and textures**, deeper layers capture **shapes and objects**.

### **2️⃣ Feature Visualization for Computer Vision Models**
- Helps analyze **which parts of an image contribute to the final prediction**.
- Useful for debugging models used in **classification, object detection, or segmentation**.

### **3️⃣ Debugging Deep Learning Models**
- If a model is not performing well, visualizing feature maps can show **if it is focusing on the right areas**.
- Helps in improving **model architecture or preprocessing steps**.

---

## **🚀 Where Can You Use This?**
✔ **Image Classification & Object Recognition** – Understand feature extraction.
✔ **Medical Image Analysis (X-rays, MRIs, etc.)** – Check what a model learns from scans.
✔ **Autonomous Vehicles & Robotics** – Visualize road, sign, and obstacle detection.
✔ **Security & Facial Recognition** – Analyze how CNNs identify features in images.

---

## **💻 How to Run the Code**
### **1️⃣ Upload an Image**
Run the following code in **Google Colab** to upload an image from your local machine:
```python
from google.colab import files
uploaded = files.upload()
image_filename = list(uploaded.keys())[0]  # Get uploaded file name
```

### **2️⃣ Install Dependencies (If Not Installed)**
```python
!pip install torch torchvision matplotlib numpy opencv-python
```

### **3️⃣ Run the Full Code**
```python
import torch
import torchvision.transforms as transforms
import torchvision.models as models
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image

# Load Image
image = Image.open(image_filename).convert("RGB")
plt.imshow(image)
plt.axis("off")
plt.title("Original Image")
plt.show()

# Define Transformations for ResNet Input
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
image_tensor = transform(image).unsqueeze(0)

# Load Pretrained ResNet-50 Model
model = models.resnet50(pretrained=True)
model.eval()

# Extract Features from Layer 1
activation = {}
def get_activation(name):
    def hook(model, input, output):
        activation[name] = output.detach()
    return hook
model.layer1.register_forward_hook(get_activation("layer1"))

# Run Forward Pass
with torch.no_grad():
    _ = model(image_tensor)

# Visualize Feature Maps
feature_maps = activation["layer1"].squeeze(0)
fig, axes = plt.subplots(1, 6, figsize=(15,5))
for i in range(6):
    ax = axes[i]
    ax.imshow(feature_maps[i].cpu().numpy(), cmap="viridis")
    ax.axis("off")
    ax.set_title(f"Feature Map {i+1}")
plt.suptitle("Feature Maps from ResNet Layer 1", fontsize=14)
plt.show()
```

---

## **📌 Key Takeaways**
✔ **Visualizes how deep learning models "see" images**
✔ **Helps debug and improve CNN models**
✔ **Supports various applications like medical imaging, security, and self-driving tech**
✔ **Great for understanding deep learning and transfer learning techniques**

### **🌟 Want to Extend This Project?**
- Try extracting feature maps from **layer2, layer3, or layer4**.
- Use a **different pre-trained model** like VGG16 or EfficientNet.
- Train a custom model on your own dataset and visualize its feature maps.

---



