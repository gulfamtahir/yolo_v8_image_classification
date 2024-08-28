!pip install the ultralytics


from ultralytics import YOLO
# Load a model
model = YOLO("yolov8n-cls.pt")# load a pretrained model (recommended for training)
results = model.train(data='/content/data/', epochs=10)  # train the model
