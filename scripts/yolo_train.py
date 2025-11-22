from ultralytics import YOLO
 
model = YOLO("yolo11n.pt") 
trained = model.train( data = "../bdd_to_yolo/dataset_yolo_converted/bdd100k_ultralytics.yaml",
                       epochs = 30,
                       imgsz = 640, 
                       device ="0") 
metrics = model.val() 
# show 1 images 
results = model("../bdd_to_yolo/dataset_yolo_converted/images/test/cb078020-ab5a89f2.jpg") 
results[0].show() 
path = model.export(format="onnx")
