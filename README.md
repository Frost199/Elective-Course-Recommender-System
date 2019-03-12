# Elective-Course-Recommender-System
This is a web based elective course recommender system implemented with flask and Sklearn

The Project is a case study for the **Department of Computer Science, University of Nigeria Nsukka**. THeis project involves two part,
the first part deals with the selection of Area of Specialization for a Masters student, this is done by asking series of questions and then a ranking
system is used to generate an area of specializtion from the persons score. 

## Clustering 
This is done to analyse the previous records of students in the selected area of specialization and a pie chart is shown to the user
to give a detailed anaysis of the rate of failure to success in the area of specializtion selected.

**Below is a screenshot of a course clustered of past sudents record for a compulsory course in an Area of sepcialization.
The cluster shows the performance of students in their test to exam scores.**

![clustered_example](https://user-images.githubusercontent.com/25561713/54163668-013c8680-445a-11e9-8caa-b664ad78d1b9.png)

## Model Selection
The second part of the project has to do with the Selection of elective courses in the preferred area of specialization.
Here, the data is binned and the courses are ranked based on the model __decision trees__ which was evaluated and then the top four courses are
selected.

The models used for training are:
* Decision Trees
* Support Vector Machine (Linear and Kernel)
* K-Nearest Neighbour
* Naïve Bayes
* Logistic Regression

## Evaluation Metrics
This is a way of evaluating our models for the best model to be used for our predictions, A basic confusion matrix is shown below

|   |   | Predicted Class |   |
| - | - | --------------- | - |
|   |   | **Class 1** | **Class 0**
**Actual Class** | **Class 1** | _True Positive (TP)_ | _False Negative (FN)_
|   | **class 0** | *False Positive (FP)* | _True Negative (TN)_


For this project this is the Confusion matrix below
![confusion_matrix](https://user-images.githubusercontent.com/25561713/54164625-9725e080-445d-11e9-8edf-1f4395ea2629.png)


## Accuracy
<img src="http://bit.ly/2Cb1p0r" align="center" border="0" alt=" \frac{True Positive + True Negative}{ Total Points} " width="256" height="43" />

## Precision
<img src="http://www.sciweavers.org/tex2img.php?eq=%20%5Cfrac%7BTrue%20Positive%7D%7B%20True%20Positive%20%2B%20False%20Positive%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt=" \frac{True Positive}{ True Positive + False Positive} " width="250" height="44" />

## Recall
<img src="http://www.sciweavers.org/tex2img.php?eq=%20%5Cfrac%7BTrue%20Positive%7D%7B%20True%20Positive%20%2B%20False%20Negative%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt=" \frac{True Positive}{ True Positive + False Negative} " width="261" height="47" />

## F1 Score
<img src="http://bit.ly/2SUZLWx" align="center" border="0" alt=" 2*\frac{Precision * Recall}{ Precision + Recall}" width="192" height="44" />

### Evaluation Metrics for our project

Evaluation Metrics |   |   | Models |   |   |   |
------------------ | - | - | ------ | - | - | - |
|   | Linear SVM | Kernel SVM | Decison Trees | Logistic Regression | Naïve Bayes | K-Nearest Neighbours
Accuracy | 93.307% | 97.633% | 99.409% | 37.008% | 99.409% | 99.213%
Precision | 93.307% | 97.633% | 99.409% | 37.008% | 99.409% | 99.213%
Recall | 0.741 | 0.783 | 0.912 | 0.147 | 0.912 | 0.906
F1 Score |0.7 | 0.74 | 0.902 | 0.093 | 0.902 | 0.896
