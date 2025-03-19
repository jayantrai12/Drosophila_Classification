import argparse
import os
import cv2
import numpy as np
from ultralytics import YOLO
from pathlib import Path

# Define default paths
DEFAULT_MODEL_DIR = "/fungel/JAYANT_work/jayant2/saved_models/Object Detection/Yolov8"
DEFAULT_MODEL_NAME = "best.pt"
DEFAULT_MODEL_PATH = os.path.join(DEFAULT_MODEL_DIR, DEFAULT_MODEL_NAME)
OUTPUT_DIR = "/fungel/JAYANT_work/jayant2/new_output"

# Function to check if the model exists
def check_model(model_path):
    if not os.path.exists(model_path):
        print(f"❌ Model file not found at {model_path}")
        exit(1)

# Function to process an image
def process_image(image_path, model):
    image = cv2.imread(image_path)
    if image is None:
        return None, None, None

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = model(image_rgb)
    annotated_image = results[0].plot()

    detected_classes = []
    if results[0].boxes is not None and hasattr(results[0].boxes, 'cls'):
        detected_classes = results[0].boxes.cls.cpu().numpy().astype(int).tolist()

    males = detected_classes.count(1)  # Assuming '1' is Male
    females = detected_classes.count(0)  # Assuming '0' is Female

    return annotated_image, males, females

# Function to process all images in a folder
def process_folder(folder_path, model):
    image_files = [f for f in Path(folder_path).glob("*") if f.suffix.lower() in [".jpg", ".jpeg", ".png"]]
    
    if not image_files:
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    for img_path in image_files:
        annotated_image, males, females = process_image(str(img_path), model)
        if annotated_image is not None:
            output_path = os.path.join(OUTPUT_DIR, os.path.basename(img_path))
            cv2.imwrite(output_path, cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR))
            print(f"{os.path.basename(img_path)} | Male = {males}, Female = {females} | Saved to: {output_path}")

# Main function
def main():
    parser = argparse.ArgumentParser(description="Drosophila Gender Classification using YOLO")
    parser.add_argument("--image", type=str, help="Path to a single image file")
    parser.add_argument("--folder", type=str, help="Path to a folder containing multiple images")
    parser.add_argument("--model_path", type=str, default=DEFAULT_MODEL_PATH, help="Path to the YOLO model")
    
    args = parser.parse_args()

    # Check if model exists
    check_model(args.model_path)
    
    # Load the YOLO model
    model = YOLO(args.model_path)

    if args.image:
        annotated_image, males, females = process_image(args.image, model)
        if annotated_image is not None:
            output_path = os.path.join(OUTPUT_DIR, os.path.basename(args.image))
            os.makedirs(OUTPUT_DIR, exist_ok=True)
            cv2.imwrite(output_path, cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR))
            print(f"{os.path.basename(args.image)} | Male = {males}, Female = {females} | Saved to: {output_path}")

    elif args.folder:
        process_folder(args.folder, model)

if __name__ == "__main__":
    main()

