# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
**Name** Census Income
**Model Type** ~Random Forest~ Selected this as it has a high accurracy, and provides a reduction in overfitting,  This is a supervised model with binary classification.
**Framework** scikit-learn was used for model training and OneHotEncoder
**Tasks** This will try to predict wether a person income is more than 50,000 a year.

## Intended Use
**Intended Use** D501 school use and informal informational purposes.
**Purpose** Estimate income category for individuals

## Training Data
**Data** ~census.csv~
**label** salary 
**Train/Test split** 80/20
**Random State** 42
**Features Used** *"workclass", "education, "marital-status","occupation","relationship","race","sex","native-country"*

## Evaluation Data
**Method** trained on random data, evaluated on test data, Used the F1 Score, Precision and recall.
**Slice** used to help detect lower performance or a bias on groups and subgroups.

## Metrics
Precision: 0.7450 | Recall: 0.6397 | F1: 0.6884

## Ethical Considerations
**Privacy** No  PII (personal identifiable information), minimal risk of not being compliant to data regulations
**Risks and harms** data may contain biases, which could 

## Caveats and Recommendations
**Improve Model** increase dataset and training and testing size
**Improve Data** more timely data, increased features, improve labeling.
**Data Warnings** Model may not work without futher adaptation, using outside data, or more recent data, data might also be underepresented in some sub groups
