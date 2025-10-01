from services import fetch_api_data, transform_data, save_data

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
from skopt import BayesSearchCV
from skopt.space import Real, Categorical, Integer
import numpy as np

debug = True

def main():
    if debug:
      data = fetch_api_data(51.2155, 2.927, "2005-09-01", "2025-01-01")
      df = transform_data(data)
      save_data(df, 'oostende')


# X = df.drop(columns=['rain_flag', 'time'])
# y = df['rain_flag']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# estimators = [
#     ('clf', XGBClassifier(random_state=42))
# ]

# pipe = Pipeline(steps=estimators)

# search_space = {
#     'clf__max_depth': Integer(2,8),
#     'clf__learning_rate': Real(0.001, 1.0, prior='log-uniform'),
#     'clf__subsample': Real(0.5, 1.0),
#     'clf__colsample_bytree': Real(0.5, 1.0),
#     'clf__colsample_bylevel': Real(0.5, 1.0),
#     'clf__colsample_bynode' : Real(0.5, 1.0),
#     'clf__reg_alpha': Real(0.0, 10.0),
#     'clf__reg_lambda': Real(0.0, 10.0),
#     'clf__gamma': Real(0.0, 10.0)
# }

# opt = BayesSearchCV(pipe, search_space, cv=3, n_iter=10, scoring='roc_auc', random_state=42)

# opt.fit(X_train, y_train)

# y_pred = opt.predict(X_test)
# predictions = [round(value) for value in y_pred]

# from sklearn.metrics import accuracy_score

# accuracy = accuracy_score(y_test, predictions) 
# print("Accuracy: %.2f%%" % (accuracy * 100.0))

# df = pd.DataFrame(data['daily'])

# df['rain_yesterday'] = df['rain_sum'].shift(1).fillna(0)
# df['temp_3day_avg'] = df['temperature_2m_mean'].rolling(3).mean().bfill()
# df['month'] = pd.to_datetime(df['time']).dt.month
# df['day_of_year'] = pd.to_datetime(df['time']).dt.dayofyear
# df['wind_dir_sin'] = np.sin(np.radians(df['wind_direction_10m_dominant']))
# df['wind_dir_cos'] = np.cos(np.radians(df['wind_direction_10m_dominant']))

# tommorow_df = df.iloc[-1]

# prediction = opt.predict(tommorow_df)

if __name__ == "__main__":
    main()