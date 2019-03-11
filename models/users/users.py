import datetime
import sqlite3
import uuid
from flask_login import UserMixin
from extensions import login_manager
from utils import Utils


@login_manager.user_loader
def load_user(user_id):
    return User.find_by_id(user_id)


class User(UserMixin):

    date_time = str(datetime.datetime.utcnow()).split()
    date, time = date_time
    date = str(date)
    time = time.split(".")
    time = time[0].__str__()

    def __init__(self, inc_id=None, reg_number=None, surname=None, middle_name=None,
                 first_name=None, email=None, password=None, _id=None, timestamp=time,
                 date=date, default_image=None, account_type=None):
        self.inc_id = inc_id
        self.reg_number = reg_number
        self.surname = surname
        self.middle_name = middle_name
        self.first_name = first_name
        self.email = email
        self.password = password
        self.id = uuid.uuid4().__str__() if _id is None else _id
        self.timestamp = timestamp
        self.date_registered = date
        self.default_image = "default.png" if default_image is None else default_image
        self.account_type = account_type

    def save_to_db(self):
        """
        This saves the question to the database
        Returns: A notification string

        """
        connection = sqlite3.connect("./database/Credentials.db")
        cursor = connection.cursor()

        query = "INSERT INTO users_credential VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (self.reg_number, self.surname, self.middle_name, self.first_name, self.email,
                               self.password, self.id, self.timestamp, self.date_registered, self.default_image,
                               self.account_type,))
        connection.commit()
        connection.close()

    def create_admin(self, surname, middle_name, first_name, email, password, username):
        self.account_type = "admin"
        connection = sqlite3.connect("./database/credentials.db")
        cursor = connection.cursor()

        query = "INSERT INTO users_credential VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (username, surname, middle_name, first_name, email,
                               password, self.id, self.timestamp, self.date_registered, self.default_image,
                               self.account_type,))
        connection.commit()
        connection.close()

    def insert_student_into_db(self, surname, middle_name, first_name, reg_number, email, password):
        encrypted_password = Utils.encrypt_password(password=password)
        self.account_type = "student"
        connection = sqlite3.connect("./database/credentials.db")
        cursor = connection.cursor()

        query = "INSERT INTO users_credential VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (reg_number, surname, middle_name, first_name, email,
                               encrypted_password, self.id, self.timestamp, self.date_registered,
                               self.default_image, self.account_type,))
        connection.commit()
        connection.close()

    @staticmethod
    def update_profile(username, surname, middle_name, first_name, password, email, picture_to_update, user_corresponding_id):
        encrypted_password = Utils.encrypt_password(password=password)
        connection = sqlite3.connect('./database/Credentials.db')
        cursor = connection.cursor()

        query = "UPDATE users_credential SET reg_number=?, surname=?, middle_name=?, first_name=?, password=?," \
                "email=?, profile_picture=? WHERE _id=?"
        cursor.execute(query, (username,surname, middle_name, first_name, encrypted_password, email, picture_to_update,
                               user_corresponding_id,))

        connection.commit()
        connection.close()

    @staticmethod
    def update_student_profile_by_admin(reg_number, surname, middle_name, first_name, email, user_corresponding_id):
        connection = sqlite3.connect('./database/Credentials.db')
        cursor = connection.cursor()

        query = "UPDATE users_credential SET reg_number=?, surname=?, middle_name=?, first_name=?," \
                "email=? WHERE _id=?"
        cursor.execute(query, (reg_number, surname, middle_name, first_name, email, user_corresponding_id,))

        connection.commit()
        connection.close()

    @staticmethod
    def update_password(new_password, user_corresponding_id):
        connection = sqlite3.connect('./database/Credentials.db')
        cursor = connection.cursor()

        query = "UPDATE users_credential SET password=? WHERE _id=?"
        cursor.execute(query, (new_password, user_corresponding_id,))

        connection.commit()
        connection.close()

    @staticmethod
    def update_email(email_update, user_corresponding_id):
        connection = sqlite3.connect('./database/Credentials.db')
        cursor = connection.cursor()

        query = "UPDATE users_credential SET email=? WHERE _id=?"
        cursor.execute(query, (email_update, user_corresponding_id,))

        connection.commit()
        connection.close()

    @staticmethod
    def update_profile_picture(picture_file, user_corresponding_id):
        connection = sqlite3.connect('./database/Credentials.db')
        cursor = connection.cursor()

        query = "UPDATE users_credential SET profile_picture=? WHERE _id=?"
        cursor.execute(query, (picture_file, user_corresponding_id,))

        connection.commit()
        connection.close()

    @classmethod
    def find_by_registration_number(cls, reg_number):
        connection = sqlite3.connect('./database/Credentials.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users_credential WHERE reg_number=?"
        result = cursor.execute(query, (reg_number,))
        row = result.fetchone()
        if row:
            user = cls(*row)  # same as row[0], row[1], row[2]...passing args by position
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_email(cls, email):
        connection = sqlite3.connect('./database/Credentials.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users_credential WHERE email=?"
        result = cursor.execute(query, (email,))
        row = result.fetchone()
        if row:
            user = cls(*row)  # same as row[0], row[1], row[2]...passing args by position
        else:
            user = None

        connection.close()
        return user

    @staticmethod
    def find_all_emails_and_registration_number():
        connection = sqlite3.connect('./database/Credentials.db')
        cursor = connection.cursor()
        query = "SELECT * FROM users_credential ORDER BY email ASC "
        result = cursor.execute(query, )
        rows = result.fetchall()
        new_registration_number = []
        new_email = []
        for row in rows:
            new_registration_number.append(row[1])
            new_email.append(row[5])
        return new_registration_number, new_email

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('./database/Credentials.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users_credential WHERE _id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)  # same as row[0], row[1], row[2]...passing args by position
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def fetch_all_students_by_account_type(cls):
        student = []
        connection = sqlite3.connect('./database/Credentials.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users_credential WHERE account_type='student'"
        result = cursor.execute(query,)
        rows = result.fetchall()
        if rows:
            for row in rows:
                student.append(row)
        else:
            student = []

        connection.close()
        return student
