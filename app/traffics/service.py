import os
from keras.models import load_model
from sklearn.metrics import mean_squared_error

model = load_model("app/common/model.h5")

def nad_predict(inputs):
  outputs = model.predict(inputs)
  mse = mean_squared_error(outputs, inputs)
  if mse > float(os.environ.get("ANOMALY_THRESHOLD")):
    return "anomaly"
  else:
    return "normal"