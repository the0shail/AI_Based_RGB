import tensorflow as tf
import keras
from keras import layers
from generate import create_trains, show_color, generate_random_color
import numpy as np

model = keras.Sequential(
    [
        layers.Dense(6, activation="relu", name="layer1"),
        layers.Dense(3, activation="softmax", name="layer2"),
    ]
)

dataset = create_trains(1000)

x_train = tf.Variable(dataset.x_trains)
y_train = tf.Variable(dataset.y_trains)

model.compile(loss="categorical_crossentropy", optimizer='adam', metrics=['accuracy'])
# ,
model.fit(x_train, y_train, epochs=1000, batch_size=32)

color_predict = generate_random_color()
show_color(color_predict)
predict = model.predict(tf.Variable([color_predict]))
print(predict)
result = np.argmax(predict)

# model.save("weight/predicted_rgb_based_color.keras")
# model.save("weight/predicted_rgb_based_color.h5")

print("\n\n---------------------------------------")
if result == 0:
    print("This color is based on the red color")
if result == 1:
    print("This color is based on the green color")
if result == 2:
    print("This color is based on the blue color")
print("---------------------------------------")
