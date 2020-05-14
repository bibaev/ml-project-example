import os
import sys
from typing import List

import tensorflow as tf
from tensorflow.python.keras.models import model_from_json

from train import compile_model


def evaluate(model, x_test, y_test) -> float:
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
    x_test = x_test.astype('float32')
    x_test /= 255
    print('Number of images in x_test', x_test.shape[0])
    score = model.evaluate(x_test, y_test)
    return score[1]


def load_model(dir: str):
    with open(os.path.join(dir, 'model.json'), 'r') as model_json:
        loaded_model = model_from_json(model_json.read())
    loaded_model.load_weights(os.path.join(dir, "weights.h5"))
    compile_model(loaded_model)
    return loaded_model


def main(argv: List[str]):
    assert len(argv) == 1, "only model directory must be specified in arguments"
    _, (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    print(f'accuracy = {evaluate(load_model(argv[0]), x_test, y_test)}')


if __name__ == '__main__':
    main(sys.argv[1:])
