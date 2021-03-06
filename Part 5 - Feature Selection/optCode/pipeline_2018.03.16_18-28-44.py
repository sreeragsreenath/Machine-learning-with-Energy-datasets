import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=42)

# Score on the training set was:-5358.917200314865
exported_pipeline = GradientBoostingRegressor(alpha=0.95, learning_rate=0.1, loss="huber", max_depth=10, max_features=0.7500000000000001, min_samples_leaf=5, min_samples_split=11, n_estimators=300, subsample=0.2)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
