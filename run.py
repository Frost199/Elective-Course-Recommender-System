from app import create_app
from models.users.users import User
from utils import Utils


if __name__ == '__main__':
    app = create_app()
    with open("first_time_server_run.txt", "r") as new_file:
        content = new_file.read()
        if content == "":
            var = True
            while var:
                print("Welcome Admin Please put in the following Credentials")
                surname = input("Surname: ")
                middle_name = input("Middle Name: ")
                first_name = input("First Name: ")
                user_name = input("Username: ")
                email = input("E-mail: ")
                password = input("Password: ")
                if surname != "" and middle_name != "" and first_name != "" and email != "" and user_name != "" \
                        and password != "":
                    encrypted_password = Utils.encrypt_password(password)
                    grand_admin = User()
                    grand_admin.create_admin(surname=surname, middle_name=middle_name, email=email,
                                             first_name=first_name, password=encrypted_password, username=user_name)
                    with open("first_time_server_run.txt", "a") as new_file_write:
                        new_file_write.write("true")
                        var = False
                    break
                else:
                    continue
    app.run()
