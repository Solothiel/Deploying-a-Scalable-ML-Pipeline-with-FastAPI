import pytest
# TODO: add necessary import
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import fbeta_score, precision_score, recall_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder, LabelBinarizer
from ml.model import train_model, compute_model_metrics
from ml.data import process_data
import math

@pytest.fixture
def sample_data():
    sample = pd.DataFrame({
        "age": [30,76,25,41,50],
        "workclass": ["Private","Without-pay","Private","State-gov", "Self-emp-not-inc"],
        "education": ["Bachelors", "11th","HS-grad", "Bachelors", "HS-grad"],
        "marital-status":["Divorced", "Married-civ-spouse", "Never-married", "Divorced", "Married-civ-spouse"],
        "occupation":["Tech-support","Armed-Forces", "Transport-moving", "Exec-managerial", "Handlers-cleaners"],
        "relationship": ["Husband","Unmarried", "Wife","Wife", "Not-in-family"],
        "race": ["Black", "White", "White","Black", "BLack"],
        "sex": ["Male", "Male", "Female","Female", "Male"],
        "native-country": ["United-States","United-States", "United-States", "United-States", "United-States"],
        "salary": [0, 1, 0, 1, 1]
	})
    return sample    
                        

# TODO: implement the first test. Change the function name and input as needed
def test_data_split(sample_data):
    """
    Checks to see if the data is split into training and testing sets and the sets are not empty.
    """

    train,test = train_test_split(sample_data, test_size=0.2, random_state=42)

    assert not train.empty, "Training dataset is empty."
    assert not test.empty, "Test dataset is empty."
    assert math.isclose(len(test) / len(sample_data), 0.2, rel_tol=0.01), f"Test dataset to precision: {len(test) / len(sample_data):.4f}"


# TODO: implement the second test. Change the function name and input as needed
def test_train_and_inference(sample_data):
    """
    Checks the number of rows and features match the dataset
     and that the correct encoders returned.
    """
    cat_features = [
        "workclass", "education", "marital-status", "occupation",
        "relationship", "race", "sex", "native-country"
    ]

    X, y, encoder, lb = process_data(
        sample_data,
        categorical_features=cat_features,
        label="salary",
        training=True
    )

    # Normal assertions
    assert X.shape[0] == sample_data.shape[0]
    assert len(y) == sample_data.shape[0]
    assert isinstance(encoder, OneHotEncoder)
    assert isinstance(lb, LabelBinarizer)

    


# TODO: implement the third test. Change the function name and input as needed
def test_data_shape(sample_data):
    """
    # Testing the shape of the data
    """
    assert sample_data.shape == (5, 10)
    
