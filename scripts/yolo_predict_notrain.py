from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("yolo11n.pt")


results = model("../bdd_to_yolo/dataset_yolo_converted/images/test/cb078020-ab5a89f2.jpg")  # Predict on an image
results[0].show()  # Display results
model.val(data = "../bdd_to_yolo/dataset_yolo_converted/bdd100k_ultralytics.yaml")
print(model.names)
