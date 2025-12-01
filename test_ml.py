import pytest
# TODO: add necessary import
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

@pytest.fixture
def sample_data():
    data = pd.DataFrame({
        "age": [30,76,25],
        "workclass": ["Private","Without-pay","Private"],
        "education": ["Bachelors", "11th","HS-grad"],
        "marital-status":["Divorced", "Married-civ-spouse", "Never-married"],
        "occupation":["Tech-support","Armed-Forces", "Transport-moving"],
        "relationship": ["Husband","Unmarried", "Wife"],
        "race": ["Black", "White", "White"],
        "sex": ["Male", "Male", "Female"],
        "native-country": ["United-States","United-States", "United-States"],
        "salary": ["<=50K", ">50K", "<=50K"]
    })
                        

# TODO: implement the first test. Change the function name and input as needed
def test_one(sample_data):
    """
    
    """
    cat_features = [
        "workclass", "education", "martial-status", "occupation",
        "relationship", "race", "sex", "native-counrty"
    ]

    X, y, encoder, lb =process_data(
        sample_data,
        categorical_features=cat_features,
        label="salary",
        training=True
    )

    assert X.shape[0] ==sample_data.shape[0]
    assert len(y) ==sample_data.shape[0]
    assert isinstance(encoder, OneHotEncoder)
    assert isinstance(lb, LabelBinarizer)
    


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # add description for the second test
    """
    # Your code here
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    """
    # Your code here
    pass
