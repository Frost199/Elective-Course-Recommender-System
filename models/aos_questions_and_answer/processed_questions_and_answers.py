# Importing required modules
import random

import pandas as pd
from models.aos_questions_and_answer.processedlistofdictionaries import Util

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
total_questions = 0

# Reading the CSV file that contains all compiled questions with respective answers
dataset = pd.read_csv('models/aos_questions_and_answer/dataset/core_courses.csv')

# AI Data processing
ai_questions = dataset.iloc[:, :1].values
ai_answers = dataset.iloc[:, 1].values
ai_list_of_dictionaries_of_questions_and_answers = Util.processed_list_dict(ai_questions, ai_answers)
ai_selected_six_random = Util.select_six_random(ai_list_of_dictionaries_of_questions_and_answers)

# Software Engineering Data processing
software_engineering_questions = dataset.iloc[:, 2:3].values
software_engineering_answers = dataset.iloc[:, 3].values
software_engineering_list_of_dictionaries_of_questions_and_answers = \
    Util.processed_list_dict(software_engineering_questions, software_engineering_answers)
se_selected_six_random = Util.select_six_random(software_engineering_list_of_dictionaries_of_questions_and_answers)

# Computer Networks Data processing
computer_networks_questions = dataset.iloc[:, 4:5].values
computer_networks_answers = dataset.iloc[:, 5].values
computer_networks_list_of_dictionaries_of_questions_and_answers =\
    Util.processed_list_dict(computer_networks_questions, computer_networks_answers)
cn_selected_six_random = Util.select_six_random(computer_networks_list_of_dictionaries_of_questions_and_answers)

# Systems Engineering Data processing
systems_engineering_questions = dataset.iloc[:, 6:7].values
systems_engineering_answers = dataset.iloc[:, 7].values
systems_engineering_list_of_dictionaries_of_questions_and_answers = \
    Util.processed_list_dict(systems_engineering_questions, systems_engineering_answers)
sye_selected_six_random = Util.select_six_random(systems_engineering_list_of_dictionaries_of_questions_and_answers)

# Theoretical Computing Data processing
theoretical_computing_questions = dataset.iloc[:, 8:9].values
theoretical_computing_answers = dataset.iloc[:, 9].values
theoretical_computing_list_of_dictionaries_of_questions_and_answers = \
    Util.processed_list_dict(theoretical_computing_questions, theoretical_computing_answers)
tc_selected_six_random = Util.select_six_random(theoretical_computing_list_of_dictionaries_of_questions_and_answers)

# Getting total questions and answers to be asked for ever user
total_questions_and_answer = Util.all_selected_questions_with_answers(ai_selected_six_random,
                                                                      se_selected_six_random,
                                                                      cn_selected_six_random,
                                                                      sye_selected_six_random,
                                                                      tc_selected_six_random)

# print(total_questions_and_answer)
for i in total_questions_and_answer.values():
    for j in i:
        total_questions += 1
    # total_questions = len(total_questions_and_answer) - len(total_questions_and_answer.values())
# print(total_questions)
# print(total_questions_and_answer['1'])
# print(total_questions_and_answer['1'][0])


# def output_question():
#     for one_quest in total_questions_and_answer['1']:
#         question_to_ask = ''
#         a = ""
#         b = ""
#         c = ""
#         question_tuple = tuple(one_quest.items())
#         # print(question_tuple)
#         for question_posted in question_tuple:
#             questions, answers = question_posted
#             questions = questions.split()
#             question_to_ask = " ".join(questions[:questions.index('(A)')])
#             mango = questions[questions.index('(A)'):]
#             a = " ".join(mango[:mango.index('(B)')])
#             b = " ".join(mango[mango.index('(B)'):mango.index('(C)')])
#             c = " ".join(mango[mango.index('(C)'):])
#             print(question_to_ask)
#             print(a)
#             print(b)
#             print(c)
#             # return question_to_ask, a, b, c


# output_question()

# ques, opt_1, opt_2, opt_3, = output_question()
# print(ques)
# print(opt_1)
# print(opt_2)
# print(opt_3)

#
# for i in range(5):
#     output_question()
#     ques, opt_1, opt_2, opt_3, = output_question()
#     print(ques)
#     print(opt_1)
#     print(opt_2)
#     print(opt_3)
        # print(questions[questions.index('(A)'):])
        # print(" ".join(questions[questions.index('(A)'):]))
        # print(questions, answers)

#######################################################################################


# for m, i in enumerate(total_questions_and_answer):
#     random.shuffle(i, random.random)
#     for j, k in enumerate(i):

#         question_tuple = tuple(k.items())
#         for question_posted in question_tuple:
#             questions, answers = question_posted
#             if k == ai_selected_six_random[m]:
#                 current_question_number += 1
#                 print(f"Question {current_question_number}/{total_questions}\n")
#                 print(questions)
#                 y = input("Select your answer: \n")
#                 # y == k.getitem() ? correct+=1 : failed+=1
#                 if y == answers:
#                     ai_correct += 1
#                 else:
#                     ai_failed += 1
#             elif k == se_selected_six_random[m]:
#                 current_question_number += 1
#                 print(f"Question {current_question_number}/{total_questions}\n")
#                 print(questions)
#                 y = input("Select your answer: \n")
#                 # y == k.getitem() ? correct+=1 : failed+=1
#                 if y == answers:
#                     se_correct += 1
#                 else:
#                     se_failed += 1
#             elif k == cn_selected_six_random[m]:
#                 current_question_number += 1
#                 print(f"Question {current_question_number}/{total_questions}\n")
#                 print(questions)
#                 y = input("Select your answer: \n")
#                 # y == k.getitem() ? correct+=1 : failed+=1
#                 if y == answers:
#                     cn_correct += 1
#                 else:
#                     cn_failed += 1
#             elif k == sye_selected_six_random[m]:
#                 current_question_number += 1
#                 print(f"Question {current_question_number}/{total_questions}\n")
#                 print(questions)
#                 y = input("Select your answer: \n")
#                 # y == k.getitem() ? correct+=1 : failed+=1
#                 if y == answers:
#                     sye_correct += 1
#                 else:
#                     sye_failed += 1
#             elif k == tc_selected_six_random[m]:
#                 current_question_number += 1
#                 print(f"Question {current_question_number}/{total_questions}\n")
#                 print(questions)
#                 y = input("Select your answer: \n")
#                 # y == k.getitem() ? correct+=1 : failed+=1
#                 if y == answers:
#                     tc_correct += 1
#                 else:
#                     tc_failed += 1
#
# print("==" * 30)
# print(f"AI\n===\n correct = {ai_correct}, failed = {ai_failed}\n")
# print(f"SE\n===\n correct = {se_correct}, failed = {se_failed}\n")
# print(f"CN\n===\n correct = {cn_correct}, failed = {cn_failed}\n")
# print(f"SYE\n===\n correct = {sye_correct}, failed = {sye_failed}\n")
# print(f"TC\n===\n correct = {tc_correct}, failed = {tc_failed}\n")
#
# if ai_correct == 0 and se_correct == 0 and cn_correct == 0 and sye_correct == 0 and tc_correct == 0:
#     print("==" * 30)
#     print("No Area of Specialization can be selected\n")
# else:
#     print("==" * 30)
#     new_list = [("AI", ai_correct), ("SE", se_correct), ("CN", cn_correct), ("SYE", sye_correct), ("TC", tc_correct)]
#     new_dict = dict(new_list)
#     reversed_dict = dict(map(reversed, new_list))
#     maximum_score = max(sorted(reversed_dict, reverse=True))
#     for new_sorted_list_checker in new_dict.items():
#         if maximum_score == new_sorted_list_checker[1]:
#             a, b = new_sorted_list_checker
#             new_sorted_list_checker = {a: b}
#             final_scores.append(new_sorted_list_checker)
#     print(final_scores, "\n")
#     print("==" * 30)
#     if len(final_scores) > 1:
#         print("From your assessment, Your area of specialization could be \n")
#         for i in final_scores:
#             for j in i:
#                 if j == 'CN':
#                     print("Computer Networks\n")
#                 if j == 'TC':
#                     print('Theoretical Computing\n')
#                 if j == 'AI':
#                     print('Artificial Intelligence\n')
#                 if j == 'SE':
#                     print('Software Engineering\n')
#                 if j == 'SYE':
#                     print('Systems Engineering\n')
#         print("You could select an select an area of specialization of your choice!")
#     else:
#         for i in final_scores:
#             for j in i:
#                 print("From your assessment, Your area of specialization is\n")
#                 if j == 'CN':
#                     print("Computer Networks\n")
#                 elif j == 'TC':
#                     print('Theoretical Computing\n')
#                 elif j == 'AI':
#                     print('Artificial Intelligence\n')
#                 elif j == 'SE':
#                     print('Software Engineering\n')
#                 elif j == 'SYE':
#                     print('Systems Engineering\n')

# print("Kindly view the performance of people in that Field!")  # do clustering
