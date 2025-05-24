import pytest
# TODO: add necessary import
import os

import pandas as pd
from sklearn.model_selection import train_test_split

from ml.data import process_data
from ml.model import (
    compute_model_metrics,
    inference,
    load_model,
    performance_on_categorical_slice,
    save_model,
    train_model,
)

project_path = os.getcwd()
data_path = os.path.join(project_path, "data", "census.csv")
data = pd.read_csv(data_path)

train, test = train_test_split(data, test_size = 0.2, random_state = 1, stratify = data['salary'])

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

X_train, y_train, encoder, lb = process_data(
    # your code here
    # use the train dataset
    # use training=True
    # do not need to pass encoder and lb as input
    train,
    categorical_features = cat_features,
    label = 'salary',
    training = True
    )

X_test, y_test, _, _ = process_data(
    test,
    categorical_features=cat_features,
    label="salary",
    training=False,
    encoder=encoder,
    lb=lb,
)

model = train_model(X_train, y_train)

preds = inference(model, X_test)

p, r, fb = compute_model_metrics(y_test, preds)

# TODO: implement the first test. Change the function name and input as needed
def test_precision():
    """
    # Test if Precision metric is accurate
    """
    # Your code here
    assert(round(p, 4) == 0.7419)


# TODO: implement the second test. Change the function name and input as needed
def test_recall():
    """
    # Test if Recall metric is accurate
    """
    # Your code here
    assert(round(r, 4) == 0.6103)


# TODO: implement the third test. Change the function name and input as needed
def test_f():
    """
    # Test if F1 metric is accurate
    """
    # Your code here
    assert(round(fb, 4) == 0.6697)
