
# K-Nearest Neighbours (KNN)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib
from sklearn.utils import column_or_1d


class KnnTraining(object):

    def __init__(self):
        self.X = None
        self.Y = None
        self.x_train_variables = None
        self.x_test_variables = None
        self.y_train_variables = None
        self.y_test_variables = None

    def load_dataset(self):
        # importing the dataset
        dataset = pd.read_csv('./models/Prediction/dataset/score_and_grade.csv')
        bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
        dataset["Grade Bins"] = pd.cut(dataset['Score'], bins=bins)
        self.X = dataset.iloc[:, :1].values  # take all the columns but leave the last one(-1)
        self.Y = dataset.iloc[:, 2].values

    def encode_variables_for_y(self, variables_for_y):
        # Encoding our categorical variables for Y
        label_encoding_y = LabelEncoder()
        self.Y = column_or_1d(variables_for_y, warn=True)
        self.Y = label_encoding_y.fit_transform(self.Y)

    def spliting_to_training_and_test_set(self, variables_for_x_to_split, variables_for_y_to_split):
        # splitting the dataset into a training set and a test set
        # here we are using 100 observation which is 100/400 = 0.25, so test_size=0.25
        self.x_train_variables, self.x_test_variables, self.y_train_variables, self.y_test_variables = train_test_split(
            variables_for_x_to_split,
            variables_for_y_to_split,
            test_size=0.20,
            random_state=0)
        return self.x_train_variables, self.x_test_variables, self.y_train_variables, self.y_test_variables

    def spliting_to_training_and_test_set_no_return(self, variables_for_x_to_split, variables_for_y_to_split):
        # Reshaping X as data has a single feature
        variables_for_x_to_split = np.array(variables_for_x_to_split)
        variables_for_x_to_split = variables_for_x_to_split.reshape(-1, 1)
        # splitting the dataset into a training set and a test set
        # here we are using 100 observation which is 100/400 = 0.25, so test_size=0.25
        self.x_train_variables, self.x_test_variables, self.y_train_variables, self.y_test_variables = train_test_split(
            variables_for_x_to_split,
            variables_for_y_to_split,
            test_size=0.20,
            random_state=0)

    def feature_scaling(self, x_test_to_scale):
        # feature scaling
        sc_x = StandardScaler()
        sc_x.fit_transform(self.x_train_variables)
        x_test_scaled = sc_x.transform(x_test_to_scale)
        return x_test_scaled

    def inverse_feature_scaling(self, x_test_scale_to_invert):
        # feature scaling
        sc_x = StandardScaler()
        scale_x = sc_x.fit(self.x_train_variables)
        scale_x.transform(self.x_train_variables)
        inverted_scale = scale_x.inverse_transform(x_test_scale_to_invert)

        return inverted_scale

    @staticmethod
    def training(scaled_x_train, y_train_variables):
        # fitting the classifier to the training set
        classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
        classifier.fit(scaled_x_train, y_train_variables)
        joblib.dump(classifier, "./saved_model/mark_category")
        return classifier
