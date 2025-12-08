

---

# AI_X Project — BDD-100K Dataset + YOLOv11 Training Guide

본 프로젝트에서는 **BDD-100K 데이터셋**을 **YOLOv11** 모델에 맞게 변환하여
학습 가능한 구조로 만드는 전체 과정을 설명합니다.

---

# 🚗 BDD-100K Dataset

공식 다운로드 링크
➡️ [http://bdd-data.berkeley.edu/download.html](http://bdd-data.berkeley.edu/download.html)

BDD-100K는 총 **100,000장**의 이미지와 라벨로 구성된 대규모 자율주행 데이터셋입니다.

---

## 📥 1. BDD-100K 데이터 다운로드

<img width="600" src="https://github.com/user-attachments/assets/a101e81c-80c8-4474-9c47-fa2862b275ae" />

BDD-100K 페이지에서 **100K Images**, **Labels**를 다운로드합니다.

⚠️ **주의사항**
10K Images에는라벨 누락 이미지가 많아 학습 오류가 발생합니다.

<img width="600" src="https://github.com/user-attachments/assets/89cdf7c6-2e19-45fe-b0dc-51da99bf9697" />

따라서 **100K Images + Labels 다운로드를 권장**합니다.

---

# 🗂️ 2. YOLO 학습을 위한 Dataset 구조 만들기

YOLO는 다음과 같은 디렉토리 구조를 요구합니다:

<img width="550" src="https://github.com/user-attachments/assets/774dcd85-18a2-4b44-8e94-014c474b0d11" />

BDD-100K의 원본 라벨은 JSON 기반이므로, YOLO 라벨(txt) 형식으로 변환이 필요합니다.

YOLO 라벨 형식은 다음과 같습니다:

```
class x_center y_center width height
```

<img width="500" src="https://github.com/user-attachments/assets/a3ac8eae-9235-410d-a504-20540278a70b" />

---

# 🛠️ 3. 개발 환경 설정

## ✔️ 가상환경 생성

```bash
python3 -m venv venv
source venv/bin/activate
```

## ✔️ 의존성 설치

```bash
cd bdd_to_yolo
pip install -r requirements.txt
pip install PyYAML opencv-python
```

---

# 🔍 4-1. 데이터 필터링 (Subset 생성)

BDD-100K는 크기 때문에,
config.yaml 기반으로 목적에 맞는 데이터만 필터링합니다.

<img width="600" src="https://github.com/user-attachments/assets/d497ad85-8e85-4c53-bcba-14c67aeff609" />

```bash
python3 make_bdd_subset.py --config config.yaml
```

📌 출력 경로

```
bdd_to_yolo/bdd100k_subset_filtered/
```

---

# 🔄 4-2. BDD-100K → YOLO 포맷 변환

```bash
cd bdd_to_yolo
python3 converter.py
```

<img width="600" src="https://github.com/user-attachments/assets/77d54f7a-8e0b-41a2-abca-3cbf8f6161d3" />

---

# 👀 5-1. 이미지–라벨 매칭 확인

라벨과 이미지가 잘 매칭되었는지 시각적으로 확인합니다.

<img width="600" src="https://github.com/user-attachments/assets/5a87ee15-9d39-42c9-897e-480904a617c3" />

---

# 🖼️ 5-2. YOLO 라벨 시각화 확인

```bash
python3 viz_yolo_labels.py
```

`yolo_viz/` 폴더가 생성됩니다.

<img width="600" src="https://github.com/user-attachments/assets/01a175e7-33d6-4978-909b-9f3d2825b1d9" />

<img width="600" src="https://github.com/user-attachments/assets/be31c1f9-a7cf-4cd7-8d7b-b147ca044204" />

---

# 🎉 완료!

이제 데이터셋을 YOLOv11 학습 가능한 구조로 변환했습니다.
`train.py` 또는 `YOLO().train(...)`으로 바로 학습을 진행할 수 있습니다.

---




