from csv import reader, DictReader

# TODOS : 1) Test and integrate the class into the project
#         2) Provide a method to write data back into the CSV


class Extractor(object):

    def __init__(self, filepath):
        self.file = filepath

    def get_column(self, column_name, type_conversion=None):
        with open(self.file, "r") as csv_file:
            data_iter = DictReader(column_name)
            if type_conversion is None:
                data = [row[column_name] for row in data_iter]
            else:
                data = [type_conversion(row[column_name]) for row in data_iter]
            return data
