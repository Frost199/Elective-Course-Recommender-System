import random


class Util:

    @staticmethod
    def processed_list_dict(questions, answers):
        questions_list = []
        answers_list = []
        list_of_dictionaries_of_questions_and_answers = []

        for i in questions[1:]:
            for k in i:
                questions_list.append(k)

        for i in answers[1:]:
            for k in i:
                answers_list.append(k)

        for i in range(len(questions_list)):
            ai_dictionary = {questions_list[i]: answers_list[i]}
            list_of_dictionaries_of_questions_and_answers.append(ai_dictionary)

        return list_of_dictionaries_of_questions_and_answers

    @staticmethod
    def select_six_random(list_of_dictionaries):
        random.shuffle(list_of_dictionaries, random.random)
        list_of_dictionaries = list_of_dictionaries[:5]
        return list_of_dictionaries

    @staticmethod
    def all_selected_questions_with_answers(course_a, course_b, course_c, course_d):
        total_list_of_selected_questions_with_answers = dict()
        for i in range(len(course_a)):
            total_list_of_selected_questions_with_answers.update({str(i + 1): [course_a[i],
                                                                               course_b[i],
                                                                               course_c[i],
                                                                               course_d[i]]})
            # total_list_of_selected_questions_with_answers.append(batch_list_of_selected_questions_with_answers)
        return total_list_of_selected_questions_with_answers
