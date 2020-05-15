import sys
from typing import List

import tensorflow as tf

from common import load_model


def evaluate(model, x_test, y_test) -> float:
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
    x_test = x_test.astype('float32')
    x_test /= 255
    print('Number of images in x_test', x_test.shape[0])
    score = model.evaluate(x_test, y_test)
    return score[1]



def main(argv: List[str]):
    assert len(argv) == 1, "only model directory must be specified in arguments"
    _, (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    print(f'accuracy = {evaluate(load_model(argv[0]), x_test, y_test)}')


if __name__ == '__main__':
    main(sys.argv[1:])
