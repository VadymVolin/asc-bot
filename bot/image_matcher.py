from neuralink import load_data, batch_size
import tensorflow as tf
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
# example of converting an image with the Keras API
from keras.preprocessing.image import load_img

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


def check_image(image_path):
    # загрузим тестовый набор
    ds_train, ds_test, info = load_data()
    # загрузим итоговую модель с весовыми коэффициентами
    model = load_model("results/cifar10-model-v2.h5")

    # оценка
    loss, accuracy = model.evaluate(
        ds_test, steps=info.splits["test"].num_examples // batch_size)
    print("Тестовая оценка:", accuracy*100, "%")

    # получить прогноз для этого изображения
    data_sample = next(iter(ds_test))

    image_path = tf.keras.utils.get_file('Test_image', origin=image_path)

    img = load_img(path=image_path, target_size=(32, 32))
    img_array = tf.keras.utils.img_to_array(img)

    sample_label = "cat"
    prediction = np.argmax(model.predict(
        img_array.reshape(-1, *img_array.shape))[0])
    print("Predicted label:", categories[prediction])
    print("Predicted:", prediction)
    print("True label:", sample_label)

    # show the image
    # plt.axis('on')
    # plt.imshow(img)
    # plt.show()
    return prediction == 3 and categories[prediction] == sample_label
