import numpy as np
from keras.models import load_model
import tensorflow as tf
from generate import generate_random_color, show_color

loaded_model = load_model("weight/predicted_rgb_based_color.keras")

color_predict = generate_random_color()
show_color(color_predict)

predict = loaded_model.predict(tf.Variable([color_predict]))
predictions = np.argmax(predict)

print(predict)
print(predictions)