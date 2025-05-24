# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model uses the ensemble method Random Forest (RandomForestClassifier) with the random state
value set to one (random_state=1) to predict whether a person makes >50K a year. In order for the
model to make this prediction, it has been trained on census income data from the UCI Machine 
Learning Repository.
## Intended Use
The intended use of this model is to predict whether a person makes >50K a year based on specific 
demographics within the census data. In addition, the model is used to investigate how machine 
learning models perform differently with different data slices that highlight specific demographic
data values.

## Training Data
Training data consist of 80% of the census income data acquired from the UCI Machine Learning
Repository. The whole census income dataset contains 48,842 instances that represents people who 
have made >50K and <=50K, with their respective demographics. 
## Evaluation Data
Evaluation data, also known as test data, consist of 20% of the census income data from the UCI
Machine Learning Repository. Therefore, 20% of the total census income dataset that contains 48,842 
instances was used to evaluate the model and gather model metrics.
## Metrics
_Please include the metrics used and your model's performance on those metrics._
The reported metrics of the model include:
Precision: 0.7419, Recall: 0.6103, F1: 0.6697
## Ethical Considerations
This model only uses 14 demographic features to make a prediction on whether a person makes >50K.
However, there are many more features that could define a person and determine whether they could 
make >50k. Considering more features could also expose specific class imbalances within the current 
model, due to it only using 14 features to describe a person's income level. 
## Caveats and Recommendations
This model was built using census data from 1994, therefore the model may not be effective on modern
day data. To learn more about the census income dataset from the UCI Machine Learning Repository,
visit the link (https://archive.ics.uci.edu/dataset/20/census+income).