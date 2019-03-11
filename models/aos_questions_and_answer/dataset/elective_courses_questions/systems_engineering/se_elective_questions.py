# Importing required modules

import pandas as pd
from models.aos_questions_and_answer.dataset.elective_courses_questions.systems_engineering \
    .procesing_se_elective_courses import \
    Util

# Initializing variables
ai_correct = 0
ai_failed = 0
se_correct = 0
se_failed = 0
cn_correct = 0
cn_failed = 0
sye_correct = 0
sye_failed = 0
tc_correct = 0
tc_failed = 0

AI = []
SE = []
CN = []
SYE = []
TC = []
final_scores = []

current_question_number = 0
se_total_questions = 0

# Reading the CSV file that contains all compiled questions with respective answers
# models/aos_questions_and_answer/dataset/elective_courses_questions/systems_engineering
# /se_elective_courses_questions.csv
dataset = pd.read_csv(
    'models/aos_questions_and_answer/dataset/elective_courses_questions/systems_engineering'
    '/se_elective_courses_questions.csv')

# COS815
cos_815_questions = dataset.iloc[1:, :1].values
cos_815_answers = dataset.iloc[1:, 1].values
cos_815_list_of_dictionaries_of_questions_and_answers = Util.processed_list_dict(cos_815_questions, cos_815_answers)
cos_815_selected_six_random = Util.select_six_random(cos_815_list_of_dictionaries_of_questions_and_answers)

# COS823
cos_823_questions = dataset.iloc[1:, 2:3].values
cos_823_answers = dataset.iloc[1:, 3].values
cos_823_list_of_dictionaries_of_questions_and_answers = \
    Util.processed_list_dict(cos_823_questions, cos_823_answers)
cos_823_selected_six_random = Util.select_six_random(cos_823_list_of_dictionaries_of_questions_and_answers)

# COS817
cos_817_questions = dataset.iloc[1:, 4:5].values
cos_817_answers = dataset.iloc[1:, 5].values
cos_817_list_of_dictionaries_of_questions_and_answers = \
    Util.processed_list_dict(cos_817_questions, cos_817_answers)
cos_817_selected_six_random = Util.select_six_random(cos_817_list_of_dictionaries_of_questions_and_answers)

# COS810
cos_810_questions = dataset.iloc[1:, 6:7].values
cos_810_answers = dataset.iloc[1:, 7].values
cos_810_list_of_dictionaries_of_questions_and_answers = \
    Util.processed_list_dict(cos_810_questions, cos_810_answers)
cos_810_selected_six_random = Util.select_six_random(cos_810_list_of_dictionaries_of_questions_and_answers)

# COS812
cos_812_questions = dataset.iloc[1:, 8:9].values
cos_812_answers = dataset.iloc[1:, 9].values
cos_812_list_of_dictionaries_of_questions_and_answers = \
    Util.processed_list_dict(cos_812_questions, cos_812_answers)
cos_812_selected_six_random = Util.select_six_random(cos_812_list_of_dictionaries_of_questions_and_answers)

# Getting total questions and answers to be asked for ever user
se_total_questions_and_answer = Util.all_selected_questions_with_answers(cos_815_selected_six_random,
                                                                         cos_823_selected_six_random,
                                                                         cos_817_selected_six_random,
                                                                         cos_810_selected_six_random,
                                                                         cos_812_selected_six_random)
# print(total_questions_and_answer)
for i in se_total_questions_and_answer.values():
    for j in i:
        se_total_questions += 1
