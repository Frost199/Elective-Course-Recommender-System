# Importing required modules

import pandas as pd
from models.aos_questions_and_answer.dataset.elective_courses_questions.computer_networks \
    .procesing_cn_elective_courses import \
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
cn_total_questions = 0

# Reading the CSV file that contains all compiled questions with respective answers
# models/aos_questions_and_answer/dataset/elective_courses_questions/computer_networks
# /cn_elective_courses_questions.csv
dataset = pd.read_csv(
    'models/aos_questions_and_answer/dataset/elective_courses_questions/computer_networks'
    '/cn_elective_courses_questions.csv')

# COS845
cos_845_questions = dataset.iloc[1:, :1].values
cos_845_answers = dataset.iloc[1:, 1].values
cos_845_list_of_dictionaries_of_questions_and_answers = Util.processed_list_dict(cos_845_questions, cos_845_answers)
cos_845_selected_six_random = Util.select_six_random(cos_845_list_of_dictionaries_of_questions_and_answers)

# COS829
cos_829_questions = dataset.iloc[1:, 2:3].values
cos_829_answers = dataset.iloc[1:, 3].values
cos_829_list_of_dictionaries_of_questions_and_answers = \
    Util.processed_list_dict(cos_829_questions, cos_829_answers)
cos_829_selected_six_random = Util.select_six_random(cos_829_list_of_dictionaries_of_questions_and_answers)

# COS852
cos_852_questions = dataset.iloc[1:, 4:5].values
cos_852_answers = dataset.iloc[1:, 5].values
cos_852_list_of_dictionaries_of_questions_and_answers = \
    Util.processed_list_dict(cos_852_questions, cos_852_answers)
cos_852_selected_six_random = Util.select_six_random(cos_852_list_of_dictionaries_of_questions_and_answers)

# COS850
cos_850_questions = dataset.iloc[1:, 6:7].values
cos_850_answers = dataset.iloc[1:, 7].values
cos_850_list_of_dictionaries_of_questions_and_answers = \
    Util.processed_list_dict(cos_850_questions, cos_850_answers)
cos_850_selected_six_random = Util.select_six_random(cos_850_list_of_dictionaries_of_questions_and_answers)

# Getting total questions and answers to be asked for ever user
cn_total_questions_and_answer = Util.all_selected_questions_with_answers(cos_845_selected_six_random,
                                                                         cos_829_selected_six_random,
                                                                         cos_852_selected_six_random,
                                                                         cos_850_selected_six_random)
# print(total_questions_and_answer)
for i in cn_total_questions_and_answer.values():
    for j in i:
        cn_total_questions += 1
