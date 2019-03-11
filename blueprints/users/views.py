import base64
import os
import secrets
from PIL import Image
from flask import Blueprint, render_template, flash, redirect, url_for, request
from decorators import role_required
from extensions import csrf
from models.forms.forms import AdminAddUserForm, UserLoginForm, UpdateAccountForm, UpdateAdminAccountForm, \
    AdminUpdateStudentAccountForm
from models.users.users import User
from utils import Utils
from flask_login import login_user, current_user, logout_user, login_required

user = Blueprint('user', __name__, template_folder='templates')


@user.route('/user portal')
@login_required
@role_required('student')
def user_account():
    image_file = url_for('static', filename='assets/pictures/' + current_user.default_image)
    return render_template('account.html', image_file=image_file)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, file_extension = os.path.split(form_picture.filename)
    picture_file_name = random_hex + file_extension
    picture_path = os.path.join('./static/assets/pictures', picture_file_name)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_file_name


@user.route('/update', methods=['GET', 'POST'])
@login_required
@role_required('student', 'admin')
def update():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.default_image = picture_file
        current_user.reg_number = form.registration_number.data
        current_user.surname = form.surname.data
        current_user.middle_name = form.middle_name.data
        current_user.first_name = form.first_name.data
        current_user.password = current_user.password if form.password.data is None else form.password.data
        current_user.email = form.email.data
        User.update_profile(username=current_user.reg_number, surname=current_user.surname,
                            middle_name=current_user.middle_name, first_name=current_user.first_name,
                            password=current_user.password, email=current_user.email,
                            picture_to_update=current_user.default_image, user_corresponding_id=current_user.id)
        flash('Your account has been updated!', 'success')
        return redirect(url_for('user.update'))
    elif request.method == 'GET':
        form.registration_number.data = current_user.reg_number
        form.surname.data = current_user.surname
        form.middle_name.data = current_user.middle_name
        form.first_name.data = current_user.first_name
        form.email.data = current_user.email
    image_file = url_for('static', filename='assets/pictures/' + current_user.default_image)
    return render_template('account_update.html', title='Update', image_file=image_file, form=form)


@user.route('/admin-update', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def admin_update():
    form = UpdateAdminAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.default_image = picture_file
        current_user.reg_number = form.registration_number.data
        current_user.surname = form.surname.data
        current_user.middle_name = form.middle_name.data
        current_user.first_name = form.first_name.data
        current_user.password = current_user.password if form.password.data is None else form.password.data
        current_user.email = form.email.data
        User.update_profile(username=current_user.reg_number, surname=current_user.surname,
                            middle_name=current_user.middle_name, first_name=current_user.first_name,
                            password=current_user.password, email=current_user.email,
                            picture_to_update=current_user.default_image, user_corresponding_id=current_user.id)
        flash('Your account has been updated!', 'success')
        return redirect(url_for('user.admin_home'))
    elif request.method == 'GET':
        form.registration_number.data = current_user.reg_number
        form.surname.data = current_user.surname
        form.middle_name.data = current_user.middle_name
        form.first_name.data = current_user.first_name
        form.email.data = current_user.email
    image_file = url_for('static', filename='assets/pictures/' + current_user.default_image)
    return render_template('admin/update.html', title='Update', image_file=image_file, form=form)


@user.route('/admin', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def admin_home():
    all_students = User.fetch_all_students_by_account_type()
    image_file = url_for('static', filename='assets/pictures/' + current_user.default_image)
    return render_template('admin/admin.html', title='Admin Home', image_file=image_file, all_students=all_students)


@user.route("/add-student", methods=['GET', 'POST'])
@login_required
@role_required('admin')
def add_student():
    form = AdminAddUserForm()
    if form.validate_on_submit():
        new_student = User()
        new_student.insert_student_into_db(surname=form.surname.data, middle_name=form.middle_name.data,
                                           first_name=form.first_name.data, reg_number=form.registration_number.data,
                                           email=form.email.data, password=form.password.data)
        flash('Account Created!', 'success')
        return redirect(url_for("user.admin_home"))
    return render_template("admin/add_user.html", title="Edit User", form=form)


@user.route("/admin-edit", methods=['GET', 'POST'])
@login_required
@role_required('admin')
@csrf.exempt
def edit_users():
    _id = request.form['id']
    _id_bytes = _id.encode()
    _id = base64.encodebytes(_id_bytes)
    return redirect(url_for("user.edit_users_template", base_id=_id))


@user.route("/edit/<string:base_id>", methods=['GET', 'POST'])
@login_required
@role_required('admin')
def edit_users_template(base_id):
    id_str = base_id.encode()
    _id = base64.decodebytes(id_str)
    base_id = _id.decode()
    form = AdminUpdateStudentAccountForm()
    individual_student = User.find_by_id(base_id)
    if form.validate_on_submit():
        User.update_student_profile_by_admin(reg_number=form.registration_number.data, surname=form.surname.data,
                                             middle_name=form.middle_name.data, first_name=form.first_name.data,
                                             email=form.email.data, user_corresponding_id=individual_student.id)
        flash('Account Updated!', 'success')
        return redirect(url_for("user.admin_home"))
    elif request.method == 'GET':
        form.registration_number.data = individual_student.reg_number
        form.surname.data = individual_student.surname
        form.middle_name.data = individual_student.middle_name
        form.first_name.data = individual_student.first_name
        form.email.data = individual_student.email
    image_file = url_for('static', filename='assets/pictures/' + individual_student.default_image)
    return render_template("admin/edit_user.html", title="Edit User", form=form,
                           image_file=image_file, individual_student=individual_student)


# @user.route('/register', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('user.user_account'))
#     form = UserRegistrationForm()
#     if form.validate_on_submit():
#
#         reg_number_checker = Utils.check_reg_number(form.registration_number.data)
#         registration_number_from_database = User.find_by_registration_number(reg_number=form.registration_number.data)
#         email_from_database = User.find_by_email(email=form.email.data)
#
#         if registration_number_from_database is None and email_from_database is None:
#
#             if reg_number_checker is None:
#                 encrypted_password = Utils.encrypt_password(password=form.password.data)
#                 user_created = User(reg_number=form.registration_number.data,
#                                     surname=form.surname.data,
#                                     middle_name=form.middle_name.data,
#                                     first_name=form.first_name.data,
#                                     email=form.email.data,
#                                     password=encrypted_password)
#                 user_created.save_to_db()
#                 flash(f'Account created for {form.first_name.data}!', 'success')
#                 return redirect(url_for('user.login'))
#
#         elif registration_number_from_database or email_from_database:
#             if registration_number_from_database and email_from_database:
#                 flash(f'Email and Registration Number are already registered!', 'danger')
#                 return render_template('signup.html', title='Register', form=form,
#                                        wrong_reg=reg_number_checker)
#             if registration_number_from_database:
#                 if form.registration_number.data == registration_number_from_database.reg_number:
#                     flash(f'Registration Number {form.registration_number.data} Exists!', 'danger')
#
#                     return render_template('signup.html', title='Register', form=form,
#                                            wrong_reg=reg_number_checker)
#             if email_from_database:
#                 if form.email.data == email_from_database.email:
#                     flash(f'{form.email.data} is already registered', 'danger')
#
#                     return render_template('signup.html', title='Register', form=form,
#                                            wrong_reg=reg_number_checker)
#     else:
#         return render_template('signup.html', title='Register', form=form)


@user.route('/', methods=['GET', 'POST'])
@user.route('/home', methods=['GET', 'POST'])
@user.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        if current_user.account_type == "admin":
            return redirect(url_for('user.admin_home'))
        elif current_user.account_type == "student":
            return redirect(url_for('user.user_account'))
    form = UserLoginForm()
    if form.validate_on_submit():
        valid_user_with_reg = User.find_by_registration_number(form.registration_number.data)
        if valid_user_with_reg and Utils.check_encrypted_password(form.password.data, valid_user_with_reg.password):
            login_user(valid_user_with_reg, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if valid_user_with_reg.account_type == "student":
                return redirect(next_page) if next_page else redirect(url_for('user.user_account'))
            elif valid_user_with_reg.account_type == "admin":
                if next_page:
                    return redirect(next_page)
                else:
                    flash(f'Welcome {current_user.surname} {current_user.first_name} {current_user.middle_name}', 'info')
                    return redirect(url_for('user.admin_home'))
        else:
            flash(f'Login Unsuccessful, please check Registration Number and Password', 'danger')
    return render_template('home.html', title='Home', form=form)


@user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))
