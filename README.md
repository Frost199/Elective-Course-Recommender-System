# Elective-Course-Recommender-System
This is a web based elective course recommender system implemented with flask and Sklearn

The Project is a case study for the **Department of Computer science, University of Nigeria Nsukka**. THeis project involves two part,
the first part deals with the selection of Area of Specialization for a Masters student, this is done by asking series of questions and then a ranking
system is used to generate an area of specializtion from the persons score. 

## Clustering 
This is done to analyse the previous records of students in the selected area of specialization and a pie chart is shown to the user
to give a detailed anaysis of the rate of failure to success in the area of specializtion selected.

## Model Selection
The second part of the project has to do with the Selection of elective courses in the preferred area of specialization.
Here, the data is binned and the courses are ranked based on the model __decision trees__ which was evaluated and then the top four courses are
selected.

The models used for training are:
* Decision Trees
* Support Vector Machine (Linear and Kernel)
* K-Nearest Neighbour
* Naive Bayes
