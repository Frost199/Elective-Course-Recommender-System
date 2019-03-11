import sqlite3

connection = sqlite3.connect('Credentials.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users_credential (id INTEGER PRIMARY KEY," \
               "reg_number text," \
               "surname text," \
               "middle_name text," \
               "first_name text," \
               "email text," \
               "password text," \
               "_id text," \
               "timestamp text," \
               "date_registered text," \
               "profile_picture text," \
               "account_type text)"
cursor.execute(create_table)

connection.commit()
connection.close()
