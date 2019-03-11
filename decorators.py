from functools import wraps
from flask import redirect, url_for, session, flash
from flask_login import current_user

selected_aos = ''


def question_info_page(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and "current_question" not in session:
            return redirect(url_for('aos_test.index'))
        return func(*args, **kwargs)

    return decorated_function


def elective_question_info_page(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and "elective_courses_question" not in session:
            return redirect(url_for('elective_course.index'))
        return func(*args, **kwargs)

    return decorated_function


def question_finished(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and "finished" not in session:
            if "current_question" not in session:
                session["current_question"] = '0'
            # print(session["current_question"])
            if int(session["current_question"]) > 0:
                return redirect(url_for('aos_test.timer'))
            else:
                return redirect(url_for('aos_test.index'))
        return func(*args, **kwargs)

    return decorated_function


def elective_question_finished(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and "elective_finished" not in session:
            if "current_ai_question" not in session:
                session["current_ai_question"] = '0'
            # print(session["current_question"])
            if int(session["current_ai_question"]) > 0:
                if selected_aos == 'ai':
                    return redirect(url_for('elective_course.timer'))
                elif selected_aos == 'cn':
                    return redirect(url_for('elective_course.timer_cn'))
                elif selected_aos == 'se':
                    return redirect(url_for('elective_course.timer_se'))
                elif selected_aos == 'sye':
                    return redirect(url_for('elective_course.timer_sye'))
            else:
                return redirect(url_for('elective_course.index'))
        return func(*args, **kwargs)

    return decorated_function


def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.account_type not in roles:
                flash('Permission Denied, You cannot access that given Page!', "danger")
                return redirect("/")
            return f(*args, **kwargs)

        return decorated_function

    return decorator
