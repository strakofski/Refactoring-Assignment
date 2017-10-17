# KRIS LITTLE

import sqlite3

from Database.IDatabase import *


class SQLDatabase(IDatabase):
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def backup_database(self):
        self.execute_sql("""select * from employee""")
        get_data = self.cursor.fetchall()
        data = []
        for d in get_data:
            data.append(d)
        print(data)
        return data

    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e, "\nFor a list of tables, type help.")

    def write_to_database(self, data):
        try:
            for employee in data:
                format_str = """INSERT INTO employee (EMPID, Gender, Age, Sales, BMI, Salary, Birthday) 
                VALUES ("{empid}","{gender}","{age}","{sales}","{BMI}","{salary}","{birthday}"); """
                sql_command = format_str.format(empid=employee[0], gender=employee[1], age=employee[2],
                                                sales=employee[3], BMI=employee[4], salary=employee[5],
                                                birthday=employee[6])
                self.execute_sql(sql_command)
        except IndexError as e:
            print(e)

        except TypeError as e:
            print(e)

        self.commit()

    def display_data(self):
        self.execute_sql("""select * from employee""")
        data = self.cursor.fetchall()
        for d in data:
            print(str(d))

    def close_connection(self):
        self.connection.close()

    def commit(self):
        self.connection.commit()

    def setup(self):

        sql = """
        CREATE TABLE if not exists employee ( 
        EMPID char(3),
        Gender char(1),
        Age int,
        Sales int,
        BMI varchar(200),
        Salary int,
        Birthday date
        );

        """
        self.execute_sql(sql)
        self.commit()

    def reset(self):
        self.execute_sql("""drop table if exists employee""")
        self.setup()
