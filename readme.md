Phone numbers in India are a set of unique 10 digit numbers. Out of which, first 4 are network operator/circle code. These prefixes range from 6xxx - 9xxx. Last six are random. This is a dataset, charts, model of first four numbers with their respective circle, operator name.

Note: This dataset is provided "as-is" without any warranty of any kind. While I have personally fixed many errors, I still can't guarantee that this dataset is accurate. Use at your own risk.


## Use Cases

- Privacy friendly alternative to reverse phone number lookup services like Truecaller

See the section below for pretrained models, training and inference script.

- Model training

- Spam Detection


## Using Machine Learning To Predict Operator Names

A Python script named, `predict-operator.py` is provided with this project. It works by checking if the operator to predict is in dataset. If not, it will try using the appropriate model for predicting the operator. If appropriate model is not found, it will train the model using Gradient Boosting Classifer(GBC), save it, and predict using newly trained model.

Pretrained models are provided in releases section. If you want, you can train your own by running `python train_save_all.py`

### Examples

``` 
$ python predict-operator.py ../data/6xxx-in-mob-prefix.csv 7000 ../models/6xxx-gbc.bin

Predicted Operator: 
['RJ']

```

```
$ python predict-operator.py ../data/9xxx-in-mob-prefix.csv 9000 ../models/9xxx-gbc.bin

Operator Found in Database
['AT']

```

 
## Sources

Majority of this data is sourced from Wikipedia, Department of Telecom(DoT) and Telecom Regulatory Authority of India(TRAI). Rest of it was collected from various sources including web scrapping, personal research.

The metro circles which have been [merged into their respective states](https://www.thehindu.com/business/Industry/DoT-to-merge-Mumbai-Kolkata-telecom-circles-with-Maharashtra-Bengal/article60087718.ece) were updated. Then the rows which have both columns empty were dropped using the script provided in src/scripts folder. 

The dataset contains missing values, because I want to be accurate, and this data is hard to find. If I wanted, I could fill the data with a single function call `df.fillna()`, but I did not.
