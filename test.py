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

def check_image():
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

    sunflower_url = "dog1.png"

    img = load_img(path=sunflower_url, target_size=(32, 32))
    img_array = tf.keras.utils.img_to_array(img)


    sample_label = "cat"
    prediction = np.argmax(model.predict(
        img_array.reshape(-1, *img_array.shape))[0])
    print("Predicted label:", categories[prediction])
    print("True label:", sample_label)


    # show the image
    plt.axis('on')
    # plt.imshow(img)
    plt.show()
    return prediction == 3 and categories[prediction] == sample_label

print(check_image())