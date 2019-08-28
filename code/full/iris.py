# ===============================================================
# Author: Rodolfo Ferro
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro,
# for his workshop at RIIAA 2.0. Any explicit usage of
# this script or its contents is granted according to
# the license provided and its conditions.
# ===============================================================

# -*- coding: utf-8 -*-

from tensorflow.keras.models import model_from_json
import numpy as np


def iris_classifier(verbose=True):
    """Iris classifier trained model loader."""

    # Load json and create model:
    json_file = open('../data/iris_model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # Load weights into loaded model:
    loaded_model.load_weights("../data/iris_model.h5")
    
    if verbose:
        print("[INFO] Model loaded from disk.")
    
    # Evaluate loaded model on test data:
    loaded_model.compile(loss='categorical_crossentropy',
                         optimizer='adam',
                         metrics=['accuracy'])
    return loaded_model


if __name__ == '__main__':
    model = iris_classifier()
    r = model.predict(np.array([[5.1, 3.5, 1.4, 0.2]]))
    print(r)
    print(np.argmax(r))
