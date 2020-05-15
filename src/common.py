import os

from tensorflow.python.keras.models import model_from_json


def compile_model(model):
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])


def load_model(dir: str):
    with open(os.path.join(dir, 'model.json'), 'r') as model_json:
        loaded_model = model_from_json(model_json.read())
    loaded_model.load_weights(os.path.join(dir, "weights.h5"))
    compile_model(loaded_model)
    return loaded_model
