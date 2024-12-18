# Real-Time Drosophila Detection App

Welcome to the **Real-Time Drosophila Detection App**! This repository provides real-time detection of male and female Drosophila (fruit flies) using state-of-the-art deep learning models. Models used include **ResNet50**, **ResNet18**, **InceptionV3**, **MobileNet**, **Detectron2**, and **YOLOv8**. Additionally, an APK file has been created using a **Streamlit app** for easy accessibility.

---

## 🚀 Features

- **Multi-Model Integration:** Detection using various models including ResNet, Inception, MobileNet, YOLOv8, and Detectron2.
- **Real-Time Detection:** Leverage a webcam for detecting Drosophila in real time.
- **APK Integration:** User-friendly APK for detection via a mobile interface.
- **Saved Models:** Pre-trained models provided for quick deployment.
- **Interactive Interface:** Streamlit app with features for live video detection, image capture, and confidence threshold adjustment.

---

## 📚 Table of Contents

- [🚀 Features](#-features)
- [🛠️ Installation](#️-installation)
- [⚙️ Usage](#️-usage)
- [📦 Dependencies](#-dependencies)
- [🤖 Model Information](#-model-information)
- [📄 License](#-license)
- [📫 Contact](#-contact)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 🛠️ Installation

Follow the steps below to set up and run the application on your local machine:

### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/real-time-drosophila-detection.git
cd real-time-drosophila-detection
```

### **2. Install Dependencies**

Create a virtual environment and install the required libraries:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### **3. Install Detectron2**

Detectron2 requires additional setup based on your system and CUDA version. Refer to the [Detectron2 Installation Guide](https://detectron2.readthedocs.io/en/latest/tutorials/install.html).

For example:

```bash
pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu113/torch1.10/index.html
```

### **4. Verify Saved Models**

Ensure all saved models are downloaded from the repository’s [Releases](https://github.com/your-username/real-time-drosophila-detection/releases) section.

---

## ⚙️ Usage

### **1. Run the Streamlit App**

```bash
streamlit run app.py
```

### **2. Use the APK File**

Install the APK file provided in the repository’s [Releases](https://github.com/your-username/real-time-drosophila-detection/releases) section on your Android device and follow the instructions in the app.

---

## 📦 Dependencies

The following libraries are required to run this application:

- **Python**: >= 3.8
- **Streamlit**: Interactive web framework.
- **OpenCV**: Image processing and real-time detection.
- **NumPy**: Numerical computing.
- **PyTorch**: Deep learning framework.
- **Torchvision**: Models and image utilities for PyTorch.
- **Detectron2**: Object detection and segmentation library.
- **Streamlit-WeRTC**: Real-time video and audio streaming.
- **Pillow**: Image processing library.
- **YOLOv8**: Object detection and tracking.

Refer to `requirements.txt` for the complete list.

---

## 🤖 Model Information

### **Included Models**

- **ResNet50 & ResNet18:** Pre-trained CNN models for image classification and detection.
- **InceptionV3:** Google’s model optimized for large-scale visual recognition.
- **MobileNet:** Lightweight CNN for mobile devices.
- **Detectron2:** Facebook AI Research’s next-gen object detection framework.
- **YOLOv8:** High-performance object detection model.

### **Saved Models**

Pre-trained models are available in the `saved_models` folder or via the repository’s [Releases](https://github.com/your-username/real-time-drosophila-detection/releases).

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📫 Contact

For any questions or suggestions, feel free to reach out:

- **GitHub:** [YourUsername](https://github.com/your-username)
- **Email:** your.email@example.com

---

## 🙏 Acknowledgments

Special thanks to:

- **Detectron2:** Facebook AI Research.
- **Streamlit:** Interactive web app framework.
- **YOLOv8:** Ultralytics for their high-performance detection model.
- **Dr. Ishaan Gupta:** For mentorship and guidance.

---

## 📈 Future Improvements

- Expand detection to include additional Drosophila species or stages.
- Integrate new lightweight models for enhanced mobile performance.
- Deploy the app on cloud platforms for broader accessibility.
- Optimize inference speed and latency.

---

Happy Detecting!
