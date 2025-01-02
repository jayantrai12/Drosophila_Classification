# Real-Time Drosophila Detection App

Welcome to the **Real-Time Drosophila Detection App**! This repository provides real-time detection of male and female Drosophila (fruit flies) using state-of-the-art deep learning models. Models used include **ResNet50**, **ResNet18**, **InceptionV3**, **MobileNet**, **Detectron2**, and **YOLOv8**. Additionally, an APK file and a **Streamlit app** have been created for easy accessibility and real-time interaction.

---

## 🚀 Features

- **Multi-Model Integration:** Detection using various models including ResNet, Inception, MobileNet, YOLOv8, and Detectron2.
- **Real-Time Detection:** Leverage a webcam for detecting Drosophila in real time.
- **APK and Web Integration:** User-friendly APK for mobile detection and a Streamlit-based web app.
- **Saved Models:** Pre-trained models provided for quick deployment.
- **Interactive Interface:** Streamlit app with features for live video detection, image capture, and confidence threshold adjustment.

---

## 📑 Table of Contents

- [🚀 Features](#-features)
- [🛠️ Installation](#-installation)
- [⚙️ Usage](#-usage)
- [📦 Dependencies](#-dependencies)
- [🤖 Model Information](#-model-information)
- [📄 License](#-license)
- [📧 Contact](#-contact)
- [🙏 Acknowledgments](#-acknowledgments)
- [📊 Future Improvements](#-future-improvements)

---

## 🛠️ Installation

Follow the steps below to set up and run the application on your local machine:

### **1. Clone the Repository**

```bash
git clone https://github.com/jayantrai12/Drosophila_Classification
cd real-time-drosophila-detection
```

### **2. Create a Virtual Environment**

#### Using Python's `venv`:

Create a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Using Conda (Linux):

Create and activate a Conda environment:

```bash
conda create -n drosophila_detection python=3.8 -y
conda activate drosophila_detection
```

### **3. Install Dependencies**

Install the required libraries from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### **4. Install Detectron2**

Detectron2 requires additional setup based on your system and CUDA version. Refer to the [Detectron2 Installation Guide](https://detectron2.readthedocs.io/en/latest/tutorials/install.html).

For example:

```bash
pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu113/torch1.10/index.html
```

### **5. Verify Saved Models**

In the Releases section, you will find the saved models, which can be directly downloaded and used without additional placement requirements. The models are pre-configured and ready to use without additional placement requirements.

---

## ⚙️ Usage

### **1. Run the Streamlit App**

To start the Streamlit app for real-time detection:

```bash
streamlit run app.py
```

This will open a local web interface for real-time Drosophila detection.

### **2. Use the APK File**

The APK file is available for direct download and installation on your Android device. The app is designed for seamless real-time detection. Follow the in-app instructions to perform real-time detection.

---

## 📦 Dependencies

The following libraries are required to run this application:

- **Python**: >= 3.8
- **TensorFlow**: Deep learning framework for ResNet, Inception, and MobileNet models.
- **Streamlit**: Interactive web framework for the app.
- **OpenCV**: Image processing and real-time detection.
- **NumPy**: Numerical computing.
- **PyTorch**: Deep learning framework for Detectron2.
- **Torchvision**: Models and image utilities for PyTorch.
- **Detectron2**: Object detection and segmentation library.
- **Ultralytics**: YOLOv8 framework.
- **Matplotlib & Seaborn**: Visualization libraries.

Refer to `requirements.txt` for the complete list of dependencies and their versions.

---

## 🤖 Model Information

### **Included Models**

- **ResNet50 & ResNet18:** Pre-trained CNN models for image classification and detection.
- **InceptionV3:** Google’s model optimized for large-scale visual recognition.
- **MobileNet:** Lightweight CNN for mobile devices.
- **Detectron2:** Facebook AI Research’s next-gen object detection framework.
- **YOLOv8:** High-performance object detection model.

### **Saved Models**

Pre-trained models are available in the `saved_models` folder or via the repository’s [Releases](https://github.com/jayantrai12/Drosophila_Classification/releases/tag/Saved_Models).

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📧 Contact

For any questions or suggestions, feel free to reach out:

- **GitHub:** [jayantrai12](https://github.com/jayantrai12)
- **Email:** jayantrai7500@gmail.com

---

## 🙏 Acknowledgments

Special thanks to:

- **Detectron2:** Facebook AI Research.
- **Streamlit:** Interactive web app framework.
- **YOLOv8:** Ultralytics for their high-performance detection model.
- **[Dr. Ishaan Gupta](https://beb.iitd.ac.in/ishaan.html):** For mentorship and guidance.

---

## 📊 Future Improvements

- Expand detection to include additional Drosophila species or stages.
- Integrate new lightweight models for enhanced mobile performance.
- Deploy the app on cloud platforms for broader accessibility.
- Optimize inference speed and latency.

---

Happy Detecting!

