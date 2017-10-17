from Database.SQLDatabase import *
import matplotlib.pyplot as plt
import getopt
import time


class Graph:

    def __init__(self, database):
        self.data1 = None
        self.database = database
        # NEW Brendan
        self.data2 = None
        self.data3 = None
        self.data4 = None
        self.title = None
        self.type = None
        self.option = None
        self.labels = None
        self.angle = None
        self.time = None

    # Brendan Holt
    # Outputs and graph loaded in the iterpretors graph list that has been passed into the input parameters
    @staticmethod
    def print_graph(graph):
        colours = ['c', 'm', 'r', 'k']
        # If the graph is a pie graphs
        if graph.type == 'pie':
            plt.pie(graph.data1, labels=graph.labels, colors=colours, startangle=90)
        # If the graph is a bar graph
        elif graph.type == 'bar':
            # Load additional information used in a bar graph
            if graph.option == 'salary-by-gender':
                mx = [1, 3, 5, 7]
                wx = [2, 4, 6, 8]
                xl = [1.5, 3.5, 5.5, 7.5]
                plt.bar(mx, graph.data1, color='blue')
                plt.bar(wx, graph.data2, color='red')
                plt.xticks(xl, graph.labels, rotation='vertical')
            elif graph.option == 'salary-by-age':
                aa = [1, 6, 11, 16]
                ab = [2, 7, 12, 17]
                ac = [3, 8, 13, 18]
                ad = [4, 9, 14, 19]
                xl = [2.5, 7.5, 12.5, 17.5]
                plt.bar(aa, graph.data1, color='blue')
                plt.bar(ab, graph.data2, color='red')
                plt.bar(ac, graph.data3, color='green')
                plt.bar(ad, graph.data4, color='yellow')
                plt.xticks(xl, graph.labels, rotation='horizontal')
        plt.title(graph.title)
        plt.show()

    # Brendan Holt
    # Builds a graph, called from create_graph in the interpreter
    @staticmethod
    def build_graph(self, args):
        try:
            argss = []
            args = getopt.getopt(args, "t:o:", ["graph-type=", "option="])
            # If new graph is none then create argss as regular else append args from create_graph
            argss.append(args[1][0])
            argss.append(args[1][1])
            # Raises exception is wrong amount of args
            if len(argss) == 2:
                raise TypeError
            # Raised exception if args are typed incorrectly
            if argss[0] == 'pie' and argss[1] != 'gender' and argss[1] != 'bmi' and argss[1] != 'age' \
                    or argss[0] == 'bar' and argss[1] != 'salary-by-gender' and argss[1] != 'salary-by-age':
                raise ValueError
        except TypeError:
            print('This functions takes exactly one parameters')
            return
        except ValueError:
            print('Ensure Graph Value Option Parameter is correctly spelt')
            return
        database = self.database
        new_graph = Graph(database)

        # Nested Function to shorten code required to build graphdata
        def append_sql(self, sql):
            database = self.database
            database.execute_sql(sql)
            return database.cursor.fetchall()

        def get_gender(self, gender):
            new_sql = """SELECT * FROM employee WHERE gender = {0}""".format(gender)
            return len(self.append_sql(new_sql))

        def get_bmi(self, bmi):
            new_sql = """SELECT * FROM employee WHERE bmi = {0}""".format(bmi)
            return len(self.append_sql(new_sql))

        def get_age_between(self, min, max):
            new_sql = """SELECT * FROM employee WHERE age BETWEEN {0} AND {1}""".format(min, max)
            return new_sql

        def get_salary_between(self, field, val, min, max):
            new_sql = """SELECT * FROM employee WHERE {0} = {1} AND salary BETWEEN {2} AND {3}""".format(field, val, min, max)
            return new_sql

        # Graph data is used to hold the values used in the graph regardless of type and options
        graphdata1 = []
        graphdata2 = []
        graphdata3 = []
        graphdata4 = []
        labels = []
        graphtitle = None

        # The following called the database to build the graph

        if argss[0] == 'pie':
            if argss[1] == 'gender':
                graphdata1.append(self.get_sex('m'))
                graphdata1.append(self.get_sex('f'))
                labels = ['Male', 'Female']
                graphtitle = "Employees by sex"
            elif argss[1] == 'bmi':
                graphdata1.append(self.get_bmi('Underweight'))
                graphdata1.append(self.get_bmi('Normal'))
                graphdata1.append(self.get_bmi('Overweight'))
                graphdata1.append(self.get_bmi('Obesity'))
                labels = ['Underweight', 'Normal', 'Overweight', 'Obese']
                graphtitle = "Employees by BMI"
            elif argss[1] == 'age':
                graphdata1.append(self.get_age_between(0, 25))
                graphdata1.append(self.get_age_between(26, 40))
                graphdata1.append(self.get_age_between(41, 50))
                graphdata1.append(self.get_age_between(51, 1000))
                labels = ['Under 25', '25 to 40', '41 to 50', 'Over 51']
                graphtitle = "Employees by Age"
        elif argss[0] == 'bar':
            if argss[1] == 'salary-by-gender':
                graphdata1.append(self.get_salary_by_between('gender', 'm', 0, 125))
                graphdata1.append(self.get_salary_by_between('gender', 'm', 126, 150))
                graphdata1.append(self.get_salary_by_between('gender', 'm', 151, 175))
                graphdata1.append(self.get_salary_by_between('gender', 'm', 176, 200))

                graphdata2.append(self.get_salary_by_between('gender', 'f', 0, 125))
                graphdata2.append(self.get_salary_by_between('gender', 'f', 126, 150))
                graphdata2.append(self.get_salary_by_between('gender', 'f', 151, 175))
                graphdata2.append(self.get_salary_by_between('gender', 'f', 176, 200))
                labels = ['<125K', '126-150K', '151-175K', '176-200K']
                graphtitle = "Salaries by Gender"
            if argss[1] == 'salary-by-age':
                graphdata1.append(self.get_salary_by_between('age', 26, 0, 125))
                graphdata1.append(self.get_salary_by_between('age', 26, 126, 150))
                graphdata1.append(self.get_salary_by_between('age', 26, 151, 175))
                graphdata1.append(self.get_salary_by_between('age', 26, 176, 200))

                graphdata2.append(self.get_salary_by_between('age', 26, 0, 125))
                graphdata2.append(self.get_salary_by_between('age', 26, 126, 150))
                graphdata2.append(self.get_salary_by_between('age', 26, 151, 175))
                graphdata2.append(self.get_salary_by_between('age', 26, 176, 200))

                graphdata3.append(self.get_salary_by_between('age', 26, 0, 125))
                graphdata3.append(self.get_salary_by_between('age', 26, 126, 150))
                graphdata3.append(self.get_salary_by_between('age', 26, 151, 175))
                graphdata3.append(self.get_salary_by_between('age', 26, 176, 200))

                graphdata4.append(self.get_salary_by_between('age', 26, 0, 125))
                graphdata4.append(self.get_salary_by_between('age', 26, 126, 150))
                graphdata4.append(self.get_salary_by_between('age', 26, 151, 175))
                graphdata4.append(self.get_salary_by_between('age', 26, 176, 200))

                labels = ['<25', '26-40K', '40-50', '>50']
                graphtitle = "Salaries by Age"

        # Sets the new graphs data
        new_graph.data1 = graphdata1
        new_graph.data2 = graphdata2
        new_graph.data3 = graphdata3
        new_graph.data4 = graphdata4
        new_graph.title = graphtitle
        new_graph.type = argss[0]
        new_graph.option = argss[1]
        new_graph.labels = labels
        new_graph.angle = None
        # Time is used when calling do_list_graphs from interpreter
        new_graph.time = time.strftime(": Create at %H:%M - Date %d/%m/%y")
        # Return the graph
        return new_graph



    def set_data(self, new_graph):
        self.data1 = new_graph.data1
        # NEW Brendan
        self.data2 = new_graph.data2
        self.data3 = new_graph.data3
        self.data4 = new_graph.data4
        self.title = new_graph.title
        self.type = new_graph.type
        self.option = new_graph.option
        self.labels = new_graph.labels
        self.angle = new_graph.angle
        self.time = new_graph.time
