import pygal
from pygal.style import Style
from flask import Blueprint, url_for, redirect, render_template, request, session
from decorators import question_info_page, question_finished
from flask_login import current_user, login_required

from models.aos_questions_and_answer.processed_questions_and_answers import total_questions_and_answer, \
    total_questions, \
    ai_selected_six_random, tc_selected_six_random, sye_selected_six_random, cn_selected_six_random, \
    se_selected_six_random
from models.forms.forms import StartQuiz, QuestionForm
from models.aos_questions_and_answer.kmeans_cluster import Clustering

aos_test = Blueprint('aos_test', __name__, template_folder='templates')


@aos_test.route('/area_of_specialization_info_page', methods=['GET', 'POST'])
@login_required
def index():
    global counting_down
    counting_down = 5 * 60
    session["current_question"] = '0'
    form = StartQuiz()
    if form.validate_on_submit():
        return redirect(url_for('aos_test.timer'))
    image_file = url_for('static', filename='assets/pictures/' + current_user.default_image)
    return render_template('questions/question_info.html', image_file=image_file, form=form)


@aos_test.route('/questions', methods=['GET', 'POST'])
@login_required
@question_info_page
def timer():
    global rounds
    global current_number
    global answers
    global ai_correct
    global ai_failed
    global se_correct
    global se_failed
    global cn_correct
    global cn_failed
    global sye_correct
    global sye_failed
    global tc_correct
    global tc_failed
    global total_correct
    global total_failed
    global user_response
    global session_count
    global a
    global b
    global c
    global question_to_ask
    global next_question
    global back_val
    global current_answer
    global selected_courses
    global session_dict
    global switch

    form = QuestionForm()
    question_to_ask = ''
    a = ""
    b = ""
    c = ""
    # Initializing variables

    # AI = []
    # SE = []
    # CN = []
    # SYE = []
    # TC = []
    final_scores = []

    if session["current_question"] == '0':
        rounds = 0
        current_number = 1
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
        total_correct = 0
        total_failed = 0
        session_count = 1
        selected_courses = ""
        user_response = "got_1"
        next_question = "Next Question"
        session_dict = dict()

        # The first time the page is loaded, the current question is not set.
        # This means that the user has not started to quiz yet. So set the
        # current question to question 1 and save it in the session.
        session["current_question"] = '1'
        back_val = False
        switch = False
        # return jsonify({'first': "Value"})
    current_q = total_questions_and_answer[session["current_question"]][rounds]
    question_tuple = tuple(current_q.items())
    # print(question_tuple)
    for question_posted in question_tuple:
        questions, answers = question_posted
        questions = questions.split()
        question_to_ask = " ".join(questions[:questions.index('(A)')])
        mango = questions[questions.index('(A)'):]
        a = " ".join(mango[:mango.index('(B)')])
        b = " ".join(mango[mango.index('(B)'):mango.index('(C)')])
        c = " ".join(mango[mango.index('(C)'):])
        # request.form['answer_option'] = current_answer
    form.question_option.choices = [("A", a), ("B", b), ("C", c)]
    form.process()

    if request.method == 'POST':
        current_answer = request.form.get('answer_option', '')
        # print(current_answer)
        session_dict.update({session["current_question"]: [question_to_ask, answers, current_answer]})
        if not current_answer:
            print(current_answer)
            current_number += 1
            rounds += 1
            back_val = True
            if rounds == 5:
                rounds = 0
                session["current_question"] = str(int(session["current_question"]) + 1)

                # submit
                if session["current_question"] == '7' and rounds == 0:
                    session["finished"] = "yes"
                    selected_courses_list = []
                    session.pop("current_question")
                    print(session["finished"])
                    print(type(session["finished"]))
                    # session["current_question"]
                    rounds = 0
                    current_number = 1
                    print("Total Correct", total_correct)
                    print("Total Failed", total_failed)
                    print("ÄI_Correct: {}, AI_failed: {}".format(ai_correct, ai_failed))

                    print("SE_Correct: {}, SE_Failed: {}".format(se_correct, se_failed))

                    print("CN_Correct: {}, CN_Failed: {}".format(cn_correct, cn_failed))

                    print("SYE_Correct: {}, SYE_failed: {}".format(sye_correct, sye_failed))

                    print("TC_Correct: {}, TC_Failed: {}".format(tc_correct, tc_failed))
                    if ai_correct == 0 and se_correct == 0 and cn_correct == 0 and sye_correct == 0 and tc_correct == 0:
                        user_response = "No Area of Specialization can be selected"
                        print(user_response)
                        selected_courses = "None"
                    else:
                        new_list = [("AI", ai_correct), ("SE", se_correct), ("CN", cn_correct), ("SYE", sye_correct),
                                    ("TC", tc_correct)]
                        print("NEW LIST: ", new_list)
                        new_dict = dict(new_list)
                        print("Converted to DICT: ", new_dict)
                        reversed_dict = dict(map(reversed, new_list))
                        print("Reversed Dict: ", reversed_dict)
                        maximum_score = max(sorted(reversed_dict, reverse=True))
                        print("Max Score: ", maximum_score)
                        for new_sorted_list_checker in new_dict.items():
                            if maximum_score == new_sorted_list_checker[1]:
                                print("Sorted_list_checker: ", new_sorted_list_checker)
                                a, b = new_sorted_list_checker
                                new_sorted_list_checker = {a: b}
                                print("Arranged Sorted List Checker: ", new_sorted_list_checker)
                                final_scores.append(new_sorted_list_checker)
                        print(final_scores)
                        if len(final_scores) > 1:
                            # print("From your assessment, Your area of specialization could be \n")
                            for i in final_scores:
                                for j in i:
                                    if j == 'CN':
                                        selected_courses_list.append("Computer Networks")
                                    elif j == 'TC':
                                        selected_courses_list.append("Theoretical Computing")
                                    elif j == 'AI':
                                        selected_courses_list.append("Artificial Intelligence")
                                    elif j == 'SE':
                                        selected_courses_list.append("Software Engineering")
                                    elif j == 'SYE':
                                        selected_courses_list.append("Systems Engineering")
                            selected_courses = ", ".join(selected_courses_list)
                            print("Selected courses: ", selected_courses)
                            # print("You could select an select an area of specialization of your choice!")
                        else:
                            for i in final_scores:
                                for j in i:
                                    # print("From your assessment, Your area of specialization is\n")
                                    if j == 'CN':
                                        selected_courses += "Computer Networks"
                                    elif j == 'TC':
                                        selected_courses += "Theoretical Computing"
                                    elif j == 'AI':
                                        selected_courses += "Artificial Intelligence"
                                    elif j == 'SE':
                                        selected_courses += "Software Engineering"
                                    elif j == 'SYE':
                                        selected_courses += "Systems Engineering"
                            print("Selected course: ", selected_courses)

                    return redirect(url_for('aos_test.submit'))

            # Last question to ask
            if session["current_question"] == '6' and rounds == 4:
                switch = True
                print("I ma here")
                next_question = "Submit"
                return redirect(url_for('aos_test.timer'))
            if session["current_question"] in total_questions_and_answer:
                # If the question exists in the dictionary, redirect to the question
                #
                return redirect(url_for('aos_test.timer'))
        else:
            current_answer = request.form['answer_option']
            print(answers)
            print("User answer: ", current_answer)
            print("Loop for selected Six Random: ", int(session["current_question"]) - 1)

            if ai_selected_six_random[int(session["current_question"]) - 1] == \
                    total_questions_and_answer[session["current_question"]][rounds]:
                current_number += 1
                rounds += 1
                print("AI Found")
                if current_answer == answers:
                    ai_correct += 1
                    total_correct += 1
                else:
                    ai_failed += 1
                    total_failed += 1
                print("ai_correct: ", ai_correct)
                print("ai_failed: ", ai_failed)
                print("Total_Correct: ", total_correct)
                print("Total_failed: ", total_failed)
            elif se_selected_six_random[int(session["current_question"]) - 1] == \
                    total_questions_and_answer[session["current_question"]][rounds]:
                current_number += 1
                rounds += 1
                print("SE Found")
                if current_answer == answers:
                    se_correct += 1
                    total_correct += 1
                else:
                    se_failed += 1
                    total_failed += 1

                print("se_correct: ", se_correct)
                print("se_failed: ", se_failed)
                print("Total_Correct: ", total_correct)
                print("Total_failed: ", total_failed)
            elif cn_selected_six_random[int(session["current_question"]) - 1] == \
                    total_questions_and_answer[session["current_question"]][rounds]:
                current_number += 1
                rounds += 1
                print("CN Found")
                if current_answer == answers:
                    cn_correct += 1
                    total_correct += 1
                else:
                    cn_failed += 1
                    total_failed += 1

                print("cn_correct: ", cn_correct)
                print("cn_failed: ", cn_failed)
                print("Total_Correct: ", total_correct)
                print("Total_failed: ", total_failed)
            elif sye_selected_six_random[int(session["current_question"]) - 1] == \
                    total_questions_and_answer[session["current_question"]][rounds]:
                current_number += 1
                rounds += 1
                print("SYE FOUND")
                if current_answer == answers:
                    sye_correct += 1
                    total_correct += 1
                else:
                    sye_failed += 1
                    total_failed += 1

                print("sye_correct: ", sye_correct)
                print("sye_failed: ", sye_failed)
                print("Total_Correct: ", total_correct)
                print("Total_failed: ", total_failed)
            elif tc_selected_six_random[int(session["current_question"]) - 1] == \
                    total_questions_and_answer[session["current_question"]][rounds]:
                current_number += 1
                rounds += 1
                print("TC Found")
                if current_answer == answers:
                    tc_correct += 1
                    total_correct += 1
                else:
                    tc_failed += 1
                    total_failed += 1

                print("tc_correct: ", tc_correct)
                print("tc_failed: ", tc_failed)
                print("Total_Correct: ", total_correct)
                print("Total_failed: ", total_failed)

            if rounds == 5:
                rounds = 0
                main_question_umbrella = 1
                session["current_question"] = str(int(session["current_question"]) + 1)
                main_question_umbrella += 1

                # submit
                if session["current_question"] == '7' and rounds == 0:
                    session["finished"] = "yes"
                    selected_courses = ""
                    user_response = "got_1"
                    selected_courses_list = []
                    session.pop("current_question")
                    print(session["finished"])
                    print(type(session["finished"]))
                    # session["current_question"]
                    rounds = 0
                    current_number = 1
                    print("Total Correct", total_correct)
                    print("Total Failed", total_failed)
                    print("ÄI_Correct: {}, AI_failed: {}".format(ai_correct, ai_failed))

                    print("SE_Correct: {}, SE_Failed: {}".format(se_correct, se_failed))

                    print("CN_Correct: {}, CN_Failed: {}".format(cn_correct, cn_failed))

                    print("SYE_Correct: {}, SYE_failed: {}".format(sye_correct, sye_failed))

                    print("TC_Correct: {}, TC_Failed: {}".format(tc_correct, tc_failed))
                    if ai_correct == 0 and se_correct == 0 and cn_correct == 0 and sye_correct == 0 and tc_correct == 0:
                        user_response = "No Area of Specialization can be selected"
                        print(user_response)
                    else:
                        new_list = [("AI", ai_correct), ("SE", se_correct), ("CN", cn_correct), ("SYE", sye_correct),
                                    ("TC", tc_correct)]
                        print("NEW LIST: ", new_list)
                        new_dict = dict(new_list)
                        print("Converted to DICT: ", new_dict)
                        reversed_dict = dict(map(reversed, new_list))
                        print("Reversed Dict: ", reversed_dict)
                        maximum_score = max(sorted(reversed_dict, reverse=True))
                        print("Max Score: ", maximum_score)
                        for new_sorted_list_checker in new_dict.items():
                            if maximum_score == new_sorted_list_checker[1]:
                                print("Sorted_list_checker: ", new_sorted_list_checker)
                                a, b = new_sorted_list_checker
                                new_sorted_list_checker = {a: b}
                                print("Arranged Sorted List Checker: ", new_sorted_list_checker)
                                final_scores.append(new_sorted_list_checker)
                        print(final_scores)
                        if len(final_scores) > 1:
                            # print("From your assessment, Your area of specialization could be \n")
                            for i in final_scores:
                                for j in i:
                                    if j == 'CN':
                                        selected_courses_list.append("Computer Networks")
                                    elif j == 'TC':
                                        selected_courses_list.append("Theoretical Computing")
                                    elif j == 'AI':
                                        selected_courses_list.append("Artificial Intelligence")
                                    elif j == 'SE':
                                        selected_courses_list.append("Software Engineering")
                                    elif j == 'SYE':
                                        selected_courses_list.append("Systems Engineering")
                            selected_courses = ", ".join(selected_courses_list)
                            print("Selected courses: ", selected_courses)
                            # print("You could select an select an area of specialization of your choice!")
                        else:
                            for i in final_scores:
                                for j in i:
                                    # print("From your assessment, Your area of specialization is\n")
                                    if j == 'CN':
                                        selected_courses += "Computer Networks"
                                    elif j == 'TC':
                                        selected_courses += "Theoretical Computing"
                                    elif j == 'AI':
                                        selected_courses += "Artificial Intelligence"
                                    elif j == 'SE':
                                        selected_courses += "Software Engineering"
                                    elif j == 'SYE':
                                        selected_courses += "Systems Engineering"
                            print("Selected course: ", selected_courses)

                    return redirect(url_for('aos_test.submit'))
            if rounds >= 0 and int(session["current_question"]) > 1:
                back_val = True
            if rounds > 0 and int(session["current_question"]) == 1:
                back_val = True

            # Last question to answer
            if session["current_question"] == '6' and rounds == 4:
                next_question = "Submit"
                switch = True
            #     return redirect(url_for('aos_test.timer'))
            if session["current_question"] in total_questions_and_answer:
                # If the question exists in the dictionary, redirect to the question
                #
                return redirect(url_for('aos_test.timer'))

            session_count = int(session_count['current_question'])

    return render_template('questions/questions.html', num_counter=counting_down, switch=switch,
                           num=current_number, next_question=next_question, back_val=back_val,
                           ntot=total_questions,
                           question=question_to_ask,
                           ans1=a,
                           ans2=b,
                           ans3=c, form=form)


@aos_test.route('/question_back', methods=['GET', 'POST'])
@login_required
def back():
    if request.method == 'POST':
        global next_question
        global rounds
        global current_number
        global back_val
        global session_dict
        global total_correct
        global total_failed
        global switch

        current_round = rounds
        next_question = "Next Question"
        switch = False
        # current_round -= 1
        # rounds = current_round
        if current_round == 1 and session["current_question"] == '1':
            back_val = False
        if current_round == 0:
            session["current_question"] = str(int(session["current_question"]) - 1)
            if session["current_question"] in session_dict.keys():
                if session_dict[session["current_question"]][2] is not None:
                    if session_dict[session["current_question"]][1] == session_dict[session["current_question"]][2]:
                        total_correct -= 1
                    else:
                        total_failed -= 1
            current_number -= 1
            rounds = 4
            return redirect(url_for('aos_test.timer'))
        else:
            current_round -= 1
            current_number -= 1
            rounds = current_round
            return redirect(url_for('aos_test.timer'))


@aos_test.route('/submit', methods=['GET', 'POST'])
@login_required
@question_finished
def submit():
    total_questions_answered = 0
    global total_correct
    global total_failed
    global selected_courses
    global user_response
    print(total_correct)
    print(total_failed)
    print(type(selected_courses))
    print(user_response)
    try:
        total_questions_answered = int(total_correct) + int(total_failed)
    except Exception as e:
        print(e)
        pass
    # total_questions_answered = str(int(tot_correct) + int(tot_failed))
    return render_template("result/result.html", title="Result", total_correct=int(total_correct),
                           total_failed=int(total_failed),
                           total_questions_answered=total_questions_answered,
                           sel_courses=selected_courses, user_resp=user_response)


@aos_test.route('/time_up', methods=['GET'])
@login_required
def time_up_from_client():
    global ai_correct
    global ai_failed
    global se_correct
    global se_failed
    global cn_correct
    global cn_failed
    global sye_correct
    global sye_failed
    global tc_correct
    global tc_failed
    global total_correct
    global total_failed
    global user_response
    global selected_courses
    final_scores_new = []
    selected_courses_list_new = []
    session["finished"] = "yes"
    session.pop("current_question")
    if ai_correct == 0 and se_correct == 0 and cn_correct == 0 and sye_correct == 0 and tc_correct == 0:
        user_response = "No Area of Specialization can be selected"
        print(user_response)
    else:
        new_list = [("AI", ai_correct), ("SE", se_correct), ("CN", cn_correct), ("SYE", sye_correct),
                    ("TC", tc_correct)]
        print("NEW LIST: ", new_list)
        new_dict = dict(new_list)
        print("Converted to DICT: ", new_dict)
        reversed_dict = dict(map(reversed, new_list))
        print("Reversed Dict: ", reversed_dict)
        maximum_score = max(sorted(reversed_dict, reverse=True))
        print("Max Score: ", maximum_score)
        for new_sorted_list_checker in new_dict.items():
            if maximum_score == new_sorted_list_checker[1]:
                print("Sorted_list_checker: ", new_sorted_list_checker)
                a_new, b_new = new_sorted_list_checker
                new_sorted_list_checker = {a_new: b_new}
                print("Arranged Sorted List Checker: ", new_sorted_list_checker)
                final_scores_new.append(new_sorted_list_checker)
        print(final_scores_new)
        if len(final_scores_new) > 1:
            # print("From your assessment, Your area of specialization could be \n")
            for i in final_scores_new:
                for j in i:
                    if j == 'CN':
                        selected_courses_list_new.append("Computer Networks")
                    elif j == 'TC':
                        selected_courses_list_new.append("Theoretical Computing")
                    elif j == 'AI':
                        selected_courses_list_new.append("Artificial Intelligence")
                    elif j == 'SE':
                        selected_courses_list_new.append("Software Engineering")
                    elif j == 'SYE':
                        selected_courses_list_new.append("Systems Engineering")
            selected_courses = ", ".join(selected_courses_list_new)
            print("Selected courses: ", selected_courses)
            # print("You could select an select an area of specialization of your choice!")
        else:
            for i in final_scores_new:
                for j in i:
                    # print("From your assessment, Your area of specialization is\n")
                    if j == 'CN':
                        selected_courses += "Computer Networks"
                    elif j == 'TC':
                        selected_courses += "Theoretical Computing"
                    elif j == 'AI':
                        selected_courses += "Artificial Intelligence"
                    elif j == 'SE':
                        selected_courses += "Software Engineering"
                    elif j == 'SYE':
                        selected_courses += "Systems Engineering"
            print("Selected course: ", selected_courses)
    return redirect(url_for('aos_test.submit'))


@aos_test.route('/past_performance', methods=['GET', 'POST'])
@login_required
@question_finished
def past_record():
    global selected_courses
    global ai_cos843_data
    global ai_cos828_data
    global cn_cos847_data
    global cn_cos842_data
    global se_cos829_data
    global se_cos826_data
    global sye_cos819_data
    global sye_cos808_data
    global selected_courses

    ai_cos843_data = None
    ai_cos828_data = None
    cn_cos847_data = None
    cn_cos842_data = None
    se_cos829_data = None
    se_cos826_data = None
    sye_cos819_data = None
    sye_cos808_data = None

    ai_first_cluster_1_no_of_students = None
    ai_second_cluster_1_no_of_students = None
    ai_third_cluster_1_no_of_students = None
    ai_fourth_cluster_1_no_of_students = None
    ai_fifth_cluster_1_no_of_students = None
    ai_sixth_cluster_1_no_of_students = None
    ai_first_cluster_2_no_of_students = None
    ai_second_cluster_2_no_of_students = None
    ai_third_cluster_2_no_of_students = None
    ai_fourth_cluster_2_no_of_students = None
    ai_fifth_cluster_2_no_of_students = None
    ai_sixth_cluster_2_no_of_students = None

    cn_first_cluster_1_no_of_students = None
    cn_second_cluster_1_no_of_students = None
    cn_third_cluster_1_no_of_students = None
    cn_fourth_cluster_1_no_of_students = None
    cn_fifth_cluster_1_no_of_students = None
    cn_sixth_cluster_1_no_of_students = None
    cn_first_cluster_2_no_of_students = None
    cn_second_cluster_2_no_of_students = None
    cn_third_cluster_2_no_of_students = None
    cn_fourth_cluster_2_no_of_students = None
    cn_fifth_cluster_2_no_of_students = None
    cn_sixth_cluster_2_no_of_students = None

    se_first_cluster_1_no_of_students = None
    se_second_cluster_1_no_of_students = None
    se_third_cluster_1_no_of_students = None
    se_fourth_cluster_1_no_of_students = None
    se_fifth_cluster_1_no_of_students = None
    se_sixth_cluster_1_no_of_students = None
    se_first_cluster_2_no_of_students = None
    se_second_cluster_2_no_of_students = None
    se_third_cluster_2_no_of_students = None
    se_fourth_cluster_2_no_of_students = None
    se_fifth_cluster_2_no_of_students = None
    se_sixth_cluster_2_no_of_students = None

    sye_first_cluster_1_no_of_students = None
    sye_second_cluster_1_no_of_students = None
    sye_third_cluster_1_no_of_students = None
    sye_fourth_cluster_1_no_of_students = None
    sye_fifth_cluster_1_no_of_students = None
    sye_sixth_cluster_1_no_of_students = None
    sye_first_cluster_2_no_of_students = None
    sye_second_cluster_2_no_of_students = None
    sye_third_cluster_2_no_of_students = None
    sye_fourth_cluster_2_no_of_students = None
    sye_fifth_cluster_2_no_of_students = None
    sye_sixth_cluster_2_no_of_students = None

    splited_course = selected_courses.split(", ")
    custom_style = Style(title_font_size=50, tooltip_font_size=40, label_font_size=40, legend_font_size=40)

    ai_pie_chart = "Students Performance in Artificial Intelligence for COS843 and COS828"
    cn_pie_chart = "Students Performance in Computer Networks for COS847 and COS842"
    se_pie_chart = "Students Performance in Software Engineering for COS829 and COS826"
    sye_pie_chart = "Students Performance in Systems Engineering for COS819 and COS808"
    for i in splited_course:
        if i == "Artificial Intelligence":
            ai_cos843 = pygal.Pie(style=custom_style)
            ai_cos843.title = "Performance for COS843"

            ai_cos828 = pygal.Pie(style=custom_style)
            ai_cos828.title = "Performance for COS828"

            first_cluster_1, second_cluster_1, third_cluster_1, fourth_cluster_1, fifth_cluster_1, sixth_cluster_1, \
            total_students_1, first_cluster_2, second_cluster_2, third_cluster_2, fourth_cluster_2, fifth_cluster_2, \
            sixth_cluster_2, total_students_2, ai_first_cluster_1_no_of_students, ai_second_cluster_1_no_of_students, \
            ai_third_cluster_1_no_of_students, ai_fourth_cluster_1_no_of_students, ai_fifth_cluster_1_no_of_students, \
            ai_sixth_cluster_1_no_of_students, ai_first_cluster_2_no_of_students, ai_second_cluster_2_no_of_students, \
            ai_third_cluster_2_no_of_students, ai_fourth_cluster_2_no_of_students, ai_fifth_cluster_2_no_of_students, \
            ai_sixth_cluster_2_no_of_students = \
                cluster_function('models/aos_questions_and_answer/dataset/clustering/ai_cluster.csv')

            ai_cos843.add("Segment 1", first_cluster_1)
            ai_cos843.add("Segment 2", second_cluster_1)
            ai_cos843.add("Segment 3", third_cluster_1)
            ai_cos843.add("Segment 4", fourth_cluster_1)
            ai_cos843.add("Segment 5", fifth_cluster_1)
            ai_cos843.add("Segment 6", sixth_cluster_1)
            ai_cos843_data = ai_cos843.render_data_uri()

            ai_cos828.add("Segment 1", first_cluster_2)
            ai_cos828.add("Segment 2", second_cluster_2)
            ai_cos828.add("Segment 3", third_cluster_2)
            ai_cos828.add("Segment 4", fourth_cluster_2)
            ai_cos828.add("Segment 5", fifth_cluster_2)
            ai_cos828.add("Segment 6", sixth_cluster_2)
            ai_cos828_data = ai_cos828.render_data_uri()

        if i == "Computer Networks":
            cn_cos847 = pygal.Pie(style=custom_style)
            cn_cos847.title = "Performance for COS847"

            cn_cos842 = pygal.Pie(style=custom_style)
            cn_cos842.title = "Performance for COS842"

            first_cluster_1, second_cluster_1, third_cluster_1, fourth_cluster_1, fifth_cluster_1, sixth_cluster_1, \
            total_students_1, first_cluster_2, second_cluster_2, third_cluster_2, fourth_cluster_2, fifth_cluster_2, \
            sixth_cluster_2, total_students_2, cn_first_cluster_1_no_of_students, cn_second_cluster_1_no_of_students, \
            cn_third_cluster_1_no_of_students, cn_fourth_cluster_1_no_of_students, cn_fifth_cluster_1_no_of_students, \
            cn_sixth_cluster_1_no_of_students, cn_first_cluster_2_no_of_students, cn_second_cluster_2_no_of_students, \
            cn_third_cluster_2_no_of_students, cn_fourth_cluster_2_no_of_students, cn_fifth_cluster_2_no_of_students, \
            cn_sixth_cluster_2_no_of_students = \
                cluster_function('models/aos_questions_and_answer/dataset/clustering/computer_networks.csv')

            cn_cos847.add("Segment 1", first_cluster_1)
            cn_cos847.add("Segment 2", second_cluster_1)
            cn_cos847.add("Segment 3", third_cluster_1)
            cn_cos847.add("Segment 4", fourth_cluster_1)
            cn_cos847.add("Segment 5", fifth_cluster_1)
            cn_cos847.add("Segment 6", sixth_cluster_1)
            cn_cos847_data = cn_cos847.render_data_uri()

            cn_cos842.add("Segment 1", first_cluster_2)
            cn_cos842.add("Segment 2", second_cluster_2)
            cn_cos842.add("Segment 3", third_cluster_2)
            cn_cos842.add("Segment 4", fourth_cluster_2)
            cn_cos842.add("Segment 5", fifth_cluster_2)
            cn_cos842.add("Segment 6", sixth_cluster_2)
            cn_cos842_data = cn_cos842.render_data_uri()

        if i == "Software Engineering":
            se_cos829 = pygal.Pie(style=custom_style)
            se_cos829.title = "Performance for COS829"

            se_cos826 = pygal.Pie(style=custom_style)
            se_cos826.title = "Performance for COS826"

            first_cluster_1, second_cluster_1, third_cluster_1, fourth_cluster_1, fifth_cluster_1, sixth_cluster_1, \
            total_students_1, first_cluster_2, second_cluster_2, third_cluster_2, fourth_cluster_2, fifth_cluster_2, \
            sixth_cluster_2, total_students_2, se_first_cluster_1_no_of_students, se_second_cluster_1_no_of_students, \
            se_third_cluster_1_no_of_students, se_fourth_cluster_1_no_of_students, se_fifth_cluster_1_no_of_students, \
            se_sixth_cluster_1_no_of_students, se_first_cluster_2_no_of_students, se_second_cluster_2_no_of_students, \
            se_third_cluster_2_no_of_students, se_fourth_cluster_2_no_of_students, se_fifth_cluster_2_no_of_students, \
            se_sixth_cluster_2_no_of_students = \
                cluster_function('models/aos_questions_and_answer/dataset/clustering/software_eng_cluster.csv')

            se_cos829.add("Segment 1", first_cluster_1)
            se_cos829.add("Segment 2", second_cluster_1)
            se_cos829.add("Segment 3", third_cluster_1)
            se_cos829.add("Segment 4", fourth_cluster_1)
            se_cos829.add("Segment 5", fifth_cluster_1)
            se_cos829.add("Segment 6", sixth_cluster_1)
            se_cos829_data = se_cos829.render_data_uri()

            se_cos826.add("Segment 1", first_cluster_2)
            se_cos826.add("Segment 2", second_cluster_2)
            se_cos826.add("Segment 3", third_cluster_2)
            se_cos826.add("Segment 4", fourth_cluster_2)
            se_cos826.add("Segment 5", fifth_cluster_2)
            se_cos826.add("Segment 6", sixth_cluster_2)
            se_cos826_data = se_cos826.render_data_uri()

        if i == "Systems Engineering":
            sye_cos819 = pygal.Pie(style=custom_style)
            sye_cos819.title = "Performance for COS819"

            sye_cos808 = pygal.Pie(style=custom_style)
            sye_cos808.title = "Performance for COS808"

            first_cluster_1, second_cluster_1, third_cluster_1, fourth_cluster_1, fifth_cluster_1, sixth_cluster_1, \
            total_students_1, first_cluster_2, second_cluster_2, third_cluster_2, fourth_cluster_2, fifth_cluster_2, \
            sixth_cluster_2, total_students_2, sye_first_cluster_1_no_of_students, \
            sye_second_cluster_1_no_of_students, sye_third_cluster_1_no_of_students, \
            sye_fourth_cluster_1_no_of_students, sye_fifth_cluster_1_no_of_students, \
            sye_sixth_cluster_1_no_of_students, sye_first_cluster_2_no_of_students, \
            sye_second_cluster_2_no_of_students, sye_third_cluster_2_no_of_students, \
            sye_fourth_cluster_2_no_of_students, sye_fifth_cluster_2_no_of_students, \
            sye_sixth_cluster_2_no_of_students = \
                cluster_function('models/aos_questions_and_answer/dataset/clustering/system_eng_cluster.csv')

            sye_cos819.add("Segment 1", first_cluster_1)
            sye_cos819.add("Segment 2", second_cluster_1)
            sye_cos819.add("Segment 3", third_cluster_1)
            sye_cos819.add("Segment 4", fourth_cluster_1)
            sye_cos819.add("Segment 5", fifth_cluster_1)
            sye_cos819.add("Segment 6", sixth_cluster_1)
            sye_cos819_data = sye_cos819.render_data_uri()

            sye_cos808.add("Segment 1", first_cluster_2)
            sye_cos808.add("Segment 2", second_cluster_2)
            sye_cos808.add("Segment 3", third_cluster_2)
            sye_cos808.add("Segment 4", fourth_cluster_2)
            sye_cos808.add("Segment 5", fifth_cluster_2)
            sye_cos808.add("Segment 6", sixth_cluster_2)
            sye_cos808_data = sye_cos808.render_data_uri()

    return render_template("result/past_record.html", title="Past Performance", ai_cos843_data=ai_cos843_data,
                           ai_cos828_data=ai_cos828_data, cn_cos847_data=cn_cos847_data,
                           cn_cos842_data=cn_cos842_data, se_cos829_data=se_cos829_data,
                           se_cos826_data=se_cos826_data, sye_cos819_data=sye_cos819_data,
                           sye_cos808_data=sye_cos808_data, ai_pie_chart=ai_pie_chart, cn_pie_chart=cn_pie_chart,
                           se_pie_chart=se_pie_chart, sye_pie_chart=sye_pie_chart, splited_course=splited_course,
                           ai_first_cluster_1_no_of_students=ai_first_cluster_1_no_of_students,
                           ai_second_cluster_1_no_of_students=ai_second_cluster_1_no_of_students,
                           ai_third_cluster_1_no_of_students=ai_third_cluster_1_no_of_students,
                           ai_fourth_cluster_1_no_of_students=ai_fourth_cluster_1_no_of_students,
                           ai_fifth_cluster_1_no_of_students=ai_fifth_cluster_1_no_of_students,
                           ai_sixth_cluster_1_no_of_students=ai_sixth_cluster_1_no_of_students,
                           ai_first_cluster_2_no_of_students=ai_first_cluster_2_no_of_students,
                           ai_second_cluster_2_no_of_students=ai_second_cluster_2_no_of_students,
                           ai_third_cluster_2_no_of_students=ai_third_cluster_2_no_of_students,
                           ai_fourth_cluster_2_no_of_students=ai_fourth_cluster_2_no_of_students,
                           ai_fifth_cluster_2_no_of_students=ai_fifth_cluster_2_no_of_students,
                           ai_sixth_cluster_2_no_of_students=ai_sixth_cluster_2_no_of_students,
                           cn_first_cluster_1_no_of_students=cn_first_cluster_1_no_of_students,
                           cn_second_cluster_1_no_of_students=cn_second_cluster_1_no_of_students,
                           cn_third_cluster_1_no_of_students=cn_third_cluster_1_no_of_students,
                           cn_fourth_cluster_1_no_of_students=cn_fourth_cluster_1_no_of_students,
                           cn_fifth_cluster_1_no_of_students=cn_fifth_cluster_1_no_of_students,
                           cn_sixth_cluster_1_no_of_students=cn_sixth_cluster_1_no_of_students,
                           cn_first_cluster_2_no_of_students=cn_first_cluster_2_no_of_students,
                           cn_second_cluster_2_no_of_students=cn_second_cluster_2_no_of_students,
                           cn_third_cluster_2_no_of_students=cn_third_cluster_2_no_of_students,
                           cn_fourth_cluster_2_no_of_students=cn_fourth_cluster_2_no_of_students,
                           cn_fifth_cluster_2_no_of_students=cn_fifth_cluster_2_no_of_students,
                           cn_sixth_cluster_2_no_of_students=cn_sixth_cluster_2_no_of_students,
                           se_first_cluster_1_no_of_students=se_first_cluster_1_no_of_students,
                           se_second_cluster_1_no_of_students=se_second_cluster_1_no_of_students,
                           se_third_cluster_1_no_of_students=se_third_cluster_1_no_of_students,
                           se_fourth_cluster_1_no_of_students=se_fourth_cluster_1_no_of_students,
                           se_fifth_cluster_1_no_of_students=se_fifth_cluster_1_no_of_students,
                           se_sixth_cluster_1_no_of_students=se_sixth_cluster_1_no_of_students,
                           se_first_cluster_2_no_of_students=se_first_cluster_2_no_of_students,
                           se_second_cluster_2_no_of_students=se_second_cluster_2_no_of_students,
                           se_third_cluster_2_no_of_students=se_third_cluster_2_no_of_students,
                           se_fourth_cluster_2_no_of_students=se_fourth_cluster_2_no_of_students,
                           se_fifth_cluster_2_no_of_students=se_fifth_cluster_2_no_of_students,
                           se_sixth_cluster_2_no_of_students=se_sixth_cluster_2_no_of_students,
                           sye_first_cluster_1_no_of_students=sye_first_cluster_1_no_of_students,
                           sye_second_cluster_1_no_of_students=sye_second_cluster_1_no_of_students,
                           sye_third_cluster_1_no_of_students=sye_third_cluster_1_no_of_students,
                           sye_fourth_cluster_1_no_of_students=sye_fourth_cluster_1_no_of_students,
                           sye_fifth_cluster_1_no_of_students=sye_fifth_cluster_1_no_of_students,
                           sye_sixth_cluster_1_no_of_students=sye_sixth_cluster_1_no_of_students,
                           sye_first_cluster_2_no_of_students=sye_first_cluster_2_no_of_students,
                           sye_second_cluster_2_no_of_students=sye_second_cluster_2_no_of_students,
                           sye_third_cluster_2_no_of_students=sye_third_cluster_2_no_of_students,
                           sye_fourth_cluster_2_no_of_students=sye_fourth_cluster_2_no_of_students,
                           sye_fifth_cluster_2_no_of_students=sye_fifth_cluster_2_no_of_students,
                           sye_sixth_cluster_2_no_of_students=sye_sixth_cluster_2_no_of_students,
                           sel_courses=selected_courses)


def cluster_function(csv_to_load):
    first_cluster_1 = 0
    second_cluster_1 = 0
    third_cluster_1 = 0
    fourth_cluster_1 = 0
    fifth_cluster_1 = 0
    sixth_cluster_1 = 0

    first_cluster_2 = 0
    second_cluster_2 = 0
    third_cluster_2 = 0
    fourth_cluster_2 = 0
    fifth_cluster_2 = 0
    sixth_cluster_2 = 0
    # cluster_from_file = Clustering('models/aos_questions_and_answer/dataset/clustering/system_eng_cluster.csv')
    cluster_from_file = Clustering(csv_to_load)
    first_prediction, second_prediction = cluster_from_file.predict_data()
    for i_first_iterator in first_prediction:
        if i_first_iterator == 0:
            first_cluster_1 += 1
        elif i_first_iterator == 1:
            second_cluster_1 += 1
        elif i_first_iterator == 2:
            third_cluster_1 += 1
        elif i_first_iterator == 3:
            fourth_cluster_1 += 1
        elif i_first_iterator == 4:
            fifth_cluster_1 += 1
        elif i_first_iterator == 5:
            sixth_cluster_1 += 1

    for i_second_iterator in second_prediction:
        if i_second_iterator == 0:
            first_cluster_2 += 1
        elif i_second_iterator == 1:
            second_cluster_2 += 1
        elif i_second_iterator == 2:
            third_cluster_2 += 1
        elif i_second_iterator == 3:
            fourth_cluster_2 += 1
        elif i_second_iterator == 4:
            fifth_cluster_2 += 1
        elif i_second_iterator == 5:
            sixth_cluster_2 += 1

    first_cluster_pie_chart_1 = (first_cluster_1 / len(first_prediction)) * 360
    second_cluster_pie_chart_1 = (second_cluster_1 / len(first_prediction)) * 360
    third_cluster_pie_chart_1 = (third_cluster_1 / len(first_prediction)) * 360
    fourth_cluster_pie_chart_1 = (fourth_cluster_1 / len(first_prediction)) * 360
    fifth_cluster_pie_chart_1 = (fifth_cluster_1 / len(first_prediction)) * 360
    sixth_cluster_pie_chart_1 = (sixth_cluster_1 / len(first_prediction)) * 360
    total_number_of_students_in_first_course = len(first_prediction)

    first_cluster_pie_chart_2 = (first_cluster_2 / len(second_prediction)) * 360
    second_cluster_pie_chart_2 = (second_cluster_2 / len(second_prediction)) * 360
    third_cluster_pie_chart_2 = (third_cluster_2 / len(second_prediction)) * 360
    fourth_cluster_pie_chart_2 = (fourth_cluster_2 / len(second_prediction)) * 360
    fifth_cluster_pie_chart_2 = (fifth_cluster_2 / len(second_prediction)) * 360
    sixth_cluster_pie_chart_2 = (sixth_cluster_2 / len(second_prediction)) * 360
    total_number_of_students_in_second_course = len(second_prediction)

    return first_cluster_pie_chart_1, second_cluster_pie_chart_1, third_cluster_pie_chart_1, \
           fourth_cluster_pie_chart_1, fifth_cluster_pie_chart_1, sixth_cluster_pie_chart_1, \
           total_number_of_students_in_first_course, first_cluster_pie_chart_2, second_cluster_pie_chart_2, \
           third_cluster_pie_chart_2, fourth_cluster_pie_chart_2, fifth_cluster_pie_chart_2, \
           sixth_cluster_pie_chart_2, \
           total_number_of_students_in_second_course, first_cluster_1, \
           second_cluster_1, third_cluster_1, fourth_cluster_1, fifth_cluster_1, sixth_cluster_1, first_cluster_2, \
           second_cluster_2, third_cluster_2, fourth_cluster_2, fifth_cluster_2, sixth_cluster_2
