# Predicting insurance cross-sales with ML
This project uses machine learning to predict whether a current health insurance customer will buy car insurance or not.<br><br>
The underlying data was obtained [from Kaggle](https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction), and contains information on previous sales. The data was transformed and upsampled using SMOTENC prior to testing various classifiers, including logistic regression, support vector classifiers, KNN classifiers and random forest classifiers.<br><br>
After testing classifiers with their default hyperparameters, a grid search was performed to identify the optimal combination of hyperparameters.
