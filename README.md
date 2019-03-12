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

