from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

import pandas as pd

def createModel():
    data_path = "data.csv"
    data = pd.read_csv(data_path)

    y = data.open
    data_features = ['timestamp', 'high', 'low', 'close', 'adjusted close', 'volume', 'dividend amount', 'symbol']
    X = data[data_features]
    print(X)
    coded_X = X.copy()
    enc = OrdinalEncoder(handle_unknown='error')
    coded_X = enc.fit_transform(X)
    print(coded_X)

    coded_X_train, coded_X_valid, y_train, y_valid = train_test_split(coded_X, y, random_state = 0)

    model = XGBRegressor()
    model.fit(coded_X_train, y_train)

    predictions = model.predict(coded_X_valid)
    print(mean_absolute_error(y_valid, predictions))

createModel()