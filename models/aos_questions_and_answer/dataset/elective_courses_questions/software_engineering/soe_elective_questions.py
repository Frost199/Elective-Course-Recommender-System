# Importing required modules

import pandas as pd
from models.aos_questions_and_answer.dataset.elective_courses_questions.software_engineering \
    .procesing_soe_elective_courses import \
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
soe_total_questions = 0

# Reading the CSV file that contains all compiled questions with respective answers
# models/aos_questions_and_answer/dataset/elective_courses_questions/software_engineering
# /soe_elective_courses_questions.csv
dataset = pd.read_csv(
    'models/aos_questions_and_answer/dataset/elective_courses_questions/software_engineering'
    '/soe_elective_courses_questions.csv')

# COS821
cos_821_questions = dataset.iloc[1:, :1].values
cos_821_answers = dataset.iloc[1:, 1].values
cos_821_list_of_dictionaries_of_questions_and_answers = Util.processed_list_dict(cos_821_questions, cos_821_answers)
cos_821_selected_six_random = Util.select_six_random(cos_821_list_of_dictionaries_of_questions_and_answers)

# COS827
cos_827_questions = dataset.iloc[1:, 2:3].values
cos_827_answers = dataset.iloc[1:, 3].values
cos_827_list_of_dictionaries_of_questions_and_answers = \
    Util.processed_list_dict(cos_827_questions, cos_827_answers)
cos_827_selected_six_random = Util.select_six_random(cos_827_list_of_dictionaries_of_questions_and_answers)

# COS814
cos_814_questions = dataset.iloc[1:, 4:5].values
cos_814_answers = dataset.iloc[1:, 5].values
cos_814_list_of_dictionaries_of_questions_and_answers = \
    Util.processed_list_dict(cos_814_questions, cos_814_answers)
cos_814_selected_six_random = Util.select_six_random(cos_814_list_of_dictionaries_of_questions_and_answers)

# COS820
cos_820_questions = dataset.iloc[1:, 6:7].values
cos_820_answers = dataset.iloc[1:, 7].values
cos_820_list_of_dictionaries_of_questions_and_answers = \
    Util.processed_list_dict(cos_820_questions, cos_820_answers)
cos_820_selected_six_random = Util.select_six_random(cos_820_list_of_dictionaries_of_questions_and_answers)

# Getting total questions and answers to be asked for ever user
soe_total_questions_and_answer = Util.all_selected_questions_with_answers(cos_821_selected_six_random,
                                                                          cos_827_selected_six_random,
                                                                          cos_814_selected_six_random,
                                                                          cos_820_selected_six_random)
# print(total_questions_and_answer)
for i in soe_total_questions_and_answer.values():
    for j in i:
        soe_total_questions += 1
