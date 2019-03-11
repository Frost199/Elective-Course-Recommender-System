# Importing required modules

import pandas as pd
from models.aos_questions_and_answer.dataset.elective_courses_questions.artificial_intelligence \
    .procesing_ai_elective_courses import \
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
ai_total_questions = 0

# Reading the CSV file that contains all compiled questions with respective answers
# models/aos_questions_and_answer/dataset/elective_courses_questions/artificial_intelligence
# /ai_elective_courses_questions.csv
dataset = pd.read_csv(
    'models/aos_questions_and_answer/dataset/elective_courses_questions/artificial_intelligence'
    '/ai_elective_courses_questions.csv')

# COS833
cos_833_questions = dataset.iloc[1:, :1].values
cos_833_answers = dataset.iloc[1:, 1].values
cos_833_list_of_dictionaries_of_questions_and_answers = Util.processed_list_dict(cos_833_questions, cos_833_answers)
cos_833_selected_six_random = Util.select_six_random(cos_833_list_of_dictionaries_of_questions_and_answers)

# COS816
cos_816_questions = dataset.iloc[1:, 2:3].values
cos_816_answers = dataset.iloc[1:, 3].values
cos_816_list_of_dictionaries_of_questions_and_answers = \
    Util.processed_list_dict(cos_816_questions, cos_816_answers)
cos_816_selected_six_random = Util.select_six_random(cos_816_list_of_dictionaries_of_questions_and_answers)

# COS830
cos_830_questions = dataset.iloc[1:, 4:5].values
cos_830_answers = dataset.iloc[1:, 5].values
cos_830_list_of_dictionaries_of_questions_and_answers = \
    Util.processed_list_dict(cos_830_questions, cos_830_answers)
cos_830_selected_six_random = Util.select_six_random(cos_830_list_of_dictionaries_of_questions_and_answers)

# COS836
cos_836_questions = dataset.iloc[1:, 6:7].values
cos_836_answers = dataset.iloc[1:, 7].values
cos_836_list_of_dictionaries_of_questions_and_answers = \
    Util.processed_list_dict(cos_836_questions, cos_836_answers)
cos_836_selected_six_random = Util.select_six_random(cos_836_list_of_dictionaries_of_questions_and_answers)

# COS834
cos_838_questions = dataset.iloc[1:, 8:9].values
cos_838_answers = dataset.iloc[1:, 9].values
cos_838_list_of_dictionaries_of_questions_and_answers = \
    Util.processed_list_dict(cos_838_questions, cos_838_answers)
cos_834_selected_six_random = Util.select_six_random(cos_838_list_of_dictionaries_of_questions_and_answers)

# COS838
cos_838_questions = dataset.iloc[1:, 10:11].values
cos_838_answers = dataset.iloc[1:, 11].values
cos_838_list_of_dictionaries_of_questions_and_answers = \
    Util.processed_list_dict(cos_838_questions, cos_838_answers)
cos_838_selected_six_random = Util.select_six_random(cos_838_list_of_dictionaries_of_questions_and_answers)

# Getting total questions and answers to be asked for ever user
ai_total_questions_and_answer = Util.all_selected_questions_with_answers(cos_833_selected_six_random,
                                                                         cos_816_selected_six_random,
                                                                         cos_830_selected_six_random,
                                                                         cos_836_selected_six_random,
                                                                         cos_834_selected_six_random,
                                                                         cos_838_selected_six_random)
# print(total_questions_and_answer)
for i in ai_total_questions_and_answer.values():
    for j in i:
        ai_total_questions += 1
