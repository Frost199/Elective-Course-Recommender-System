from passlib.hash import pbkdf2_sha512
import constants
import re


class Utils(object):

    @staticmethod
    def encrypt_password(password):
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_encrypted_password(password, hashed_password):

        return pbkdf2_sha512.verify(password, hashed_password)

    @staticmethod
    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in constants.ALLOWED_EXTENSIONS

    @staticmethod
    def strong_password(password_to_check):
        a = b = c = d = e = f = ''
        try:
            matcher_digits = re.compile(r'[0-9]+')
            matcher_lowercase = re.compile(r'[a-z]+')
            matcher_uppercase = re.compile(r'[A-Z]+')
            matcher_special = re.compile(r'[\W.\\?\[\]|+*$()_^{\}]+')

            mo_digits = matcher_digits.search(password_to_check)
            mo_lowercase = matcher_lowercase.search(password_to_check)
            mo_uppercase = matcher_uppercase.search(password_to_check)
            mo_special = matcher_special.search(password_to_check)

            if mo_digits and mo_lowercase and mo_uppercase and mo_special:
                return None
            if not mo_digits or not mo_lowercase or not mo_uppercase or not mo_special:
                if not mo_special:
                    a += "one special character is required"
                if not mo_digits:
                    b += "a number is required"
                if not mo_lowercase:
                    c += "a lowercase letter is required"
                if not mo_uppercase:
                    d += "an uppercase letter is required"
            if not mo_digits and not mo_lowercase and not mo_uppercase and not mo_special:
                e += "Password should include a Lowercase, a Uppercase, Numbers and special characters"
            return a, b, c, d, e
        except Exception as _:
            f += "Password should include a Lowercase, a Uppercase, Numbers and special characters"
            return f

    @staticmethod
    def check_reg_number(reg_num):
        try:
            matcher = re.compile(r'\d{4}/\d{6}')
            matching_reg_number = matcher.search(reg_num)

            reg_num_format_length = reg_num.split("/")
            reg_num_format_length_first = reg_num_format_length[0]
            reg_num_format_length_last = reg_num_format_length[1]

            if matching_reg_number and \
                    len(reg_num_format_length_first) == 4 and \
                    len(reg_num_format_length_last) == 6 and \
                    len(reg_num_format_length) == 2:
                return None
            else:
                return "Incorrect formatted Registration Number"
        except Exception as _:
            return "Incorrect formatted Registration Number"
