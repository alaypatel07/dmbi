from csv import reader, DictReader

# TODOS : 1) Test and integrate the class into the project
#         2) Provide a method to write data back into the CSV


class Extractor(object):

    def __init__(self, filepath):
        self.file = filepath
        with open(self.file, "r") as csv_file:
            data_iter = DictReader(csv_file)
            self._data = [row for row in data_iter]

    def get_column(self, column_name):
        try:
            return [row[column_name] for row in self._data]
        except KeyError as e:
            raise KeyError()

    def __getitem__(self, item):
        return self._data[item]

    def __len__(self):
        return len(self._data)