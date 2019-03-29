# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 10:02:23 2018

@author: Eleam Emmanuel
"""

# Decision Trees
import pandas as pd
import matplotlib

matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, precision_score, recall_score, \
    classification_report
from mlxtend.plotting import plot_decision_regions
from sklearn.utils import column_or_1d
from sklearn.externals import joblib

# importing the dataset
dataset = pd.read_csv('./models/Prediction/dataset/score_and_grade.csv')
bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
dataset["Grade Bins"] = pd.cut(dataset['Score'], bins=bins)

x = dataset.iloc[:, :1].values
y = dataset.iloc[:, 2].values

# Encoding our categorical variables for Y
label_encoding_Y = LabelEncoder()
y = column_or_1d(y, warn=True)
y = label_encoding_Y.fit_transform(y)

# splitting the dataset into a training set and a test set
# here we are using 100 observation which is 100/400 = 0.25, so test_size=0.25
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

# feature scaling
sc_X = StandardScaler()
scaler_x = sc_X.fit(x_train)
x_train = scaler_x.transform(x_train)
x_test = scaler_x.transform(x_test)

# fitting the Decision Tree classifier to the training set
classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
classifier.fit(x_train, y_train)

joblib.dump(classifier, "mark_category")
# predicting the Test set resulrt
y_pred = classifier.predict(x_test)

# Acuuracy Score
accuracy = accuracy_score(y_test, y_pred)

result = classifier.score(x_test, y_test)
result = "Accuracy: %.3f%%" % (result * 100.0)
# making the confusion matrix to test performance of our logistic_regression
cm = confusion_matrix(y_test, y_pred, labels=classifier.classes_)

# F1 Score
f1_score_value = f1_score(y_test, y_pred, average="macro")

# precision
precision_score_value = precision_score(y_test, y_pred, average="macro")

# Recall
recall_score_value = recall_score(y_test, y_pred, average="macro")


def cm_analysis(y_true, y_pred, labels, filename, given_figsize):
    """
    Generate matrix plot of confusion matrix with pretty annotations.
    The plot image is saved to disk.
    args:
      y_true:    true label of the data, with shape (nsamples,)
      y_pred:    prediction of the data, with shape (nsamples,)
      filename:  filename of figure file to save
      labels:    string array, name the order of class labels in the confusion matrix.
                 use `clf.classes_` if using scikit-learn models.
                 with shape (nclass,).
      ymap:      dict: any -> string, length == nclass.
                 if not None, map the labels & ys to more understandable strings.
                 Caution: original y_true, y_pred and labels must align.
      figsize:   the size of the figure plotted.
    """
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    plt.figure(figsize=given_figsize)
    sns.heatmap(cm, annot=True)
    plt.title('Confusion Matrix for Decision Trees Classifiers (TEST SET) Model')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.savefig(filename)
    plt.show()


cm_analysis(y_test, y_pred, classifier.classes_, 'Confusion Matrix decision_trees_test.png', given_figsize=(19, 19))

# Visualizing the training set results
ax = plot_decision_regions(x_train, y_train, clf=classifier, legend=2)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, ['[0-5]', '[10-15]', '[15-20]', '[20-25]', '[25-30]',
                    '[30-35]', '[35-40]', '[40-45]', '[45-50]', '[5-10]',
                    '[50-55]', '[55-60]', '[60-65]', '[65-70]', '[70-75]',
                    '[75-80]', '[80-85]', '[85-90]', '[90-95]', '[95-100]'],
          framealpha=0.3, scatterpoints=1)
plt.title('Decision Tree (TRAINING SET) Exam Scores and Predicted Score Category')

plt.show()
plt.savefig('decision_tree_train.png')

# Visualizing the test set results
ax = plot_decision_regions(x_test, y_test, clf=classifier, legend=2)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, ['[0-5]', '[10-15]', '[15-20]', '[20-25]', '[25-30]',
                    '[30-35]', '[35-40]', '[40-45]', '[45-50]', '[5-10]',
                    '[50-55]', '[55-60]', '[60-65]', '[65-70]', '[70-75]',
                    '[75-80]', '[80-85]', '[85-90]', '[90-95]', '[95-100]'],
          framealpha=0.3, scatterpoints=1)
plt.title('Decision Tree (TEST SET) Exam Scores and Predicted Score Category')

plt.show()
plt.savefig('decision_tree_test.png')


# New Prediction
def predict_grade_range(list_of_scores):
    returned_grades = list()
    for i in list_of_scores:
        new_input_value = [i]
        new_input = np.array(new_input_value)
        new_input = new_input.reshape(-1, 1)

        scaled_input = scaler_x.transform(new_input)
        new_prediction = classifier.predict(scaled_input)
        student_mark = []
        if new_prediction == 0:
            new_prediction = '[0-5]'
        elif new_prediction == 1:
            new_prediction = '[10-15]'
        elif new_prediction == 2:
            new_prediction = '[15-20]'
        elif new_prediction == 3:
            new_prediction = '[20-25]'
        elif new_prediction == 4:
            new_prediction = '[25-30]'
        elif new_prediction == 5:
            new_prediction = '[30-35]'
        elif new_prediction == 6:
            new_prediction = '[35-40]'
        elif new_prediction == 7:
            new_prediction = '[40-45]'
        elif new_prediction == 8:
            new_prediction = '[45-50]'
        elif new_prediction == 9:
            new_prediction = '[5-10]'
        elif new_prediction == 10:
            new_prediction = '[50-55]'
        elif new_prediction == 11:
            new_prediction = '[55-60]'
        elif new_prediction == 12:
            new_prediction = '[60-65]'
        elif new_prediction == 13:
            new_prediction = '[65-70]'
        elif new_prediction == 14:
            new_prediction = '[70-75]'
        elif new_prediction == 15:
            new_prediction = '[75-80]'
        elif new_prediction == 16:
            new_prediction = '[80-85]'
        elif new_prediction == 17:
            new_prediction = '[85-90]'
        elif new_prediction == 18:
            new_prediction = '[90-95]'
        elif new_prediction == 19:
            new_prediction = '[95-100]'

        student_mark.append(new_input_value[0])
        student_mark.append(new_prediction)
        returned_grades.append(student_mark)
    return returned_grades


test_score = [40, 74, 93, 20]
new_grade = predict_grade_range(test_score)
