import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os
import tempfile
from datetime import datetime
from ultralytics import YOLO

# Configure page
st.set_page_config(
    page_title="🦟 Drosophila Detector",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Model path
YOLO_MODEL_PATH = "/home/user/runs/detect/train3/weights/best.pt"

class YOLODetector:
    def __init__(self):
        self.model = self.load_model()

    @staticmethod
    @st.cache_resource
    def load_model():
        try:
            if not os.path.exists(YOLO_MODEL_PATH):
                st.error(f"YOLO model not found at: {YOLO_MODEL_PATH}")
                st.info("Please check if the model path is correct")
                return None
            model = YOLO(YOLO_MODEL_PATH)
            st.sidebar.success("✅ Model loaded successfully!")
            return model
        except Exception as e:
            st.error(f"Error loading model: {e}")
            return None

    def process_frame(self, frame):
        if self.model is None:
            return frame, 0, 0
        
        try:
            results = self.model(frame)
            annotated_frame = results[0].plot()
            
            # Count males and females
            males = sum(1 for box in results[0].boxes if int(box.cls[0]) == 0)
            females = sum(1 for box in results[0].boxes if int(box.cls[0]) == 1)
            
            return annotated_frame, males, females
        except Exception as e:
            st.error(f"Error processing frame: {e}")
            return frame, 0, 0

def display_stats(males, females):
    col1, col2, col3 = st.columns(3)
    total = males + females
    col1.metric("Total Detected 🎯", total)
    col2.metric("Males 🦟", males, f"{(males/total*100):.1f}%" if total > 0 else "0%")
    col3.metric("Females 🦋", females, f"{(females/total*100):.1f}%" if total > 0 else "0%")

def main():
    st.title("🦟 Drosophila Detection System")
    
    # Initialize detector
    detector = YOLODetector()
    
    # Input method selection
    input_method = st.radio(
        "Select Input Method",
        ["Real-time Camera", "Upload Image", "Upload Video", "Record Video"],
        horizontal=True
    )

    if input_method == "Real-time Camera":
        st.header("📹 Real-time Detection")
        
        col1, col2, col3 = st.columns(3)
        start_cam = col1.button("▶️ Start Camera")
        stop_cam = col2.button("⏹️ Stop Camera")
        capture = col3.button("📸 Capture Frame")

        if start_cam:
            cap = cv2.VideoCapture(0)
            st.info("Camera started! Detection in progress...")
            
            frame_placeholder = st.empty()
            stats_placeholder = st.empty()
            
            while cap.isOpened() and not stop_cam:
                ret, frame = cap.read()
                if not ret:
                    st.error("Cannot read from camera!")
                    break
                
                # Process frame
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                processed_frame, males, females = detector.process_frame(frame_rgb)
                
                # Display results
                frame_placeholder.image(processed_frame, channels="RGB", use_column_width=True)
                with stats_placeholder:
                    display_stats(males, females)
                
                if capture:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"capture_{timestamp}.jpg"
                    cv2.imwrite(filename, cv2.cvtColor(processed_frame, cv2.COLOR_RGB2BGR))
                    st.success(f"✅ Image saved as {filename}")
                    break
            
            cap.release()

    elif input_method == "Upload Image":
        st.header("🖼️ Image Detection")
        
        uploaded_file = st.file_uploader(
            "Upload an image",
            type=['jpg', 'jpeg', 'png']
        )
        
        if uploaded_file:
            image = Image.open(uploaded_file)
            image_np = np.array(image)
            
            with st.spinner("Processing image..."):
                processed_image, males, females = detector.process_frame(image_np)
            
            st.image(processed_image, caption="Processed Image", use_column_width=True)
            display_stats(males, females)

    elif input_method == "Upload Video":
        st.header("🎥 Video Detection")
        
        uploaded_file = st.file_uploader(
            "Upload a video",
            type=['mp4', 'avi', 'mov']
        )
        
        if uploaded_file:
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(uploaded_file.read())
            
            st.info("Processing video... Please wait.")
            cap = cv2.VideoCapture(tfile.name)
            
            frame_placeholder = st.empty()
            stats_placeholder = st.empty()
            progress_bar = st.progress(0)
            
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            current_frame = 0
            
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                processed_frame, males, females = detector.process_frame(frame_rgb)
                
                frame_placeholder.image(processed_frame, channels="RGB", use_column_width=True)
                with stats_placeholder:
                    display_stats(males, females)
                
                current_frame += 1
                progress_bar.progress(current_frame / frame_count)
            
            cap.release()
            os.unlink(tfile.name)
            st.success("✅ Video processing completed!")

    elif input_method == "Record Video":
        st.header("🎬 Video Recording with Detection")
        
        col1, col2, col3 = st.columns(3)
        start_rec = col1.button("⏺️ Start Recording")
        stop_rec = col2.button("⏹️ Stop Recording")
        save_rec = col3.button("💾 Save Recording")
        
        if start_rec:
            st.info("Recording started! Detection in progress...")
            cap = cv2.VideoCapture(0)
            frames = []
            
            frame_placeholder = st.empty()
            stats_placeholder = st.empty()
            recording_time = st.empty()
            
            start_time = datetime.now()
            
            while cap.isOpened() and not stop_rec:
                ret, frame = cap.read()
                if not ret:
                    break
                
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                processed_frame, males, females = detector.process_frame(frame_rgb)
                frames.append(processed_frame)
                
                frame_placeholder.image(processed_frame, channels="RGB", use_column_width=True)
                with stats_placeholder:
                    display_stats(males, females)
                
                # Show recording duration
                duration = datetime.now() - start_time
                recording_time.text(f"⏱️ Recording Time: {duration.seconds} seconds")
            
            cap.release()
            
            if save_rec and frames:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                video_filename = f"recording_{timestamp}.mp4"
                
                with st.spinner("Saving video..."):
                    height, width = frames[0].shape[:2]
                    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                    out = cv2.VideoWriter(video_filename, fourcc, 20.0, (width, height))
                    
                    for frame in frames:
                        out.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
                    
                    out.release()
                st.success(f"✅ Video saved as {video_filename}")

if __name__ == "__main__":
    main()
