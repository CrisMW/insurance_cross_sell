# Predicting insurance cross-sell with machine learning
This project uses machine learning to predict whether or not a current health insurance customer will buy car insurance after being contacted with an offer.

The underlying data came [from Kaggle](https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction), and contains information on previous sales. The goal is to maximise profit by:

 * correctly identifying as non-many buyers as possible,
 * while also preserving as many sales as possible.

The data was transformed and upsampled using SMOTENC prior to testing various classifiers, including logistic regression, support vector classifiers, KNN classifiers and random forest classifiers.

After testing classifiers with their default hyperparameters, a grid search was performed to identify the optimal combination of hyperparameters. A voting and stacking classifier were also tested.

Ultimately, a linear support vector classifier (SVC) was chosen. It correctly identifies 52% of leads as non-buyers who should not be contacted. At the same time, the model correctly selects ~98% of the buyers for targetting. If implemented, the model would save between \$52,000-\$130,000 per 100,000 leads, depending on how leads are contacted (mail, e-mail or phone). The impact of the model is shown below:
![Visualizing model impact](model_impact_infographic.png)
