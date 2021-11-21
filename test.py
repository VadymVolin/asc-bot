from sys import path

from PIL.Image import Image
from neuralink import load_data, batch_size
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
# example of converting an image with the Keras API
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img

# CIFAR-10 classes
categories = {
    0: "airplane",
    1: "automobile",
    2: "bird",
    3: "cat",
    4: "deer",
    5: "dog",
    6: "frog",
    7: "horse",
    8: "ship",
    9: "truck"
}

# загрузим тестовый набор
ds_train, ds_test, info = load_data()
# загрузим итоговую модель с весовыми коэффициентами
model = load_model("results/cifar10-model-v1.h5")

# оценка
loss, accuracy = model.evaluate(
    ds_test, steps=info.splits["test"].num_examples // batch_size)
print("Тестовая оценка:", accuracy*100, "%")

# получить прогноз для этого изображения
data_sample = next(iter(ds_test))

img = Image.open("cat.jpg").batch(32)
# img_array = img_to_array(img)
img_array = tf.keras.preprocessing.image.img_to_array(img)
print(img_array.dtype)
print(img_array.shape)

sample_label = "cat"
sample_image = tf.convert_to_tensor(img_array, dtype=tf.int32)
# sample_image = tf.image.convert_image_dtype(sample_image, dtype=tf.float32)
sample_image = np.array(img_array)
prediction = np.argmax(model.predict(
    sample_image.reshape(-1, *sample_image.shape))[0])
print("Predicted label:", categories[prediction])
print("True label:", sample_label)

# show the image
plt.axis('off')
plt.imshow(img)
plt.show()
