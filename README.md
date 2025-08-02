# 🌾 Rice and Wheat Leaf Disease Detection using CNN

This project implements a **Convolutional Neural Network (CNN)** for the classification of rice and wheat leaf diseases. It leverages image processing and deep learning to identify common plant diseases, helping farmers and researchers take timely and accurate decisions in crop management.

---

## 📌 Project Overview

The system is trained to detect the following classes:

### 🌾 Rice Diseases:
- Bacterial Leaf Blight
- Brown Spot
- Leaf Blast
- Leaf Scald
- Narrow Brown Spot
- Healthy

### 🌿 Wheat Diseases:
- Brown Rust
- Septoria
- Yellow Smut
- Healthy

By classifying leaf images into these categories, the system can be used in the field for fast and reliable disease diagnosis.

---

## 🗂️ Repository Structure

```bash
Rice-Wheat-Leaf-Disease-Detection/
├── Applications/
│   ├── chatbot.py             # Script for chatbot interface (if applicable)
│   ├── main.py                # Script to load the model and run predictions
│   └── requirements.txt       # Python dependencies
│
├── Dataset/
│   ├── train/                 # Training dataset (images in class-wise folders)
│   ├── test/                  # Testing dataset
│   └── val/                   # Validation dataset
│
├── Jupyter Notebook/
│   ├── train_model.ipynb      # Jupyter notebook to train the CNN model
│   └── test_model.ipynb       # Jupyter notebook to test the trained model
│
├── Models/
│   ├── trained_model.h5       # Saved model in HDF5 format
│   └── trained_model.keras    # Saved model in native Keras format
│
└── README.md                  # Project documentation (this file)
```

# ⚙️ Setup Instructions
Follow these steps to get the project up and running:

## 1. Clone the repository
```bash
git clone https://github.com/your-username/Rice-Wheat-Leaf-Disease-Detection.git
cd Rice-Wheat-Leaf-Disease-Detection
```

## 2. Install required dependencies
```bash
pip install -r Applications/requirements.txt
```

## 3. Add and Setup .env file in Applications/
Use the following format
```bash
GOOGLE_API_KEY = <YOUR API KEY>
disease_info = {}
```

## 4. Run Application
Activate your python environment
```bash
cd Applications
streamlit run main.py
```

## Technologies Used
- Python
- TensorFlow / Keras
- NumPy
- Pandas
- Matplotlib
- Jupyter Notebook

## Model Performance
### Model: Traditional CNN
- Accuracy: ~89% on test data
- Evaluation Metrics: Accuracy, Precision, Recall, F1-score

## Contact
Ganashree K N
ganashree99045@gmail.com
https://www.linkedin.com/in/ganashree-k-n-37a53633b/
