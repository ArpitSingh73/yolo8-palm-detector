# 🖐️ Palm Detection using YOLOv8

This repository contains a YOLOv8-based object detection pipeline to **detect human palms from hand images**.  
The project focuses on isolating the palm region only (not full hand or fingers), which is useful for gesture recognition, biometric analysis, and hand-region preprocessing tasks.

---

## 📌 Project Overview

- **Task**: Palm Detection (Single-class object detection)
- **Model**: YOLOv8 (Ultralytics)
- **Annotation Tool**: LabelImg
- **Dataset Source**: Kaggle (Human Palm Images)
- **Framework**: PyTorch + Ultralytics YOLOv8

---

## 📂 Dataset Structure

The dataset is organized in the standard YOLO format:

- Each image has a corresponding `.txt` label file.
- Annotation format follows YOLO standard:

- Single class used:


---

## 🏷️ Annotation Tool

Images were annotated using **LabelImg**:

- Repository: https://github.com/HumanSignal/labelImg
- Output format: YOLO
- Bounding boxes were drawn **only around the palm region**, excluding fingers.

---

## 📊 Dataset Source

- Dataset: **Human Palm Images**
- Source: https://www.kaggle.com/datasets/feyiamujo/human-palm-images

The dataset was cleaned and manually annotated to match the palm-only detection objective.

---

## 🚀 Model Training

The model was trained using **Ultralytics YOLOv8**:

- Repository: https://github.com/ultralytics/ultralytics
- Model variant: YOLOv8 (configurable: n / s / m / l)

### Training Command Example

```bash
yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=50 imgsz=640

path: dataset
train: train/images
val: val/images
test: test/images

nc: 1
names: ['palm']
