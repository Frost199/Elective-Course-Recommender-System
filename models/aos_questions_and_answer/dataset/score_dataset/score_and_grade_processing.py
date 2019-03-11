import pandas as pd
import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import ListedColormap, BoundaryNorm
import matplotlib.patches as mpatches
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.utils import column_or_1d

dataset = pd.read_csv('score_and_grade.csv')
bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
dataset["Grade Bins"] = pd.cut(dataset['Score'], bins=bins)

x = dataset.iloc[:, :1].values
grade = dataset.iloc[:, 1].values
y = dataset.iloc[:, 2].values

# Encoding our categorical variables for Y
label_encoding_Y = LabelEncoder()
y = column_or_1d(y, warn=True)
y = label_encoding_Y.fit_transform(y)
grade = label_encoding_Y.fit_transform(grade)

# splitting the dataset into a training set and a test set
# here we are using 100 observation which is 100/400 = 0.25, so test_size=0.25
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

# splitting the dataset into a training set and a test set
# here we are using 100 observation which is 100/400 = 0.25, so test_size=0.25
x_train, x_test, grade_train, grade_test = train_test_split(x, grade, test_size=0.25, random_state=0)

# feature scaling
sc_X = StandardScaler()
scaler_x = sc_X.fit(x_train)
x_train = scaler_x.transform(x_train)
x_test = scaler_x.transform(x_test)

result = []
result_grade = []

# fitting the classifier to the training set
for i in range(1, 101):
    classifier = KNeighborsClassifier(n_neighbors=i, algorithm='auto', metric='minkowski', p=2)
    classifier.fit(x_train, y_train)

    # predicting the Test set resulrt
    y_pred = classifier.predict(x_test)

    # making the confusion matrix to test performance of our logistic_regression
    cm = confusion_matrix(y_test, y_pred)
    # Acuuracy Score
    acc = accuracy_score(y_test, y_pred)
    result.append("for k = {}, accuracy % is: {}".format(i, acc * 100))

# fitting the classifier to the training set
for i in range(1, 101):
    classifier_grade = KNeighborsClassifier(n_neighbors=i, algorithm='auto', metric='minkowski', p=2)
    classifier_grade.fit(x_train, grade_train)

    # predicting the Test set resulrt
    grade_pred = classifier.predict(x_test)

    # making the confusion matrix to test performance of our logistic_regression
    cm_grade = confusion_matrix(grade_test, grade_pred)
    # Acuuracy Score
    acc_grade = accuracy_score(grade_test, grade_pred)
    result_grade.append("for k = {}, accuracy % is: {}".format(i, acc * 100))

# fitting the classifier to the training set
classifier = KNeighborsClassifier(n_neighbors=5, algorithm='auto', metric='minkowski', p=2)
classifier.fit(x_train, y_train)

# fitting the classifier to the training set
classifier_grade = KNeighborsClassifier(n_neighbors=5, algorithm='auto', metric='minkowski', p=2)
classifier_grade.fit(x_train, grade_train)

# joblib.dump(classifier, "cgpa_prediction")
y_pred = classifier.predict(x_test)
grade_pred = classifier_grade.predict(x_test)

# making the confusion matrix to test performance of our logistic_regression
cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
# making the confusion matrix to test performance of our logistic_regression
cm_grade = confusion_matrix(grade_test, grade_pred)
acc_grade = accuracy_score(grade_test, grade_pred)

# performance = (int(cm[0, 0]) + int(cm[1, 1]) + int(cm[2, 2]) + int(cm[3, 3])) / len(y_test)

# performance  = performance * 100

new_input_value = [65]
new_input = np.array(new_input_value)
new_input = new_input.reshape(-1, 1)

scaled_input = scaler_x.transform(new_input)
new_prediction = classifier.predict(scaled_input)
new_prediction_grade = classifier_grade.predict(scaled_input)
score_grade_letter = ""

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

if new_prediction_grade == 0:
    score_grade_letter += "A"
elif new_prediction_grade == 1:
    score_grade_letter = "B"
elif new_prediction_grade == 2:
    score_grade_letter = "C"
elif new_prediction_grade == 3:
    score_grade_letter = "D"

student_mark.append(new_input_value[0])
student_mark.append(new_prediction)
student_mark.append(score_grade_letter)


def plot_regions(x_val, y_val):
    x_matrix = x_val.as_matrix()
    y_matrix = y_val.as_matrix()

    # create color maps
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF', '#AFAFAF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF', '#AFAFAF'])

    # plot the decision boundary by assigning a color in the colormap to each mesh point
    mesh_step_size = 0.1 # stepsize in the mesh
    plot_symbol_size = 50
    x_min, x_max = x_matrix[:, 0].min() - 1, x_matrix[:, 0].max() + 1
    y_min, y_max = x_matrix[:, 1].min() - 1, x_matrix[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, mesh_step_size))
    np.arange(y_min, y_max, mesh_step_size)
    z = classifier_grade.predict(np.c_[xx.ravel(), yy.ravel()])
    # put the result into a color plot
    z = z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, z, cmap=cmap_light)

    # Plot training points
    plt.scatter(x_matrix[:, 0], x_matrix[:, 1], s=plot_symbol_size, c=y_val, cmap=cmap_bold, edgecolor='black')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    # patches
    patch_0 = mpatches.Patch(color='#FF0000', label='A')
    patch_1 = mpatches.Patch(color='#00FF00', label='B')
    patch_2 = mpatches.Patch(color='#0000FF', label='C')
    patch_3 = mpatches.Patch(color='#AFAFAF', label='F')
    plt.legend(handles=[patch_0, patch_1, patch_2, patch_3])


