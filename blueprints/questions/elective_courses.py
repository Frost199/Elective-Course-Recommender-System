from collections import OrderedDict
from flask import Blueprint, url_for, redirect, render_template, request, session
from decorators import elective_question_info_page, elective_question_finished
import decorators
from flask_login import current_user, login_required
from models.aos_questions_and_answer.dataset.elective_courses_questions.artificial_intelligence.ai_elective_questions \
    import ai_total_questions, \
    ai_total_questions_and_answer, cos_833_selected_six_random, cos_816_selected_six_random, \
    cos_830_selected_six_random, cos_836_selected_six_random, cos_834_selected_six_random, cos_838_selected_six_random
from models.aos_questions_and_answer.dataset.elective_courses_questions.software_engineering.soe_elective_questions \
    import soe_total_questions,\
    soe_total_questions_and_answer, cos_821_selected_six_random, cos_827_selected_six_random, \
    cos_814_selected_six_random, cos_820_selected_six_random
from models.aos_questions_and_answer.dataset.elective_courses_questions.systems_engineering.se_elective_questions \
    import se_total_questions,\
    se_total_questions_and_answer, cos_815_selected_six_random, cos_823_selected_six_random, \
    cos_817_selected_six_random, cos_810_selected_six_random, cos_812_selected_six_random
from models.aos_questions_and_answer.dataset.elective_courses_questions.computer_networks.cn_elective_questions \
    import cn_total_questions,\
    cn_total_questions_and_answer, cos_845_selected_six_random, cos_829_selected_six_random, \
    cos_852_selected_six_random, cos_850_selected_six_random
from models.forms.forms import SelectElectiveCourses, QuestionForm
from sklearn.externals import joblib
from models.Prediction.Prediction import predict_grade_range
import pandas as pd

elective_course = Blueprint('elective_course', __name__, template_folder='templates')


@elective_course.route('/elective_info_page', methods=['GET', 'POST'])
@login_required
def index():
    global counting_down
    global selected_area_of_specialization_from_form
    global cos_833_total_student
    global cos_833_grade_category
    global cos_816_total_student
    global cos_816_grade_category
    global cos_830_total_student
    global cos_830_grade_category
    global cos_836_total_student
    global cos_836_grade_category
    global cos_834_total_student
    global cos_834_grade_category
    global cos_838_total_student
    global cos_838_grade_category

    global cos_845_total_student
    global cos_845_grade_category
    global cos_829_total_student
    global cos_829_grade_category
    global cos_852_total_student
    global cos_852_grade_category
    global cos_850_total_student
    global cos_850_grade_category

    global cos_821_total_student
    global cos_821_grade_category
    global cos_827_total_student
    global cos_827_grade_category
    global cos_814_total_student
    global cos_814_grade_category
    global cos_820_total_student
    global cos_820_grade_category

    global cos_815_total_student
    global cos_815_grade_category
    global cos_823_total_student
    global cos_823_grade_category
    global cos_817_total_student
    global cos_817_grade_category
    global cos_810_total_student
    global cos_810_grade_category
    global cos_812_total_student
    global cos_812_grade_category

    counting_down = 5 * 60
    session["elective_courses_question"] = '0'
    selected_area_of_specialization_from_form = ''
    form = SelectElectiveCourses()
    if form.validate_on_submit():
        if form.user_type.data == "ai":
            dataset = pd.read_csv('models/Prediction/dataset/ai_courses_scores.csv')
            bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
            dataset["COS833 Bins"] = pd.cut(dataset['COS833 SCORE'], bins=bins)
            dataset["COS816 Bins"] = pd.cut(dataset['COS816 SCORE'], bins=bins)
            dataset["COS830 Bins"] = pd.cut(dataset['COS830 SCORE'], bins=bins)
            dataset["COS836 Bins"] = pd.cut(dataset['COS836 SCORE'], bins=bins)
            dataset["COS834 Bins"] = pd.cut(dataset['COS834 SCORE'], bins=bins)
            dataset["COS838 Bins"] = pd.cut(dataset['COS838 SCORE'], bins=bins)
            cos_833_total_student = dataset.iloc[:, :1].values.astype(str)
            cos_833_grade_category = dataset.iloc[:, 12:13].values.astype(str)
            cos_816_total_student = dataset.iloc[:, 2:3].values.astype(str)
            cos_816_grade_category = dataset.iloc[:, 13:14].values.astype(str)
            cos_830_total_student = dataset.iloc[:, 4:5].values.astype(str)
            cos_830_grade_category = dataset.iloc[:, 14:15].values.astype(str)
            cos_836_total_student = dataset.iloc[:, 6:7].values.astype(str)
            cos_836_grade_category = dataset.iloc[:, 15:16].values.astype(str)
            cos_834_total_student = dataset.iloc[:, 8:9].values.astype(str)
            cos_834_grade_category = dataset.iloc[:, 16:17].values.astype(str)
            cos_838_total_student = dataset.iloc[:, 10:11].values.astype(str)
            cos_838_grade_category = dataset.iloc[:, 17:18].values.astype(str)
            selected_area_of_specialization_from_form += "ai"
            return redirect(url_for('elective_course.timer'))
        elif form.user_type.data == "cn":
            dataset = pd.read_csv('models/Prediction/dataset/computer_networks_courses_scores.csv')
            bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
            dataset["COS845 Bins"] = pd.cut(dataset['COS845 SCORE'], bins=bins)
            dataset["COS829 Bins"] = pd.cut(dataset['COS829 SCORE'], bins=bins)
            dataset["COS852 Bins"] = pd.cut(dataset['COS852 SCORE'], bins=bins)
            dataset["COS850 Bins"] = pd.cut(dataset['COS850 SCORE'], bins=bins)
            cos_845_total_student = dataset.iloc[:, :1].values.astype(str)
            cos_845_grade_category = dataset.iloc[:, 8:9].values.astype(str)
            cos_829_total_student = dataset.iloc[:, 2:3].values.astype(str)
            cos_829_grade_category = dataset.iloc[:, 9:10].values.astype(str)
            cos_852_total_student = dataset.iloc[:, 4:5].values.astype(str)
            cos_852_grade_category = dataset.iloc[:, 10:11].values.astype(str)
            cos_850_total_student = dataset.iloc[:, 6:7].values.astype(str)
            cos_850_grade_category = dataset.iloc[:, 11:12].values.astype(str)
            selected_area_of_specialization_from_form += "cn"
            return redirect(url_for('elective_course.timer_cn'))
        elif form.user_type.data == 'se':
            dataset = pd.read_csv('models/Prediction/dataset/software_engineering_courses_scores.csv')
            bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
            dataset["COS821 Bins"] = pd.cut(dataset['COS821 SCORE'], bins=bins)
            dataset["COS827 Bins"] = pd.cut(dataset['COS827 SCORE'], bins=bins)
            dataset["COS814 Bins"] = pd.cut(dataset['COS814 SCORE'], bins=bins)
            dataset["COS820 Bins"] = pd.cut(dataset['COS820 SCORE'], bins=bins)
            cos_821_total_student = dataset.iloc[:, :1].values.astype(str)
            cos_821_grade_category = dataset.iloc[:, 8:9].values.astype(str)
            cos_827_total_student = dataset.iloc[:, 2:3].values.astype(str)
            cos_827_grade_category = dataset.iloc[:, 9:10].values.astype(str)
            cos_814_total_student = dataset.iloc[:, 4:5].values.astype(str)
            cos_814_grade_category = dataset.iloc[:, 10:11].values.astype(str)
            cos_820_total_student = dataset.iloc[:, 6:7].values.astype(str)
            cos_820_grade_category = dataset.iloc[:, 11:12].values.astype(str)
            selected_area_of_specialization_from_form += "se"
            return redirect(url_for('elective_course.timer_se'))
        elif form.user_type.data == 'sye':
            dataset = pd.read_csv('models/Prediction/dataset/system_engineering_courses_scores.csv')
            bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
            dataset["COS815 Bins"] = pd.cut(dataset['COS815 SCORE'], bins=bins)
            dataset["COS823 Bins"] = pd.cut(dataset['COS823 SCORE'], bins=bins)
            dataset["COS817 Bins"] = pd.cut(dataset['COS817 SCORE'], bins=bins)
            dataset["COS810 Bins"] = pd.cut(dataset['COS810 SCORE'], bins=bins)
            dataset["COS812 Bins"] = pd.cut(dataset['COS812 SCORE'], bins=bins)
            cos_815_total_student = dataset.iloc[:, :1].values.astype(str)
            cos_815_grade_category = dataset.iloc[:, 10:11].values.astype(str)
            cos_823_total_student = dataset.iloc[:, 2:3].values.astype(str)
            cos_823_grade_category = dataset.iloc[:, 11:12].values.astype(str)
            cos_817_total_student = dataset.iloc[:, 4:5].values.astype(str)
            cos_817_grade_category = dataset.iloc[:, 12:13].values.astype(str)
            cos_810_total_student = dataset.iloc[:, 6:7].values.astype(str)
            cos_810_grade_category = dataset.iloc[:, 13:14].values.astype(str)
            cos_812_total_student = dataset.iloc[:, 8:9].values.astype(str)
            cos_812_grade_category = dataset.iloc[:, 14:15].values.astype(str)
            selected_area_of_specialization_from_form += "sye"
            return redirect(url_for('elective_course.timer_sye'))
        else:
            return redirect(url_for('elective_course.index'))
    image_file = url_for('static', filename='assets/pictures/' + current_user.default_image)
    decorators.selected_aos = selected_area_of_specialization_from_form
    return render_template('questions/elective_courses/index.html', image_file=image_file, form=form)


@elective_course.route('/aos_selection_page_page', methods=['GET', 'POST'])
@login_required
def index_for_individual():
    global counting_down
    global selected_area_of_specialization_from_form
    global cos_833_total_student
    global cos_833_grade_category
    global cos_816_total_student
    global cos_816_grade_category
    global cos_830_total_student
    global cos_830_grade_category
    global cos_836_total_student
    global cos_836_grade_category
    global cos_834_total_student
    global cos_834_grade_category
    global cos_838_total_student
    global cos_838_grade_category

    global cos_845_total_student
    global cos_845_grade_category
    global cos_829_total_student
    global cos_829_grade_category
    global cos_852_total_student
    global cos_852_grade_category
    global cos_850_total_student
    global cos_850_grade_category

    global cos_821_total_student
    global cos_821_grade_category
    global cos_827_total_student
    global cos_827_grade_category
    global cos_814_total_student
    global cos_814_grade_category
    global cos_820_total_student
    global cos_820_grade_category

    global cos_815_total_student
    global cos_815_grade_category
    global cos_823_total_student
    global cos_823_grade_category
    global cos_817_total_student
    global cos_817_grade_category
    global cos_810_total_student
    global cos_810_grade_category
    global cos_812_total_student
    global cos_812_grade_category

    counting_down = 5 * 60
    session["elective_courses_question"] = '0'
    selected_area_of_specialization_from_form = ''
    form = SelectElectiveCourses()
    if form.validate_on_submit():
        if form.user_type.data == "ai":
            dataset = pd.read_csv('models/Prediction/dataset/ai_courses_scores.csv')
            bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
            dataset["COS833 Bins"] = pd.cut(dataset['COS833 SCORE'], bins=bins)
            dataset["COS816 Bins"] = pd.cut(dataset['COS816 SCORE'], bins=bins)
            dataset["COS830 Bins"] = pd.cut(dataset['COS830 SCORE'], bins=bins)
            dataset["COS836 Bins"] = pd.cut(dataset['COS836 SCORE'], bins=bins)
            dataset["COS834 Bins"] = pd.cut(dataset['COS834 SCORE'], bins=bins)
            dataset["COS838 Bins"] = pd.cut(dataset['COS838 SCORE'], bins=bins)
            cos_833_total_student = dataset.iloc[:, :1].values.astype(str)
            cos_833_grade_category = dataset.iloc[:, 12:13].values.astype(str)
            cos_816_total_student = dataset.iloc[:, 2:3].values.astype(str)
            cos_816_grade_category = dataset.iloc[:, 13:14].values.astype(str)
            cos_830_total_student = dataset.iloc[:, 4:5].values.astype(str)
            cos_830_grade_category = dataset.iloc[:, 14:15].values.astype(str)
            cos_836_total_student = dataset.iloc[:, 6:7].values.astype(str)
            cos_836_grade_category = dataset.iloc[:, 15:16].values.astype(str)
            cos_834_total_student = dataset.iloc[:, 8:9].values.astype(str)
            cos_834_grade_category = dataset.iloc[:, 16:17].values.astype(str)
            cos_838_total_student = dataset.iloc[:, 10:11].values.astype(str)
            cos_838_grade_category = dataset.iloc[:, 17:18].values.astype(str)
            selected_area_of_specialization_from_form += "ai"
            return redirect(url_for('elective_course.timer'))
        elif form.user_type.data == "cn":
            dataset = pd.read_csv('models/Prediction/dataset/computer_networks_courses_scores.csv')
            bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
            dataset["COS845 Bins"] = pd.cut(dataset['COS845 SCORE'], bins=bins)
            dataset["COS829 Bins"] = pd.cut(dataset['COS829 SCORE'], bins=bins)
            dataset["COS852 Bins"] = pd.cut(dataset['COS852 SCORE'], bins=bins)
            dataset["COS850 Bins"] = pd.cut(dataset['COS850 SCORE'], bins=bins)
            cos_845_total_student = dataset.iloc[:, :1].values.astype(str)
            cos_845_grade_category = dataset.iloc[:, 8:9].values.astype(str)
            cos_829_total_student = dataset.iloc[:, 2:3].values.astype(str)
            cos_829_grade_category = dataset.iloc[:, 9:10].values.astype(str)
            cos_852_total_student = dataset.iloc[:, 4:5].values.astype(str)
            cos_852_grade_category = dataset.iloc[:, 10:11].values.astype(str)
            cos_850_total_student = dataset.iloc[:, 6:7].values.astype(str)
            cos_850_grade_category = dataset.iloc[:, 11:12].values.astype(str)
            selected_area_of_specialization_from_form += "cn"
            return redirect(url_for('elective_course.timer_cn'))
        elif form.user_type.data == 'se':
            dataset = pd.read_csv('models/Prediction/dataset/software_engineering_courses_scores.csv')
            bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
            dataset["COS821 Bins"] = pd.cut(dataset['COS821 SCORE'], bins=bins)
            dataset["COS827 Bins"] = pd.cut(dataset['COS827 SCORE'], bins=bins)
            dataset["COS814 Bins"] = pd.cut(dataset['COS814 SCORE'], bins=bins)
            dataset["COS820 Bins"] = pd.cut(dataset['COS820 SCORE'], bins=bins)
            cos_821_total_student = dataset.iloc[:, :1].values.astype(str)
            cos_821_grade_category = dataset.iloc[:, 8:9].values.astype(str)
            cos_827_total_student = dataset.iloc[:, 2:3].values.astype(str)
            cos_827_grade_category = dataset.iloc[:, 9:10].values.astype(str)
            cos_814_total_student = dataset.iloc[:, 4:5].values.astype(str)
            cos_814_grade_category = dataset.iloc[:, 10:11].values.astype(str)
            cos_820_total_student = dataset.iloc[:, 6:7].values.astype(str)
            cos_820_grade_category = dataset.iloc[:, 11:12].values.astype(str)
            selected_area_of_specialization_from_form += "se"
            return redirect(url_for('elective_course.timer_se'))
        elif form.user_type.data == 'sye':
            dataset = pd.read_csv('models/Prediction/dataset/system_engineering_courses_scores.csv')
            bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
            dataset["COS815 Bins"] = pd.cut(dataset['COS815 SCORE'], bins=bins)
            dataset["COS823 Bins"] = pd.cut(dataset['COS823 SCORE'], bins=bins)
            dataset["COS817 Bins"] = pd.cut(dataset['COS817 SCORE'], bins=bins)
            dataset["COS810 Bins"] = pd.cut(dataset['COS810 SCORE'], bins=bins)
            dataset["COS812 Bins"] = pd.cut(dataset['COS812 SCORE'], bins=bins)
            cos_815_total_student = dataset.iloc[:, :1].values.astype(str)
            cos_815_grade_category = dataset.iloc[:, 10:11].values.astype(str)
            cos_823_total_student = dataset.iloc[:, 2:3].values.astype(str)
            cos_823_grade_category = dataset.iloc[:, 11:12].values.astype(str)
            cos_817_total_student = dataset.iloc[:, 4:5].values.astype(str)
            cos_817_grade_category = dataset.iloc[:, 12:13].values.astype(str)
            cos_810_total_student = dataset.iloc[:, 6:7].values.astype(str)
            cos_810_grade_category = dataset.iloc[:, 13:14].values.astype(str)
            cos_812_total_student = dataset.iloc[:, 8:9].values.astype(str)
            cos_812_grade_category = dataset.iloc[:, 14:15].values.astype(str)
            selected_area_of_specialization_from_form += "sye"
            return redirect(url_for('elective_course.timer_sye'))
        else:
            return redirect(url_for('elective_course.index'))
    image_file = url_for('static', filename='assets/pictures/' + current_user.default_image)
    decorators.selected_aos = selected_area_of_specialization_from_form
    return render_template('questions/elective_courses/select_course.html', image_file=image_file, form=form)


@elective_course.route('/ai-elective-questions', methods=['GET', 'POST'])
@login_required
@elective_question_info_page
def timer():
    global rounds
    global current_number
    global answers
    global cos_833_correct
    global cos_833_failed
    global cos_816_correct
    global cos_816_failed
    global cos_830_correct
    global cos_830_failed
    global cos_836_correct
    global cos_836_failed
    global cos_834_correct
    global cos_834_failed
    global cos_838_correct
    global cos_838_failed
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
    global question_tracking
    global new_sorted_dict
    global new_sorted_list_from_dict
    global switch

    form = QuestionForm()
    question_to_ask = ''
    a = ""
    b = ""
    c = ""
    final_scores = []

    if session["elective_courses_question"] == '0':
        rounds = 0
        current_number = 1
        cos_833_correct = 0
        cos_833_failed = 0
        cos_816_correct = 0
        cos_816_failed = 0
        cos_830_correct = 0
        cos_830_failed = 0
        cos_836_correct = 0
        cos_836_failed = 0
        cos_834_correct = 0
        cos_834_failed = 0
        cos_838_correct = 0
        cos_838_failed = 0
        total_correct = 0
        total_failed = 0
        session_count = 1
        selected_courses = ""
        user_response = "got_1"
        next_question = "Next Question"
        session_dict = OrderedDict()
        question_tracking = 0
        new_sorted_dict = dict()
        new_sorted_list_from_dict = list()

        # The first time the page is loaded, the current question is not set.
        # This means that the user has not started to quiz yet. So set the
        # current question to question 1 and save it in the session.
        session["elective_courses_question"] = '1'
        back_val = False
        switch = False
    current_q = ai_total_questions_and_answer[session["elective_courses_question"]][rounds]
    question_tuple = tuple(current_q.items())
    for question_posted in question_tuple:
        questions, answers = question_posted
        questions = questions.split()
        question_to_ask = " ".join(questions[:questions.index('(A)')])
        question_split = questions[questions.index('(A)'):]
        a = " ".join(question_split[:question_split.index('(B)')])
        b = " ".join(question_split[question_split.index('(B)'):question_split.index('(C)')])
        c = " ".join(question_split[question_split.index('(C)'):])
        # request.form['answer_option'] = current_answer
    form.question_option.choices = [("A", a), ("B", b), ("C", c)]
    form.process()

    if request.method == 'POST':
        question_tracking += 1
        current_answer = request.form.get('answer_option', '')
        session_dict.update({question_tracking:
                                 [ai_total_questions_and_answer[session["elective_courses_question"]][rounds],
                                  answers,
                                  current_answer]})
        if not current_answer:
            current_number += 1
            rounds += 1
            back_val = True
            if rounds == 6:
                rounds = 0
                session["elective_courses_question"] = str(int(session["elective_courses_question"]) + 1)

                # submit
                if session["elective_courses_question"] == '6' and rounds == 0:
                    switch = False
                    saved_model = joblib.load("models/Prediction/saved_model/mark_category")
                    session["elective_finished"] = "yes"
                    selected_courses_list = []
                    session.pop("elective_courses_question")
                    # session["elective_courses_question"]
                    rounds = 0
                    current_number = 1
                    if cos_833_correct == 0 and cos_816_correct == 0 and cos_830_correct == 0 and cos_836_correct == \
                            0 and cos_834_correct == 0 and cos_838_correct == 0:
                        user_response = "No Elective Course can be selected"
                        selected_courses = "None"
                    else:
                        new_list = [("COS833", cos_833_correct), ("COS816", cos_816_correct),
                                    ("COS830", cos_830_correct), ("COS836", cos_836_correct),
                                    ("COS834", cos_834_correct), ("COS838", cos_838_correct)]
                        new_dict = dict(new_list)
                        for key, value in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True):
                            new_sorted_dict.update({key: value})
                            new_sorted_list_from_dict.append(new_sorted_dict)
                            new_sorted_dict = dict()

                        chck_list = []
                        chck_list_keys = []
                        chck_dict = dict()
                        chck_list_dict = []
                        ranked_list = []
                        for i in new_sorted_list_from_dict:
                            for j, k in i.items():
                                chck_list.append(k)
                                chck_list_keys.append(j)

                        max_val = max(chck_list)
                        inc = 1
                        for i in range(len(chck_list) - 1):
                            if chck_list[i] == chck_list[i + 1] and chck_list[i] == max_val:
                                inc += 1

                        filtered_dict = dict()
                        filtered_list_dict = list()
                        if inc > 2:
                            for i, j in enumerate(chck_list):
                                if j == max_val:
                                    chck_dict.update({chck_list_keys[i]: j})
                                    chck_list_dict.append(chck_dict)
                                    chck_dict = dict()
                            predicted_outcome_to_be_ranked = predict_from_ranges(chck_list_dict, saved_model)
                            for i in predicted_outcome_to_be_ranked:
                                for j, k in i.items():
                                    for l in k:
                                        if j == 'COS833':
                                            calculated_outcome = calculated_ranking(l[1], cos_833_total_student,
                                                                                    cos_833_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS816':
                                            calculated_outcome = calculated_ranking(l[1], cos_816_total_student,
                                                                                    cos_816_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS830':
                                            calculated_outcome = calculated_ranking(l[1], cos_830_total_student,
                                                                                    cos_830_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS836':
                                            calculated_outcome = calculated_ranking(l[1], cos_836_total_student,
                                                                                    cos_836_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS834':
                                            calculated_outcome = calculated_ranking(l[1], cos_834_total_student,
                                                                                    cos_834_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS838':
                                            calculated_outcome = calculated_ranking(l[1], cos_838_total_student,
                                                                                    cos_838_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                            filtered_dict = dict(filtered_list_dict)
                            chck_list_keys = []
                            chck_list = []
                            chck_list_dict = []
                            for key, value in sorted(filtered_dict.items(), key=lambda item: (item[1], item[0])):
                                chck_list_keys.append(key)
                                chck_list.append(value)
                            for i, j in enumerate(chck_list_keys[:2]):
                                chck_dict.update({j: chck_list[i]})
                                chck_list_dict.append(chck_dict)
                                chck_dict = dict()
                            for i in chck_list_dict:
                                for j in i:
                                    selected_courses_list.append(j)
                        else:
                            for i, j in enumerate(chck_list_keys[:2]):
                                chck_dict.update({j: chck_list[i]})
                                chck_list_dict.append(chck_dict)
                                chck_dict = dict()
                            chck_list_dict = predict_from_ranges(chck_list_dict, saved_model)
                            for i in chck_list_dict:
                                for j in i:
                                    selected_courses_list.append(j)
                        selected_courses = ", ".join(selected_courses_list)
                    return redirect(url_for('elective_course.submit'))

            # Last question to ask
            if session["elective_courses_question"] == '5' and rounds == 5:
                switch = True
                next_question = "Submit"
                return redirect(url_for('elective_course.timer'))
            if session["elective_courses_question"] in ai_total_questions_and_answer:
                # If the question exists in the dictionary, redirect to the question
                #
                return redirect(url_for('elective_course.timer'))
        else:
            current_answer = request.form['answer_option']

            if cos_833_selected_six_random[int(session["elective_courses_question"]) - 1] == \
                    session_dict[question_tracking][0]:
                current_number += 1
                rounds += 1
                if current_answer == session_dict[question_tracking][1]:
                    cos_833_correct += 1
                    total_correct += 1
                else:
                    cos_833_failed += 1
                    total_failed += 1
            elif cos_816_selected_six_random[int(session["elective_courses_question"]) - 1] == \
                    session_dict[question_tracking][0]:
                current_number += 1
                rounds += 1
                if current_answer == session_dict[question_tracking][1]:
                    cos_816_correct += 1
                    total_correct += 1
                else:
                    cos_816_failed += 1
                    total_failed += 1
            elif cos_830_selected_six_random[int(session["elective_courses_question"]) - 1] == \
                    session_dict[question_tracking][0]:
                current_number += 1
                rounds += 1
                if current_answer == session_dict[question_tracking][1]:
                    cos_830_correct += 1
                    total_correct += 1
                else:
                    cos_830_failed += 1
                    total_failed += 1
            elif cos_836_selected_six_random[int(session["elective_courses_question"]) - 1] == \
                    session_dict[question_tracking][0]:
                current_number += 1
                rounds += 1
                if current_answer == session_dict[question_tracking][1]:
                    cos_836_correct += 1
                    total_correct += 1
                else:
                    cos_836_failed += 1
                    total_failed += 1
            elif cos_834_selected_six_random[int(session["elective_courses_question"]) - 1] == \
                    session_dict[question_tracking][0]:
                current_number += 1
                rounds += 1
                if current_answer == session_dict[question_tracking][1]:
                    cos_834_correct += 1
                    total_correct += 1
                else:
                    cos_834_failed += 1
                    total_failed += 1

            elif cos_838_selected_six_random[int(session["elective_courses_question"]) - 1] == \
                    session_dict[question_tracking][0]:
                current_number += 1
                rounds += 1
                if current_answer == session_dict[question_tracking][1]:
                    cos_838_correct += 1
                    total_correct += 1
                else:
                    cos_838_failed += 1
                    total_failed += 1

            if rounds == 6:
                rounds = 0
                main_question_umbrella = 1
                session["elective_courses_question"] = str(int(session["elective_courses_question"]) + 1)
                main_question_umbrella += 1
                switch = False

                # submit
                if session["elective_courses_question"] == '6' and rounds == 0:
                    saved_model = joblib.load("models/Prediction/saved_model/mark_category")
                    session["elective_finished"] = "yes"
                    selected_courses = ""
                    user_response = "got_1"
                    selected_courses_list = []
                    session.pop("elective_courses_question")
                    # session["elective_courses_question"]
                    rounds = 0
                    current_number = 1
                    if cos_833_correct == 0 and cos_816_correct == 0 and cos_830_correct == 0 and cos_836_correct == \
                            0 and cos_834_correct == 0 and cos_838_correct == 0:
                        user_response = "No Elective Course can be selected"
                    else:
                        new_list = [("COS833", cos_833_correct), ("COS816", cos_816_correct),
                                    ("COS830", cos_830_correct), ("COS836", cos_836_correct),
                                    ("COS834", cos_834_correct), ("COS838", cos_838_correct)]
                        new_dict = dict(new_list)
                        for key, value in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True):
                            new_sorted_dict.update({key: value})
                            new_sorted_list_from_dict.append(new_sorted_dict)
                            new_sorted_dict = dict()

                        chck_list = []
                        chck_list_keys = []
                        chck_dict = dict()
                        chck_list_dict = []
                        ranked_list = []
                        for i in new_sorted_list_from_dict:
                            for j, k in i.items():
                                chck_list.append(k)
                                chck_list_keys.append(j)

                        max_val = max(chck_list)
                        inc = 1
                        for i in range(len(chck_list) - 1):
                            if chck_list[i] == chck_list[i + 1] and chck_list[i] == max_val:
                                inc += 1

                        filtered_dict = dict()
                        filtered_list_dict = list()
                        if inc > 2:
                            for i, j in enumerate(chck_list):
                                if j == max_val:
                                    chck_dict.update({chck_list_keys[i]: j})
                                    chck_list_dict.append(chck_dict)
                                    chck_dict = dict()
                            predicted_outcome_to_be_ranked = predict_from_ranges(chck_list_dict, saved_model)
                            for i in predicted_outcome_to_be_ranked:
                                for j, k in i.items():
                                    for l in k:
                                        if j == 'COS833':
                                            calculated_outcome = calculated_ranking(l[1], cos_833_total_student,
                                                                                    cos_833_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS816':
                                            calculated_outcome = calculated_ranking(l[1], cos_816_total_student,
                                                                                    cos_816_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS830':
                                            calculated_outcome = calculated_ranking(l[1], cos_830_total_student,
                                                                                    cos_830_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS836':
                                            calculated_outcome = calculated_ranking(l[1], cos_836_total_student,
                                                                                    cos_836_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS834':
                                            calculated_outcome = calculated_ranking(l[1], cos_834_total_student,
                                                                                    cos_834_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS838':
                                            calculated_outcome = calculated_ranking(l[1], cos_838_total_student,
                                                                                    cos_838_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                            filtered_dict = dict(filtered_list_dict)
                            chck_list_keys = []
                            chck_list = []
                            chck_list_dict = []
                            for key, value in sorted(filtered_dict.items(), key=lambda item: (item[1], item[0])):
                                chck_list_keys.append(key)
                                chck_list.append(value)
                            for i, j in enumerate(chck_list_keys[:2]):
                                chck_dict.update({j: chck_list[i]})
                                chck_list_dict.append(chck_dict)
                                chck_dict = dict()
                            for i in chck_list_dict:
                                for j in i:
                                    selected_courses_list.append(j)
                        else:
                            for i, j in enumerate(chck_list_keys[:2]):
                                chck_dict.update({j: chck_list[i]})
                                chck_list_dict.append(chck_dict)
                                chck_dict = dict()
                            chck_list_dict = predict_from_ranges(chck_list_dict, saved_model)
                            for i in chck_list_dict:
                                for j in i:
                                    selected_courses_list.append(j)
                        selected_courses = ", ".join(selected_courses_list)
                    return redirect(url_for('elective_course.submit'))
            if rounds >= 0 and int(session["elective_courses_question"]) > 1:
                back_val = True
            if rounds > 0 and int(session["elective_courses_question"]) == 1:
                back_val = True

            # Last question to answer
            if session["elective_courses_question"] == '5' and rounds == 5:
                next_question = "Submit"
                switch = True
            #     return redirect(url_for('elective_course.timer'))
            if session["elective_courses_question"] in ai_total_questions_and_answer:
                # If the question exists in the dictionary, redirect to the question
                #
                return redirect(url_for('elective_course.timer'))

            session_count = int(session_count['elective_courses_question'])

    return render_template('questions/elective_courses/elective_ai_questions.html', num_counter=counting_down,
                           switch=switch,
                           num=current_number, next_question=next_question, back_val=back_val,
                           ntot=ai_total_questions,
                           question=question_to_ask,
                           ans1=a,
                           ans2=b,
                           ans3=c,
                           selected_area_of_specialization_from_form=selected_area_of_specialization_from_form,
                           form=form)


@elective_course.route('/cn-elective-questions', methods=['GET', 'POST'])
@login_required
@elective_question_info_page
def timer_cn():
    global rounds
    global current_number
    global answers
    global cos_845_correct
    global cos_845_failed
    global cos_829_correct
    global cos_829_failed
    global cos_852_correct
    global cos_852_failed
    global cos_850_correct
    global cos_850_failed
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
    global question_tracking
    global new_sorted_dict
    global new_sorted_list_from_dict
    global switch

    form = QuestionForm()
    question_to_ask = ''
    a = ""
    b = ""
    c = ""
    final_scores = []

    if session["elective_courses_question"] == '0':
        rounds = 0
        current_number = 1
        cos_845_correct = 0
        cos_845_failed = 0
        cos_829_correct = 0
        cos_829_failed = 0
        cos_852_correct = 0
        cos_852_failed = 0
        cos_850_correct = 0
        cos_850_failed = 0
        total_correct = 0
        total_failed = 0
        session_count = 1
        selected_courses = ""
        user_response = "got_1"
        next_question = "Next Question"
        session_dict = OrderedDict()
        question_tracking = 0
        new_sorted_dict = dict()
        new_sorted_list_from_dict = list()

        # The first time the page is loaded, the current question is not set.
        # This means that the user has not started to quiz yet. So set the
        # current question to question 1 and save it in the session.
        session["elective_courses_question"] = '1'
        back_val = False
        switch = False
    current_q = cn_total_questions_and_answer[session["elective_courses_question"]][rounds]
    question_tuple = tuple(current_q.items())
    for question_posted in question_tuple:
        questions, answers = question_posted
        questions = questions.split()
        question_to_ask = " ".join(questions[:questions.index('(A)')])
        question_split = questions[questions.index('(A)'):]
        a = " ".join(question_split[:question_split.index('(B)')])
        b = " ".join(question_split[question_split.index('(B)'):question_split.index('(C)')])
        c = " ".join(question_split[question_split.index('(C)'):])
        # request.form['answer_option'] = current_answer
    form.question_option.choices = [("A", a), ("B", b), ("C", c)]
    form.process()

    if request.method == 'POST':
        question_tracking += 1
        current_answer = request.form.get('answer_option', '')
        session_dict.update({question_tracking:
                                 [cn_total_questions_and_answer[session["elective_courses_question"]][rounds],
                                  answers,
                                  current_answer]})
        if not current_answer:
            current_number += 1
            rounds += 1
            back_val = True
            if rounds == 4:
                rounds = 0
                session["elective_courses_question"] = str(int(session["elective_courses_question"]) + 1)

                # submit
                if session["elective_courses_question"] == '6' and rounds == 0:
                    switch = False
                    saved_model = joblib.load("models/Prediction/saved_model/mark_category")
                    session["elective_finished"] = "yes"
                    selected_courses_list = []
                    session.pop("elective_courses_question")
                    # session["elective_courses_question"]
                    rounds = 0
                    current_number = 1
                    if cos_845_correct == 0 and cos_829_correct == 0 and cos_852_correct == 0 and cos_850_correct == \
                            0:
                        user_response = "No Elective Course can be selected"
                        selected_courses = "None"
                    else:
                        new_list = [("COS845", cos_845_correct), ("COS829", cos_829_correct),
                                    ("COS852", cos_852_correct), ("COS850", cos_850_correct)]
                        new_dict = dict(new_list)
                        for key, value in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True):
                            new_sorted_dict.update({key: value})
                            new_sorted_list_from_dict.append(new_sorted_dict)
                            new_sorted_dict = dict()

                        chck_list = []
                        chck_list_keys = []
                        chck_dict = dict()
                        chck_list_dict = []
                        ranked_list = []
                        for i in new_sorted_list_from_dict:
                            for j, k in i.items():
                                chck_list.append(k)
                                chck_list_keys.append(j)

                        max_val = max(chck_list)
                        inc = 1
                        for i in range(len(chck_list) - 1):
                            if chck_list[i] == chck_list[i + 1] and chck_list[i] == max_val:
                                inc += 1

                        filtered_dict = dict()
                        filtered_list_dict = list()
                        if inc > 2:
                            for i, j in enumerate(chck_list):
                                if j == max_val:
                                    chck_dict.update({chck_list_keys[i]: j})
                                    chck_list_dict.append(chck_dict)
                                    chck_dict = dict()
                            predicted_outcome_to_be_ranked = predict_from_ranges(chck_list_dict, saved_model)
                            for i in predicted_outcome_to_be_ranked:
                                for j, k in i.items():
                                    for l in k:
                                        if j == 'COS845':
                                            calculated_outcome = calculated_ranking(l[1], cos_845_total_student,
                                                                                    cos_845_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS829':
                                            calculated_outcome = calculated_ranking(l[1], cos_829_total_student,
                                                                                    cos_829_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS852':
                                            calculated_outcome = calculated_ranking(l[1], cos_852_total_student,
                                                                                    cos_852_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS850':
                                            calculated_outcome = calculated_ranking(l[1], cos_850_total_student,
                                                                                    cos_850_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                            filtered_dict = dict(filtered_list_dict)
                            chck_list_keys = []
                            chck_list = []
                            chck_list_dict = []
                            for key, value in sorted(filtered_dict.items(), key=lambda item: (item[1], item[0])):
                                chck_list_keys.append(key)
                                chck_list.append(value)
                            for i, j in enumerate(chck_list_keys[:2]):
                                chck_dict.update({j: chck_list[i]})
                                chck_list_dict.append(chck_dict)
                                chck_dict = dict()
                            for i in chck_list_dict:
                                for j in i:
                                    selected_courses_list.append(j)
                        else:
                            for i, j in enumerate(chck_list_keys[:2]):
                                chck_dict.update({j: chck_list[i]})
                                chck_list_dict.append(chck_dict)
                                chck_dict = dict()
                            chck_list_dict = predict_from_ranges(chck_list_dict, saved_model)
                            for i in chck_list_dict:
                                for j in i:
                                    selected_courses_list.append(j)
                        selected_courses = ", ".join(selected_courses_list)
                    return redirect(url_for('elective_course.submit'))

            # Last question to ask
            if session["elective_courses_question"] == '5' and rounds == 3:
                switch = True
                next_question = "Submit"
                return redirect(url_for('elective_course.timer_cn'))
            if session["elective_courses_question"] in cn_total_questions_and_answer:
                # If the question exists in the dictionary, redirect to the question
                #
                return redirect(url_for('elective_course.timer_cn'))
        else:
            current_answer = request.form['answer_option']
            if cos_845_selected_six_random[int(session["elective_courses_question"]) - 1] == \
                    session_dict[question_tracking][0]:
                current_number += 1
                rounds += 1
                if current_answer == session_dict[question_tracking][1]:
                    cos_845_correct += 1
                    total_correct += 1
                else:
                    cos_845_failed += 1
                    total_failed += 1
            elif cos_829_selected_six_random[int(session["elective_courses_question"]) - 1] == \
                    session_dict[question_tracking][0]:
                current_number += 1
                rounds += 1
                if current_answer == session_dict[question_tracking][1]:
                    cos_829_correct += 1
                    total_correct += 1
                else:
                    cos_829_failed += 1
                    total_failed += 1
            elif cos_852_selected_six_random[int(session["elective_courses_question"]) - 1] == \
                    session_dict[question_tracking][0]:
                current_number += 1
                rounds += 1
                if current_answer == session_dict[question_tracking][1]:
                    cos_852_correct += 1
                    total_correct += 1
                else:
                    cos_852_failed += 1
                    total_failed += 1
            elif cos_850_selected_six_random[int(session["elective_courses_question"]) - 1] == \
                    session_dict[question_tracking][0]:
                current_number += 1
                rounds += 1
                if current_answer == session_dict[question_tracking][1]:
                    cos_850_correct += 1
                    total_correct += 1
                else:
                    cos_850_failed += 1
                    total_failed += 1

            if rounds == 4:
                rounds = 0
                main_question_umbrella = 1
                session["elective_courses_question"] = str(int(session["elective_courses_question"]) + 1)
                main_question_umbrella += 1

                # submit
                if session["elective_courses_question"] == '6' and rounds == 0:
                    switch = False
                    saved_model = joblib.load("models/Prediction/saved_model/mark_category")
                    session["elective_finished"] = "yes"
                    selected_courses = ""
                    user_response = "got_1"
                    selected_courses_list = []
                    session.pop("elective_courses_question")
                    # session["elective_courses_question"]
                    rounds = 0
                    current_number = 1
                    if cos_845_correct == 0 and cos_829_correct == 0 and cos_852_correct == 0 and cos_850_correct == 0:
                        user_response = "No Elective Course can be selected"
                    else:
                        new_list = [("COS845", cos_845_correct), ("COS829", cos_829_correct),
                                    ("COS852", cos_852_correct), ("COS850", cos_850_correct)]
                        new_dict = dict(new_list)
                        for key, value in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True):
                            new_sorted_dict.update({key: value})
                            new_sorted_list_from_dict.append(new_sorted_dict)
                            new_sorted_dict = dict()

                        chck_list = []
                        chck_list_keys = []
                        chck_dict = dict()
                        chck_list_dict = []
                        ranked_list = []
                        for i in new_sorted_list_from_dict:
                            for j, k in i.items():
                                chck_list.append(k)
                                chck_list_keys.append(j)

                        max_val = max(chck_list)
                        inc = 1
                        for i in range(len(chck_list) - 1):
                            if chck_list[i] == chck_list[i + 1] and chck_list[i] == max_val:
                                inc += 1

                        filtered_dict = dict()
                        filtered_list_dict = list()
                        if inc > 2:
                            for i, j in enumerate(chck_list):
                                if j == max_val:
                                    chck_dict.update({chck_list_keys[i]: j})
                                    chck_list_dict.append(chck_dict)
                                    chck_dict = dict()
                            predicted_outcome_to_be_ranked = predict_from_ranges(chck_list_dict, saved_model)
                            for i in predicted_outcome_to_be_ranked:
                                for j, k in i.items():
                                    for l in k:
                                        if j == 'COS845':
                                            calculated_outcome = calculated_ranking(l[1], cos_845_total_student,
                                                                                    cos_845_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS829':
                                            calculated_outcome = calculated_ranking(l[1], cos_829_total_student,
                                                                                    cos_829_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS852':
                                            calculated_outcome = calculated_ranking(l[1], cos_852_total_student,
                                                                                    cos_852_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS850':
                                            calculated_outcome = calculated_ranking(l[1], cos_850_total_student,
                                                                                    cos_850_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                            filtered_dict = dict(filtered_list_dict)
                            chck_list_keys = []
                            chck_list = []
                            chck_list_dict = []
                            for key, value in sorted(filtered_dict.items(), key=lambda item: (item[1], item[0])):
                                chck_list_keys.append(key)
                                chck_list.append(value)
                            for i, j in enumerate(chck_list_keys[:2]):
                                chck_dict.update({j: chck_list[i]})
                                chck_list_dict.append(chck_dict)
                                chck_dict = dict()
                            for i in chck_list_dict:
                                for j in i:
                                    selected_courses_list.append(j)
                        else:
                            for i, j in enumerate(chck_list_keys[:2]):
                                chck_dict.update({j: chck_list[i]})
                                chck_list_dict.append(chck_dict)
                                chck_dict = dict()
                            chck_list_dict = predict_from_ranges(chck_list_dict, saved_model)
                            for i in chck_list_dict:
                                for j in i:
                                    selected_courses_list.append(j)
                        selected_courses = ", ".join(selected_courses_list)
                    return redirect(url_for('elective_course.submit'))
            if rounds >= 0 and int(session["elective_courses_question"]) > 1:
                back_val = True
            if rounds > 0 and int(session["elective_courses_question"]) == 1:
                back_val = True

            # Last question to answer
            if session["elective_courses_question"] == '5' and rounds == 3:
                next_question = "Submit"
                switch = True
            #     return redirect(url_for('elective_course.timer'))
            if session["elective_courses_question"] in cn_total_questions_and_answer:
                # If the question exists in the dictionary, redirect to the question
                #
                return redirect(url_for('elective_course.timer_cn'))

            session_count = int(session_count['elective_courses_question'])

    return render_template('questions/elective_courses/elective_cn_questions.html', num_counter=counting_down,
                           switch=switch,
                           num=current_number, next_question=next_question, back_val=back_val,
                           ntot=cn_total_questions,
                           question=question_to_ask,
                           ans1=a,
                           ans2=b,
                           ans3=c,
                           selected_area_of_specialization_from_form=selected_area_of_specialization_from_form,
                           form=form)


@elective_course.route('/se-elective-questions', methods=['GET', 'POST'])
@login_required
@elective_question_info_page
def timer_se():
    global rounds
    global current_number
    global answers
    global cos_821_correct
    global cos_821_failed
    global cos_827_correct
    global cos_827_failed
    global cos_814_correct
    global cos_814_failed
    global cos_820_correct
    global cos_820_failed
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
    global question_tracking
    global new_sorted_dict
    global new_sorted_list_from_dict
    global switch

    form = QuestionForm()
    question_to_ask = ''
    a = ""
    b = ""
    c = ""
    final_scores = []

    if session["elective_courses_question"] == '0':
        rounds = 0
        current_number = 1
        cos_821_correct = 0
        cos_821_failed = 0
        cos_827_correct = 0
        cos_827_failed = 0
        cos_814_correct = 0
        cos_814_failed = 0
        cos_820_correct = 0
        cos_820_failed = 0
        total_correct = 0
        total_failed = 0
        session_count = 1
        selected_courses = ""
        user_response = "got_1"
        next_question = "Next Question"
        session_dict = OrderedDict()
        question_tracking = 0
        new_sorted_dict = dict()
        new_sorted_list_from_dict = list()

        # The first time the page is loaded, the current question is not set.
        # This means that the user has not started to quiz yet. So set the
        # current question to question 1 and save it in the session.
        session["elective_courses_question"] = '1'
        back_val = False
        switch = False
    current_q = soe_total_questions_and_answer[session["elective_courses_question"]][rounds]
    question_tuple = tuple(current_q.items())
    for question_posted in question_tuple:
        questions, answers = question_posted
        questions = questions.split()
        question_to_ask = " ".join(questions[:questions.index('(A)')])
        question_split = questions[questions.index('(A)'):]
        a = " ".join(question_split[:question_split.index('(B)')])
        b = " ".join(question_split[question_split.index('(B)'):question_split.index('(C)')])
        c = " ".join(question_split[question_split.index('(C)'):])
        # request.form['answer_option'] = current_answer
    form.question_option.choices = [("A", a), ("B", b), ("C", c)]
    form.process()

    if request.method == 'POST':
        question_tracking += 1
        current_answer = request.form.get('answer_option', '')
        session_dict.update({question_tracking:
                                 [soe_total_questions_and_answer[session["elective_courses_question"]][rounds],
                                  answers,
                                  current_answer]})
        if not current_answer:
            current_number += 1
            rounds += 1
            back_val = True
            if rounds == 4:
                rounds = 0
                session["elective_courses_question"] = str(int(session["elective_courses_question"]) + 1)

                # submit
                if session["elective_courses_question"] == '6' and rounds == 0:
                    switch = False
                    saved_model = joblib.load("models/Prediction/saved_model/mark_category")
                    session["elective_finished"] = "yes"
                    selected_courses_list = []
                    session.pop("elective_courses_question")
                    # session["elective_courses_question"]
                    rounds = 0
                    current_number = 1
                    if cos_821_correct == 0 and cos_827_correct == 0 and cos_814_correct == 0 and cos_820_correct == 0:
                        user_response = "No Elective Course can be selected"
                        selected_courses = "None"
                    else:
                        new_list = [("COS821", cos_821_correct), ("COS814", cos_814_correct),
                                    ("COS827", cos_827_correct), ("COS820", cos_820_correct)]
                        new_dict = dict(new_list)
                        for key, value in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True):
                            new_sorted_dict.update({key: value})
                            new_sorted_list_from_dict.append(new_sorted_dict)
                            new_sorted_dict = dict()

                        chck_list = []
                        chck_list_keys = []
                        chck_dict = dict()
                        chck_list_dict = []
                        ranked_list = []
                        for i in new_sorted_list_from_dict:
                            for j, k in i.items():
                                chck_list.append(k)
                                chck_list_keys.append(j)

                        max_val = max(chck_list)
                        inc = 1
                        for i in range(len(chck_list) - 1):
                            if chck_list[i] == chck_list[i + 1] and chck_list[i] == max_val:
                                inc += 1

                        filtered_dict = dict()
                        filtered_list_dict = list()
                        if inc > 2:
                            for i, j in enumerate(chck_list):
                                if j == max_val:
                                    chck_dict.update({chck_list_keys[i]: j})
                                    chck_list_dict.append(chck_dict)
                                    chck_dict = dict()
                            predicted_outcome_to_be_ranked = predict_from_ranges(chck_list_dict, saved_model)
                            for i in predicted_outcome_to_be_ranked:
                                for j, k in i.items():
                                    for l in k:
                                        if j == 'COS821':
                                            calculated_outcome = calculated_ranking(l[1], cos_821_total_student,
                                                                                    cos_821_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS827':
                                            calculated_outcome = calculated_ranking(l[1], cos_827_total_student,
                                                                                    cos_827_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS814':
                                            calculated_outcome = calculated_ranking(l[1], cos_814_total_student,
                                                                                    cos_814_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS820':
                                            calculated_outcome = calculated_ranking(l[1], cos_820_total_student,
                                                                                    cos_820_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                            filtered_dict = dict(filtered_list_dict)
                            chck_list_keys = []
                            chck_list = []
                            chck_list_dict = []
                            for key, value in sorted(filtered_dict.items(), key=lambda item: (item[1], item[0])):
                                chck_list_keys.append(key)
                                chck_list.append(value)
                            for i, j in enumerate(chck_list_keys[:2]):
                                chck_dict.update({j: chck_list[i]})
                                chck_list_dict.append(chck_dict)
                                chck_dict = dict()
                            for i in chck_list_dict:
                                for j in i:
                                    selected_courses_list.append(j)
                        else:
                            for i, j in enumerate(chck_list_keys[:2]):
                                chck_dict.update({j: chck_list[i]})
                                chck_list_dict.append(chck_dict)
                                chck_dict = dict()
                            chck_list_dict = predict_from_ranges(chck_list_dict, saved_model)
                            for i in chck_list_dict:
                                for j in i:
                                    selected_courses_list.append(j)
                        selected_courses = ", ".join(selected_courses_list)
                    return redirect(url_for('elective_course.submit'))

            # Last question to ask
            if session["elective_courses_question"] == '5' and rounds == 3:
                switch = True
                next_question = "Submit"
                return redirect(url_for('elective_course.timer_se'))
            if session["elective_courses_question"] in soe_total_questions_and_answer:
                # If the question exists in the dictionary, redirect to the question
                #
                return redirect(url_for('elective_course.timer_se'))
        else:
            current_answer = request.form['answer_option']
            if cos_821_selected_six_random[int(session["elective_courses_question"]) - 1] == \
                    session_dict[question_tracking][0]:
                current_number += 1
                rounds += 1
                if current_answer == session_dict[question_tracking][1]:
                    cos_821_correct += 1
                    total_correct += 1
                else:
                    cos_821_failed += 1
                    total_failed += 1
            elif cos_827_selected_six_random[int(session["elective_courses_question"]) - 1] == \
                    session_dict[question_tracking][0]:
                current_number += 1
                rounds += 1
                if current_answer == session_dict[question_tracking][1]:
                    cos_827_correct += 1
                    total_correct += 1
                else:
                    cos_827_failed += 1
                    total_failed += 1
            elif cos_814_selected_six_random[int(session["elective_courses_question"]) - 1] == \
                    session_dict[question_tracking][0]:
                current_number += 1
                rounds += 1
                if current_answer == session_dict[question_tracking][1]:
                    cos_814_correct += 1
                    total_correct += 1
                else:
                    cos_814_failed += 1
                    total_failed += 1
            elif cos_820_selected_six_random[int(session["elective_courses_question"]) - 1] == \
                    session_dict[question_tracking][0]:
                current_number += 1
                rounds += 1
                if current_answer == session_dict[question_tracking][1]:
                    cos_820_correct += 1
                    total_correct += 1
                else:
                    cos_820_failed += 1
                    total_failed += 1

            if rounds == 4:
                rounds = 0
                main_question_umbrella = 1
                session["elective_courses_question"] = str(int(session["elective_courses_question"]) + 1)
                main_question_umbrella += 1

                # submit
                if session["elective_courses_question"] == '6' and rounds == 0:
                    switch = False
                    saved_model = joblib.load("models/Prediction/saved_model/mark_category")
                    session["elective_finished"] = "yes"
                    selected_courses = ""
                    user_response = "got_1"
                    selected_courses_list = []
                    session.pop("elective_courses_question")
                    # session["elective_courses_question"]
                    rounds = 0
                    current_number = 1
                    if cos_821_correct == 0 and cos_827_correct == 0 and cos_814_correct == 0 and cos_820_correct == 0:
                        user_response = "No Elective Course can be selected"
                    else:
                        new_list = [("COS821", cos_821_correct), ("COS814", cos_814_correct),
                                    ("COS827", cos_827_correct), ("COS820", cos_820_correct)]
                        new_dict = dict(new_list)
                        for key, value in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True):
                            new_sorted_dict.update({key: value})
                            new_sorted_list_from_dict.append(new_sorted_dict)
                            new_sorted_dict = dict()

                        chck_list = []
                        chck_list_keys = []
                        chck_dict = dict()
                        chck_list_dict = []
                        ranked_list = []
                        for i in new_sorted_list_from_dict:
                            for j, k in i.items():
                                chck_list.append(k)
                                chck_list_keys.append(j)

                        max_val = max(chck_list)
                        inc = 1
                        for i in range(len(chck_list) - 1):
                            if chck_list[i] == chck_list[i + 1] and chck_list[i] == max_val:
                                inc += 1

                        filtered_dict = dict()
                        filtered_list_dict = list()
                        if inc > 2:
                            for i, j in enumerate(chck_list):
                                if j == max_val:
                                    chck_dict.update({chck_list_keys[i]: j})
                                    chck_list_dict.append(chck_dict)
                                    chck_dict = dict()
                            predicted_outcome_to_be_ranked = predict_from_ranges(chck_list_dict, saved_model)
                            for i in predicted_outcome_to_be_ranked:
                                for j, k in i.items():
                                    for l in k:
                                        if j == 'COS821':
                                            calculated_outcome = calculated_ranking(l[1], cos_821_total_student,
                                                                                    cos_821_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS827':
                                            calculated_outcome = calculated_ranking(l[1], cos_827_total_student,
                                                                                    cos_827_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS814':
                                            calculated_outcome = calculated_ranking(l[1], cos_814_total_student,
                                                                                    cos_814_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS820':
                                            calculated_outcome = calculated_ranking(l[1], cos_820_total_student,
                                                                                    cos_820_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                            filtered_dict = dict(filtered_list_dict)
                            chck_list_keys = []
                            chck_list = []
                            chck_list_dict = []
                            for key, value in sorted(filtered_dict.items(), key=lambda item: (item[1], item[0])):
                                chck_list_keys.append(key)
                                chck_list.append(value)
                            for i, j in enumerate(chck_list_keys[:2]):
                                chck_dict.update({j: chck_list[i]})
                                chck_list_dict.append(chck_dict)
                                chck_dict = dict()
                            for i in chck_list_dict:
                                for j in i:
                                    selected_courses_list.append(j)
                        else:
                            for i, j in enumerate(chck_list_keys[:2]):
                                chck_dict.update({j: chck_list[i]})
                                chck_list_dict.append(chck_dict)
                                chck_dict = dict()
                            chck_list_dict = predict_from_ranges(chck_list_dict, saved_model)
                            for i in chck_list_dict:
                                for j in i:
                                    selected_courses_list.append(j)
                        selected_courses = ", ".join(selected_courses_list)
                    return redirect(url_for('elective_course.submit'))
            if rounds >= 0 and int(session["elective_courses_question"]) > 1:
                back_val = True
            if rounds > 0 and int(session["elective_courses_question"]) == 1:
                back_val = True

            # Last question to answer
            if session["elective_courses_question"] == '5' and rounds == 3:
                next_question = "Submit"
                switch = True
            #     return redirect(url_for('elective_course.timer'))
            if session["elective_courses_question"] in cn_total_questions_and_answer:
                # If the question exists in the dictionary, redirect to the question
                #
                return redirect(url_for('elective_course.timer_se'))

            session_count = int(session_count['elective_courses_question'])

    return render_template('questions/elective_courses/elective_soe_questions.html', num_counter=counting_down,
                           switch=switch,
                           num=current_number, next_question=next_question, back_val=back_val,
                           ntot=soe_total_questions,
                           question=question_to_ask,
                           ans1=a,
                           ans2=b,
                           ans3=c,
                           selected_area_of_specialization_from_form=selected_area_of_specialization_from_form,
                           form=form)


@elective_course.route('/sye-elective-questions', methods=['GET', 'POST'])
@login_required
@elective_question_info_page
def timer_sye():
    global rounds
    global current_number
    global answers
    global cos_815_correct
    global cos_815_failed
    global cos_823_correct
    global cos_823_failed
    global cos_817_correct
    global cos_817_failed
    global cos_810_correct
    global cos_810_failed
    global cos_812_correct
    global cos_812_failed
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
    global question_tracking
    global new_sorted_dict
    global new_sorted_list_from_dict
    global switch

    form = QuestionForm()
    question_to_ask = ''
    a = ""
    b = ""
    c = ""
    final_scores = []

    if session["elective_courses_question"] == '0':
        rounds = 0
        current_number = 1
        cos_815_correct = 0
        cos_815_failed = 0
        cos_823_correct = 0
        cos_823_failed = 0
        cos_817_correct = 0
        cos_817_failed = 0
        cos_810_correct = 0
        cos_810_failed = 0
        cos_812_correct = 0
        cos_812_failed = 0
        total_correct = 0
        total_failed = 0
        session_count = 1
        selected_courses = ""
        user_response = "got_1"
        next_question = "Next Question"
        session_dict = OrderedDict()
        question_tracking = 0
        new_sorted_dict = dict()
        new_sorted_list_from_dict = list()

        # The first time the page is loaded, the current question is not set.
        # This means that the user has not started to quiz yet. So set the
        # current question to question 1 and save it in the session.
        session["elective_courses_question"] = '1'
        back_val = False
        switch = False
    current_q = se_total_questions_and_answer[session["elective_courses_question"]][rounds]
    question_tuple = tuple(current_q.items())
    for question_posted in question_tuple:
        questions, answers = question_posted
        questions = questions.split()
        question_to_ask = " ".join(questions[:questions.index('(A)')])
        question_split = questions[questions.index('(A)'):]
        a = " ".join(question_split[:question_split.index('(B)')])
        b = " ".join(question_split[question_split.index('(B)'):question_split.index('(C)')])
        c = " ".join(question_split[question_split.index('(C)'):])
        # request.form['answer_option'] = current_answer
    form.question_option.choices = [("A", a), ("B", b), ("C", c)]
    form.process()

    if request.method == 'POST':
        question_tracking += 1
        current_answer = request.form.get('answer_option', '')
        session_dict.update({question_tracking:
                                 [se_total_questions_and_answer[session["elective_courses_question"]][rounds],
                                  answers,
                                  current_answer]})
        if not current_answer:
            current_number += 1
            rounds += 1
            back_val = True
            if rounds == 5:
                rounds = 0
                session["elective_courses_question"] = str(int(session["elective_courses_question"]) + 1)

                # submit
                if session["elective_courses_question"] == '5' and rounds == 0:
                    switch = False
                    saved_model = joblib.load("models/Prediction/saved_model/mark_category")
                    session["elective_finished"] = "yes"
                    selected_courses_list = []
                    session.pop("elective_courses_question")
                    # session["elective_courses_question"]
                    rounds = 0
                    current_number = 1
                    if cos_815_correct == 0 and cos_823_correct == 0 and cos_817_correct == 0 and cos_810_correct == \
                            0 and cos_812_correct == 0:
                        user_response = "No Elective Course can be selected"
                        selected_courses = "None"
                    else:
                        new_list = [("COS815", cos_815_correct), ("COS823", cos_823_correct),
                                    ("COS817", cos_817_correct), ("COS810", cos_810_correct),
                                    ("COS812", cos_812_correct)]
                        new_dict = dict(new_list)
                        for key, value in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True):
                            new_sorted_dict.update({key: value})
                            new_sorted_list_from_dict.append(new_sorted_dict)
                            new_sorted_dict = dict()

                        chck_list = []
                        chck_list_keys = []
                        chck_dict = dict()
                        chck_list_dict = []
                        ranked_list = []
                        for i in new_sorted_list_from_dict:
                            for j, k in i.items():
                                chck_list.append(k)
                                chck_list_keys.append(j)

                        max_val = max(chck_list)
                        inc = 1
                        for i in range(len(chck_list) - 1):
                            if chck_list[i] == chck_list[i + 1] and chck_list[i] == max_val:
                                inc += 1

                        filtered_dict = dict()
                        filtered_list_dict = list()
                        if inc > 2:
                            for i, j in enumerate(chck_list):
                                if j == max_val:
                                    chck_dict.update({chck_list_keys[i]: j})
                                    chck_list_dict.append(chck_dict)
                                    chck_dict = dict()
                            predicted_outcome_to_be_ranked = predict_from_ranges(chck_list_dict, saved_model)
                            for i in predicted_outcome_to_be_ranked:
                                for j, k in i.items():
                                    for l in k:
                                        if j == 'COS815':
                                            calculated_outcome = calculated_ranking(l[1], cos_815_total_student,
                                                                                    cos_815_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS823':
                                            calculated_outcome = calculated_ranking(l[1], cos_823_total_student,
                                                                                    cos_823_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS817':
                                            calculated_outcome = calculated_ranking(l[1], cos_817_total_student,
                                                                                    cos_817_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS810':
                                            calculated_outcome = calculated_ranking(l[1], cos_810_total_student,
                                                                                    cos_810_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS812':
                                            calculated_outcome = calculated_ranking(l[1], cos_812_total_student,
                                                                                    cos_812_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                            filtered_dict = dict(filtered_list_dict)
                            chck_list_keys = []
                            chck_list = []
                            chck_list_dict = []
                            for key, value in sorted(filtered_dict.items(), key=lambda item: (item[1], item[0])):
                                chck_list_keys.append(key)
                                chck_list.append(value)
                            for i, j in enumerate(chck_list_keys[:2]):
                                chck_dict.update({j: chck_list[i]})
                                chck_list_dict.append(chck_dict)
                                chck_dict = dict()
                            for i in chck_list_dict:
                                for j in i:
                                    selected_courses_list.append(j)
                        else:
                            for i, j in enumerate(chck_list_keys[:2]):
                                chck_dict.update({j: chck_list[i]})
                                chck_list_dict.append(chck_dict)
                                chck_dict = dict()
                            chck_list_dict = predict_from_ranges(chck_list_dict, saved_model)
                            for i in chck_list_dict:
                                for j in i:
                                    selected_courses_list.append(j)
                        selected_courses = ", ".join(selected_courses_list)
                    return redirect(url_for('elective_course.submit'))

            # Last question to ask
            if session["elective_courses_question"] == '4' and rounds == 4:
                switch = True
                next_question = "Submit"
                return redirect(url_for('elective_course.timer_sye'))
            if session["elective_courses_question"] in se_total_questions_and_answer:
                # If the question exists in the dictionary, redirect to the question
                #
                return redirect(url_for('elective_course.timer_sye'))
        else:
            current_answer = request.form['answer_option']
            if cos_815_selected_six_random[int(session["elective_courses_question"]) - 1] == \
                    session_dict[question_tracking][0]:
                current_number += 1
                rounds += 1
                if current_answer == session_dict[question_tracking][1]:
                    cos_815_correct += 1
                    total_correct += 1
                else:
                    cos_815_failed += 1
                    total_failed += 1
            elif cos_823_selected_six_random[int(session["elective_courses_question"]) - 1] == \
                    session_dict[question_tracking][0]:
                current_number += 1
                rounds += 1
                if current_answer == session_dict[question_tracking][1]:
                    cos_823_correct += 1
                    total_correct += 1
                else:
                    cos_823_failed += 1
                    total_failed += 1
            elif cos_817_selected_six_random[int(session["elective_courses_question"]) - 1] == \
                    session_dict[question_tracking][0]:
                current_number += 1
                rounds += 1
                if current_answer == session_dict[question_tracking][1]:
                    cos_817_correct += 1
                    total_correct += 1
                else:
                    cos_817_failed += 1
                    total_failed += 1
            elif cos_810_selected_six_random[int(session["elective_courses_question"]) - 1] == \
                    session_dict[question_tracking][0]:
                current_number += 1
                rounds += 1
                if current_answer == session_dict[question_tracking][1]:
                    cos_810_correct += 1
                    total_correct += 1
                else:
                    cos_810_failed += 1
                    total_failed += 1
            elif cos_812_selected_six_random[int(session["elective_courses_question"]) - 1] == \
                    session_dict[question_tracking][0]:
                current_number += 1
                rounds += 1
                if current_answer == session_dict[question_tracking][1]:
                    cos_812_correct += 1
                    total_correct += 1
                else:
                    cos_812_failed += 1
                    total_failed += 1
            if rounds == 5:
                rounds = 0
                main_question_umbrella = 1
                session["elective_courses_question"] = str(int(session["elective_courses_question"]) + 1)
                main_question_umbrella += 1

                # submit
                if session["elective_courses_question"] == '5' and rounds == 0:
                    switch = False
                    saved_model = joblib.load("models/Prediction/saved_model/mark_category")
                    session["elective_finished"] = "yes"
                    selected_courses = ""
                    user_response = "got_1"
                    selected_courses_list = []
                    session.pop("elective_courses_question")
                    # session["elective_courses_question"]
                    rounds = 0
                    current_number = 1
                    if cos_815_correct == 0 and cos_823_correct == 0 and cos_817_correct == 0 and cos_810_correct == \
                            0 and cos_812_correct == 0:
                        user_response = "No Elective Course can be selected"
                    else:
                        new_list = [("COS815", cos_815_correct), ("COS823", cos_823_correct),
                                    ("COS817", cos_817_correct), ("COS810", cos_810_correct),
                                    ("COS812", cos_812_correct)]
                        new_dict = dict(new_list)
                        for key, value in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True):
                            new_sorted_dict.update({key: value})
                            new_sorted_list_from_dict.append(new_sorted_dict)
                            new_sorted_dict = dict()

                        chck_list = []
                        chck_list_keys = []
                        chck_dict = dict()
                        chck_list_dict = []
                        ranked_list = []
                        for i in new_sorted_list_from_dict:
                            for j, k in i.items():
                                chck_list.append(k)
                                chck_list_keys.append(j)

                        max_val = max(chck_list)
                        inc = 1
                        for i in range(len(chck_list) - 1):
                            if chck_list[i] == chck_list[i + 1] and chck_list[i] == max_val:
                                inc += 1

                        filtered_dict = dict()
                        filtered_list_dict = list()
                        if inc > 2:
                            for i, j in enumerate(chck_list):
                                if j == max_val:
                                    chck_dict.update({chck_list_keys[i]: j})
                                    chck_list_dict.append(chck_dict)
                                    chck_dict = dict()
                            predicted_outcome_to_be_ranked = predict_from_ranges(chck_list_dict, saved_model)
                            for i in predicted_outcome_to_be_ranked:
                                for j, k in i.items():
                                    for l in k:
                                        if j == 'COS815':
                                            calculated_outcome = calculated_ranking(l[1], cos_815_total_student,
                                                                                    cos_815_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS823':
                                            calculated_outcome = calculated_ranking(l[1], cos_823_total_student,
                                                                                    cos_823_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS817':
                                            calculated_outcome = calculated_ranking(l[1], cos_817_total_student,
                                                                                    cos_817_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS810':
                                            calculated_outcome = calculated_ranking(l[1], cos_810_total_student,
                                                                                    cos_810_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                                        elif j == 'COS812':
                                            calculated_outcome = calculated_ranking(l[1], cos_812_total_student,
                                                                                    cos_812_grade_category)
                                            filtered_list_dict.append((j, calculated_outcome))
                            filtered_dict = dict(filtered_list_dict)
                            chck_list_keys = []
                            chck_list = []
                            chck_list_dict = []
                            for key, value in sorted(filtered_dict.items(), key=lambda item: (item[1], item[0])):
                                chck_list_keys.append(key)
                                chck_list.append(value)
                            for i, j in enumerate(chck_list_keys[:2]):
                                chck_dict.update({j: chck_list[i]})
                                chck_list_dict.append(chck_dict)
                                chck_dict = dict()
                            for i in chck_list_dict:
                                for j in i:
                                    selected_courses_list.append(j)
                        else:
                            for i, j in enumerate(chck_list_keys[:2]):
                                chck_dict.update({j: chck_list[i]})
                                chck_list_dict.append(chck_dict)
                                chck_dict = dict()
                            chck_list_dict = predict_from_ranges(chck_list_dict, saved_model)
                            for i in chck_list_dict:
                                for j in i:
                                    selected_courses_list.append(j)
                        selected_courses = ", ".join(selected_courses_list)
                    return redirect(url_for('elective_course.submit'))
            if rounds >= 0 and int(session["elective_courses_question"]) > 1:
                back_val = True
            if rounds > 0 and int(session["elective_courses_question"]) == 1:
                back_val = True

            # Last question to answer
            if session["elective_courses_question"] == '4' and rounds == 4:
                next_question = "Submit"
                switch = True
            #     return redirect(url_for('elective_course.timer'))
            if session["elective_courses_question"] in se_total_questions_and_answer:
                # If the question exists in the dictionary, redirect to the question
                #
                return redirect(url_for('elective_course.timer_sye'))

            session_count = int(session_count['elective_courses_question'])

    return render_template('questions/elective_courses/elective_sye_questions.html', num_counter=counting_down,
                           switch=switch,
                           num=current_number, next_question=next_question, back_val=back_val,
                           ntot=se_total_questions,
                           question=question_to_ask,
                           ans1=a,
                           ans2=b,
                           ans3=c,
                           selected_area_of_specialization_from_form=selected_area_of_specialization_from_form,
                           form=form)


@elective_course.route('/elective-submit', methods=['GET', 'POST'])
@login_required
@elective_question_finished
def submit():
    total_questions_answered = 0
    global total_correct
    global total_failed
    global selected_courses
    global user_response
    total_questions_from_course = 0
    if selected_area_of_specialization_from_form == 'ai':
        total_questions_from_course = ai_total_questions
    elif selected_area_of_specialization_from_form == 'cn':
        total_questions_from_course = cn_total_questions
    elif selected_area_of_specialization_from_form == 'se':
        total_questions_from_course = soe_total_questions
    elif selected_area_of_specialization_from_form == 'sye':
        total_questions_from_course = se_total_questions
    try:
        total_questions_answered = int(total_correct) + int(total_failed)
    except Exception as e:
        pass
    # total_questions_answered = str(int(tot_correct) + int(tot_failed))
    return render_template("result/elective_courses/elective_result.html", title="Result",
                           total_correct=int(total_correct),
                           total_failed=int(total_failed),
                           total_questions_from_course=total_questions_from_course,
                           total_questions_answered=total_questions_answered,
                           sel_courses=selected_courses, user_resp=user_response)


@elective_course.route('/elective-time-up', methods=['GET'])
@login_required
def time_up_from_client():
    global cos_833_total_student
    global cos_833_grade_category
    global cos_816_total_student
    global cos_816_grade_category
    global cos_830_total_student
    global cos_830_grade_category
    global cos_836_total_student
    global cos_836_grade_category
    global cos_834_total_student
    global cos_834_grade_category
    global cos_838_total_student
    global cos_838_grade_category
    global cos_845_total_student
    global cos_845_grade_category
    global cos_829_total_student
    global cos_829_grade_category
    global cos_852_total_student
    global cos_852_grade_category
    global cos_850_total_student
    global cos_850_grade_category
    global total_correct
    global total_failed
    global user_response
    global selected_courses
    global new_sorted_dict
    global new_sorted_list_from_dict

    global cos_833_total_student
    global cos_833_grade_category
    global cos_816_total_student
    global cos_816_grade_category
    global cos_830_total_student
    global cos_830_grade_category
    global cos_836_total_student
    global cos_836_grade_category
    global cos_834_total_student
    global cos_834_grade_category
    global cos_838_total_student
    global cos_838_grade_category

    global cos_821_total_student
    global cos_821_grade_category
    global cos_827_total_student
    global cos_827_grade_category
    global cos_814_total_student
    global cos_814_grade_category
    global cos_820_total_student
    global cos_820_grade_category

    global cos_815_total_student
    global cos_815_grade_category
    global cos_823_total_student
    global cos_823_grade_category
    global cos_817_total_student
    global cos_817_grade_category
    global cos_810_total_student
    global cos_810_grade_category
    global cos_812_total_student
    global cos_812_grade_category

    global selected_area_of_specialization_from_form

    selected_courses_list_new = []
    session["elective_finished"] = "yes"
    session.pop("elective_courses_question")
    filtered_list_output = list()
    new_list = []
    saved_model = joblib.load("models/Prediction/saved_model/mark_category")
    if selected_area_of_specialization_from_form == 'ai':
        if cos_833_correct == 0 and cos_816_correct == 0 and cos_830_correct == 0 and cos_836_correct == \
                0 and cos_834_correct == 0 and cos_838_correct == 0:
            user_response = "No Elective Course can be selected"
    elif selected_area_of_specialization_from_form == "cn":
        if cos_845_correct == 0 and cos_829_correct == 0 and cos_852_correct == 0 and cos_850_correct == 0:
            user_response = "No Elective Course can be selected"
    elif selected_area_of_specialization_from_form == "se":
        if cos_821_correct == 0 and cos_827_correct == 0 and cos_814_correct == 0 and cos_820_correct == 0:
            user_response = "No Elective Course can be selected"
    elif selected_area_of_specialization_from_form == "sye":
        if cos_815_correct == 0 and cos_823_correct == 0 and cos_817_correct == 0 and cos_810_correct == \
                0 and cos_812_correct == 0:
            user_response = "No Elective Course can be selected"
    if user_response != "No Elective Course can be selected":
        if selected_area_of_specialization_from_form == 'ai':
            new_list = [("COS833", cos_833_correct), ("COS816", cos_816_correct),
                        ("COS830", cos_830_correct), ("COS836", cos_836_correct),
                        ("COS834", cos_834_correct), ("COS838", cos_838_correct)]
        elif selected_area_of_specialization_from_form == 'cn':
            new_list = [("COS845", cos_845_correct), ("COS829", cos_829_correct),
                        ("COS852", cos_852_correct), ("COS850", cos_850_correct)]
        elif selected_area_of_specialization_from_form == 'se':
            new_list = [("COS821", cos_821_correct), ("COS814", cos_814_correct),
                        ("COS827", cos_827_correct), ("COS820", cos_820_correct)]
        elif selected_area_of_specialization_from_form == 'sye':
            new_list = [("COS815", cos_815_correct), ("COS823", cos_823_correct),
                        ("COS817", cos_817_correct), ("COS810", cos_810_correct),
                        ("COS812", cos_812_correct)]
        new_dict = dict(new_list)
        for key, value in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True):
            new_sorted_dict.update({key: value})
            new_sorted_list_from_dict.append(new_sorted_dict)
            new_sorted_dict = dict()

        chck_list = []
        chck_list_keys = []
        chck_dict = dict()
        chck_list_dict = []
        ranked_list = []
        for i in new_sorted_list_from_dict:
            for j, k in i.items():
                chck_list.append(k)
                chck_list_keys.append(j)

        max_val = max(chck_list)
        inc = 1
        for i in range(len(chck_list) - 1):
            if chck_list[i] == chck_list[i + 1] and chck_list[i] == max_val:
                inc += 1

        filtered_dict = dict()
        if inc > 2:
            for i, j in enumerate(chck_list):
                if j == max_val:
                    chck_dict.update({chck_list_keys[i]: j})
                    chck_list_dict.append(chck_dict)
                    chck_dict = dict()
            if selected_area_of_specialization_from_form == 'ai':
                filtered_list_output = ai_preprocessing(chck_list_dict, saved_model)
            elif selected_area_of_specialization_from_form == 'cn':
                filtered_list_output = cn_preprocessing(chck_list_dict, saved_model)
            elif selected_area_of_specialization_from_form == 'se':
                filtered_list_output = se_preprocessing(chck_list_dict, saved_model)
            elif selected_area_of_specialization_from_form == 'sye':
                filtered_list_output = sye_preprocessing(chck_list_dict, saved_model)
            filtered_dict = dict(filtered_list_output)
            chck_list_keys = []
            chck_list = []
            chck_list_dict = []
            for key, value in sorted(filtered_dict.items(), key=lambda item: (item[1], item[0])):
                chck_list_keys.append(key)
                chck_list.append(value)
            for i, j in enumerate(chck_list_keys[:2]):
                chck_dict.update({j: chck_list[i]})
                chck_list_dict.append(chck_dict)
                chck_dict = dict()
            for i in chck_list_dict:
                for j in i:
                    selected_courses_list_new.append(j)
        else:
            for i, j in enumerate(chck_list_keys[:2]):
                chck_dict.update({j: chck_list[i]})
                chck_list_dict.append(chck_dict)
                chck_dict = dict()
            chck_list_dict = predict_from_ranges(chck_list_dict, saved_model)
            for i in chck_list_dict:
                for j in i:
                    selected_courses_list_new.append(j)
        selected_courses = ", ".join(selected_courses_list_new)
    return redirect(url_for('elective_course.submit'))


@elective_course.route('/elective-question-back', methods=['GET', 'POST'])
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
        global question_tracking
        global selected_area_of_specialization_from_form

        current_round = rounds
        next_question = "Next Question"
        switch = False
        # current_round -= 1
        # rounds = current_round
        if current_round == 1 and session["elective_courses_question"] == '1':
            if question_tracking == 0:
                question_tracking = 1
            for key in list(session_dict)[question_tracking:]:
                del session_dict[key]
            back_val = False
        if current_round == 0:
            session["elective_courses_question"] = str(int(session["elective_courses_question"]) - 1)
            question_tracking -= 1
            if question_tracking == 0:
                question_tracking = 1
            if selected_area_of_specialization_from_form == 'ai':
                ai_removal(session["elective_courses_question"])
            elif selected_area_of_specialization_from_form == 'cn':
                cn_removal(session["elective_courses_question"])
            elif selected_area_of_specialization_from_form == 'se':
                se_removal(session["elective_courses_question"])
            elif selected_area_of_specialization_from_form == 'sye':
                sye_removal(session["elective_courses_question"])
            for key in list(session_dict)[question_tracking:]:
                del session_dict[key]
            if session["elective_courses_question"] in session_dict.keys():
                if session_dict[question_tracking][2] is not None:
                    if session_dict[question_tracking][1] == \
                            session_dict[question_tracking][2]:
                        total_correct -= 1
                    else:
                        total_failed -= 1
            current_number -= 1
            rounds = 5
            if selected_area_of_specialization_from_form == 'ai':
                return redirect(url_for('elective_course.timer'))
            elif selected_area_of_specialization_from_form == 'cn':
                return redirect(url_for('elective_course.timer_cn'))
            elif selected_area_of_specialization_from_form == 'se':
                return redirect(url_for('elective_course.timer_se'))
            elif selected_area_of_specialization_from_form == 'sye':
                return redirect(url_for('elective_course.timer_sye'))
        else:
            current_round -= 1
            current_number -= 1
            question_tracking -= 1
            if selected_area_of_specialization_from_form == 'ai':
                ai_removal(session["elective_courses_question"])
            elif selected_area_of_specialization_from_form == 'cn':
                cn_removal(session["elective_courses_question"])
            elif selected_area_of_specialization_from_form == 'se':
                se_removal(session["elective_courses_question"])
            elif selected_area_of_specialization_from_form == 'sye':
                sye_removal(session["elective_courses_question"])
            if question_tracking == 0:
                question_tracking = 1
            rounds = current_round
            if session_dict[question_tracking][2] is not None:
                if session_dict[question_tracking][1] == \
                        session_dict[question_tracking][2]:
                    total_correct -= 1
                else:
                    total_failed -= 1
            for key in list(session_dict)[question_tracking:]:
                del session_dict[key]
            if selected_area_of_specialization_from_form == 'ai':
                return redirect(url_for('elective_course.timer'))
            elif selected_area_of_specialization_from_form == 'cn':
                return redirect(url_for('elective_course.timer_cn'))
            elif selected_area_of_specialization_from_form == 'se':
                return redirect(url_for('elective_course.timer_se'))
            elif selected_area_of_specialization_from_form == 'sye':
                return redirect(url_for('elective_course.timer_sye'))


def ai_removal(subtracted_session):
    global cos_833_correct
    global cos_833_failed
    global cos_816_correct
    global cos_816_failed
    global cos_830_correct
    global cos_830_failed
    global cos_836_correct
    global cos_836_failed
    global cos_834_correct
    global cos_834_failed
    global cos_838_correct
    global cos_838_failed
    global session_dict
    global question_tracking
    if question_tracking == 0:
        question_tracking = 1
    if cos_833_selected_six_random[int(subtracted_session) - 1] == \
            session_dict[question_tracking][0]:
        if current_answer == session_dict[question_tracking][1]:
            cos_833_correct -= 1
        else:
            cos_833_failed -= 1
    elif cos_816_selected_six_random[int(subtracted_session) - 1] == \
            session_dict[question_tracking][0]:
        if current_answer == session_dict[question_tracking][1]:
            cos_816_correct -= 1
        else:
            cos_816_failed -= 1
    elif cos_830_selected_six_random[int(subtracted_session) - 1] == \
            session_dict[question_tracking][0]:
        if current_answer == session_dict[question_tracking][1]:
            cos_830_correct -= 1
        else:
            cos_830_failed -= 1
    elif cos_836_selected_six_random[int(subtracted_session) - 1] == \
            session_dict[question_tracking][0]:
        if current_answer == session_dict[question_tracking][1]:
            cos_836_correct -= 1
        else:
            cos_836_failed -= 1
    elif cos_834_selected_six_random[int(subtracted_session) - 1] == \
            session_dict[question_tracking][0]:
        if current_answer == session_dict[question_tracking][1]:
            cos_834_correct -= 1
        else:
            cos_834_failed -= 1
    elif cos_838_selected_six_random[int(subtracted_session) - 1] == \
            session_dict[question_tracking][0]:
        if current_answer == session_dict[question_tracking][1]:
            cos_838_correct -= 1
        else:
            cos_838_failed -= 1


def cn_removal(subtracted_session):
    global cos_845_correct
    global cos_845_failed
    global cos_829_correct
    global cos_829_failed
    global cos_852_correct
    global cos_852_failed
    global cos_850_correct
    global cos_850_failed
    global session_dict
    global question_tracking
    if question_tracking == 0:
        question_tracking = 1
    if cos_845_selected_six_random[int(subtracted_session) - 1] == \
            session_dict[question_tracking][0]:
        if current_answer == session_dict[question_tracking][1]:
            cos_845_correct -= 1
        else:
            cos_845_failed -= 1
    elif cos_829_selected_six_random[int(subtracted_session) - 1] == \
            session_dict[question_tracking][0]:
        if current_answer == session_dict[question_tracking][1]:
            cos_829_correct -= 1
        else:
            cos_829_failed -= 1
    elif cos_852_selected_six_random[int(subtracted_session) - 1] == \
            session_dict[question_tracking][0]:
        if current_answer == session_dict[question_tracking][1]:
            cos_852_correct -= 1
        else:
            cos_852_failed -= 1
    elif cos_850_selected_six_random[int(subtracted_session) - 1] == \
            session_dict[question_tracking][0]:
        if current_answer == session_dict[question_tracking][1]:
            cos_850_correct -= 1
        else:
            cos_850_failed -= 1


def se_removal(subtracted_session):
    global cos_821_correct
    global cos_821_failed
    global cos_827_correct
    global cos_827_failed
    global cos_814_correct
    global cos_814_failed
    global cos_820_correct
    global cos_820_failed
    global session_dict
    global question_tracking
    if question_tracking == 0:
        question_tracking = 1
    if cos_821_selected_six_random[int(subtracted_session) - 1] == \
            session_dict[question_tracking][0]:
        if current_answer == session_dict[question_tracking][1]:
            cos_821_correct -= 1
        else:
            cos_821_failed -= 1
    elif cos_827_selected_six_random[int(subtracted_session) - 1] == \
            session_dict[question_tracking][0]:
        if current_answer == session_dict[question_tracking][1]:
            cos_827_correct -= 1
        else:
            cos_827_failed -= 1
    elif cos_814_selected_six_random[int(subtracted_session) - 1] == \
            session_dict[question_tracking][0]:
        if current_answer == session_dict[question_tracking][1]:
            cos_814_correct -= 1
        else:
            cos_814_failed -= 1
    elif cos_820_selected_six_random[int(subtracted_session) - 1] == \
            session_dict[question_tracking][0]:
        if current_answer == session_dict[question_tracking][1]:
            cos_820_correct -= 1
        else:
            cos_820_failed -= 1


def sye_removal(subtracted_session):
    global cos_815_correct
    global cos_815_failed
    global cos_823_correct
    global cos_823_failed
    global cos_817_correct
    global cos_817_failed
    global cos_810_correct
    global cos_810_failed
    global cos_812_correct
    global cos_812_failed
    global session_dict
    global question_tracking
    if question_tracking == 0:
        question_tracking = 1
    if cos_815_selected_six_random[int(subtracted_session) - 1] == \
            session_dict[question_tracking][0]:
        if current_answer == session_dict[question_tracking][1]:
            cos_815_correct -= 1
        else:
            cos_815_failed -= 1
    elif cos_823_selected_six_random[int(subtracted_session) - 1] == \
            session_dict[question_tracking][0]:
        if current_answer == session_dict[question_tracking][1]:
            cos_823_correct -= 1
        else:
            cos_823_failed -= 1
    elif cos_817_selected_six_random[int(subtracted_session) - 1] == \
            session_dict[question_tracking][0]:
        if current_answer == session_dict[question_tracking][1]:
            cos_817_correct -= 1
        else:
            cos_817_failed -= 1
    elif cos_810_selected_six_random[int(subtracted_session) - 1] == \
            session_dict[question_tracking][0]:
        if current_answer == session_dict[question_tracking][1]:
            cos_810_correct -= 1
        else:
            cos_810_failed -= 1
    elif cos_812_selected_six_random[int(subtracted_session) - 1] == \
            session_dict[question_tracking][0]:
        if current_answer == session_dict[question_tracking][1]:
            cos_812_correct -= 1
        else:
            cos_812_failed -= 1


def predict_from_ranges(list_dict_to_predict_value, saved_model):
    global selected_area_of_specialization_from_form
    predicted_dict = dict()
    predicted_list_dict = list()
    for i in list_dict_to_predict_value:
        for j, k in i.items():
            if selected_area_of_specialization_from_form == 'ai':
                k = k * 20
            elif selected_area_of_specialization_from_form == 'cn':
                k = k * 20
            elif selected_area_of_specialization_from_form == 'se':
                k = k * 20
            elif selected_area_of_specialization_from_form == 'sye':
                k = k * 25
            predicted_value = predict_grade_range(k, saved_model)
            predicted_dict.update({j: predicted_value})
            predicted_list_dict.append(predicted_dict)
            predicted_dict = dict()
    return predicted_list_dict


def calculated_ranking(predicted_range, course_total_students, course_grade_category):
    total_students = 0
    expected_students = 0
    for i in course_total_students:
        for j in i:
            if j != 'nan':
                total_students += 1
    for i in course_grade_category:
        for j in i:
            if j == predicted_range:
                expected_students += 1
    try:
        total_range = total_students / expected_students
    except Exception as _:
        total_range = 0

    return total_range


def ai_preprocessing(ai_chck_list_dict, saved_model_to_use):
    filtered_list_dict = list()
    predicted_outcome_to_be_ranked = predict_from_ranges(ai_chck_list_dict, saved_model_to_use)
    for i in predicted_outcome_to_be_ranked:
        for j, k in i.items():
            for l in k:
                if j == 'COS833':
                    calculated_outcome = calculated_ranking(l[1], cos_833_total_student,
                                                            cos_833_grade_category)
                    filtered_list_dict.append((j, calculated_outcome))
                elif j == 'COS816':
                    calculated_outcome = calculated_ranking(l[1], cos_816_total_student,
                                                            cos_816_grade_category)
                    filtered_list_dict.append((j, calculated_outcome))
                elif j == 'COS830':
                    calculated_outcome = calculated_ranking(l[1], cos_830_total_student,
                                                            cos_830_grade_category)
                    filtered_list_dict.append((j, calculated_outcome))
                elif j == 'COS836':
                    calculated_outcome = calculated_ranking(l[1], cos_836_total_student,
                                                            cos_836_grade_category)
                    filtered_list_dict.append((j, calculated_outcome))
                elif j == 'COS834':
                    calculated_outcome = calculated_ranking(l[1], cos_834_total_student,
                                                            cos_834_grade_category)
                    filtered_list_dict.append((j, calculated_outcome))
                elif j == 'COS838':
                    calculated_outcome = calculated_ranking(l[1], cos_838_total_student,
                                                            cos_838_grade_category)
                    filtered_list_dict.append((j, calculated_outcome))
    return filtered_list_dict


def cn_preprocessing(cn_chck_list_dict, saved_model_to_use):
    filtered_list_dict = list()
    predicted_outcome_to_be_ranked = predict_from_ranges(cn_chck_list_dict, saved_model_to_use)
    for i in predicted_outcome_to_be_ranked:
        for j, k in i.items():
            for l in k:
                if j == 'COS845':
                    calculated_outcome = calculated_ranking(l[1], cos_845_total_student,
                                                            cos_845_grade_category)
                    filtered_list_dict.append((j, calculated_outcome))
                elif j == 'COS829':
                    calculated_outcome = calculated_ranking(l[1], cos_829_total_student,
                                                            cos_829_grade_category)
                    filtered_list_dict.append((j, calculated_outcome))
                elif j == 'COS852':
                    calculated_outcome = calculated_ranking(l[1], cos_852_total_student,
                                                            cos_852_grade_category)
                    filtered_list_dict.append((j, calculated_outcome))
                elif j == 'COS850':
                    calculated_outcome = calculated_ranking(l[1], cos_850_total_student,
                                                            cos_850_grade_category)
                    filtered_list_dict.append((j, calculated_outcome))
    return filtered_list_dict


def se_preprocessing(cn_chck_list_dict, saved_model_to_use):
    filtered_list_dict = list()
    predicted_outcome_to_be_ranked = predict_from_ranges(cn_chck_list_dict, saved_model_to_use)
    for i in predicted_outcome_to_be_ranked:
        for j, k in i.items():
            for l in k:
                if j == 'COS821':
                    calculated_outcome = calculated_ranking(l[1], cos_821_total_student,
                                                            cos_821_grade_category)
                    filtered_list_dict.append((j, calculated_outcome))
                elif j == 'COS827':
                    calculated_outcome = calculated_ranking(l[1], cos_827_total_student,
                                                            cos_827_grade_category)
                    filtered_list_dict.append((j, calculated_outcome))
                elif j == 'COS814':
                    calculated_outcome = calculated_ranking(l[1], cos_814_total_student,
                                                            cos_814_grade_category)
                    filtered_list_dict.append((j, calculated_outcome))
                elif j == 'COS820':
                    calculated_outcome = calculated_ranking(l[1], cos_820_total_student,
                                                            cos_820_grade_category)
                    filtered_list_dict.append((j, calculated_outcome))
    return filtered_list_dict


def sye_preprocessing(cn_chck_list_dict, saved_model_to_use):
    filtered_list_dict = list()
    predicted_outcome_to_be_ranked = predict_from_ranges(cn_chck_list_dict, saved_model_to_use)
    for i in predicted_outcome_to_be_ranked:
        for j, k in i.items():
            for l in k:
                if j == 'COS815':
                    calculated_outcome = calculated_ranking(l[1], cos_815_total_student,
                                                            cos_815_grade_category)
                    filtered_list_dict.append((j, calculated_outcome))
                elif j == 'COS823':
                    calculated_outcome = calculated_ranking(l[1], cos_823_total_student,
                                                            cos_823_grade_category)
                    filtered_list_dict.append((j, calculated_outcome))
                elif j == 'COS817':
                    calculated_outcome = calculated_ranking(l[1], cos_817_total_student,
                                                            cos_817_grade_category)
                    filtered_list_dict.append((j, calculated_outcome))
                elif j == 'COS810':
                    calculated_outcome = calculated_ranking(l[1], cos_810_total_student,
                                                            cos_810_grade_category)
                    filtered_list_dict.append((j, calculated_outcome))
                elif j == 'COS812':
                    calculated_outcome = calculated_ranking(l[1], cos_812_total_student,
                                                            cos_812_grade_category)
                    filtered_list_dict.append((j, calculated_outcome))
    return filtered_list_dict
