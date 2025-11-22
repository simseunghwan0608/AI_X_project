from ultralytics import YOLO

model = YOLO("./runs/detect/train/weights/best.pt")


results = model("../bdd_to_yolo/dataset_yolo_converted/images/test/cb078020-ab5a89f2.jpg")  # Predict on an image
results[0].show() 
model.val(data ="../bdd_to_yolo/dataset_yolo_converted/bdd100k_ultralytics.yaml")
print(model.names)
