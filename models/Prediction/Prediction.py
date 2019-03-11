import numpy as np


# New Prediction
from models.Prediction.Training import KnnTraining


def predict_grade_range(scores, saved_model):
    returned_grades = list()
    student_mark = []
    model_year = KnnTraining()
    new_input_value = [scores]
    new_input = np.array(new_input_value)
    new_input = new_input.reshape(-1, 1)
    model_year.load_dataset()
    model_year.encode_variables_for_y(model_year.Y)
    model_year.spliting_to_training_and_test_set_no_return(model_year.X, model_year.Y)
    scaled_input = model_year.feature_scaling(new_input)
    new_prediction = saved_model.predict(scaled_input)
    if new_prediction == 0:
        new_prediction = '(0, 5]'
    elif new_prediction == 1:
        new_prediction = '(10, 15]'
    elif new_prediction == 2:
        new_prediction = '(15, 20]'
    elif new_prediction == 3:
        new_prediction = '(20, 25]'
    elif new_prediction == 4:
        new_prediction = '(25, 30]'
    elif new_prediction == 5:
        new_prediction = '(30, 35]'
    elif new_prediction == 6:
        new_prediction = '(35, 40]'
    elif new_prediction == 7:
        new_prediction = '(40, 45]'
    elif new_prediction == 8:
        new_prediction = '(45, 50]'
    elif new_prediction == 9:
        new_prediction = '(5, 10]'
    elif new_prediction == 10:
        new_prediction = '(50, 55]'
    elif new_prediction == 11:
        new_prediction = '(55, 60]'
    elif new_prediction == 12:
        new_prediction = '(60, 65]'
    elif new_prediction == 13:
        new_prediction = '(65, 70]'
    elif new_prediction == 14:
        new_prediction = '(70, 75]'
    elif new_prediction == 15:
        new_prediction = '(75, 80]'
    elif new_prediction == 16:
        new_prediction = '(80, 85]'
    elif new_prediction == 17:
        new_prediction = '(85, 90]'
    elif new_prediction == 18:
        new_prediction = '(90, 95]'
    elif new_prediction == 19:
        new_prediction = '(95, 100]'

    student_mark.append(new_input_value[0])
    student_mark.append(new_prediction)
    returned_grades.append(student_mark)
    return returned_grades
