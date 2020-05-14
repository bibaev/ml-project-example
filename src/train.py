import os
import sys
from typing import List

import tensorflow as tf


def compile_model(model):
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])


def train(x_train, y_train):
    # Reshaping the array to 4-dims so that it can work with the Keras API
    x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
    input_shape = (28, 28, 1)
    # Making sure that the values are float so that we can get decimal points after division
    x_train = x_train.astype('float32')
    # Normalizing the RGB codes by dividing it to the max RGB value.
    x_train /= 255
    print('x_train shape:', x_train.shape)
    print('Number of images in x_train', x_train.shape[0])
    # Importing the required Keras modules containing model and layers
    print("Before importing keras")
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
    # Creating a Sequential Model and adding the layers
    model = Sequential()
    model.add(Conv2D(28, kernel_size=(3, 3), input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())  # Flattening the 2D arrays for fully connected layers
    model.add(Dense(128, activation=tf.nn.relu))
    model.add(Dropout(0.2))
    model.add(Dense(10, activation=tf.nn.softmax))
    print("Model initialized!")
    compile_model(model)
    print("Model compiled!")
    model.fit(x=x_train, y=y_train, epochs=1)
    return model


def save_to(model, dir: str):
    model_json = model.to_json()
    os.makedirs(dir, exist_ok=True)
    with open(os.path.join(dir, "model.json"), "w") as json_file:
        json_file.write(model_json)
    model.save_weights(os.path.join(dir, "weights.h5"))


def main(argv: List[str]):
    (x_train, y_train), _ = tf.keras.datasets.mnist.load_data()
    print(sys.getsizeof(x_train))
    model = train(x_train, y_train)
    if len(argv) == 1:
        dir_to_save = argv[0]
        print(f"Save model to {dir_to_save}")
        save_to(model, dir_to_save)


if __name__ == '__main__':
    main(sys.argv[1:])
