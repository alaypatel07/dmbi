import csv
from functools import reduce


def mean(records):
    return sum(records)/len(records)

if __name__ == '__main__':
    i = input()
    if i == "test":
        records = [1, 2, 3]
        m = mean(records)

        std_dev = (reduce(lambda x, y: x + ((y - m) ** 2), records, 0) / len(records)) ** 0.5

        z = map(lambda x: (x - m) / std_dev, records)

        for i in z:
            print(i)
    else:

        with open("Data.csv") as csvfile:
            data_iter = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            try:
                data = [row for row in data_iter]
                sales = [float(row["Sales"]) for row in data]

                # print(sales)
                # Calculate mean
                m = mean(sales)
                # Calculate standard deviation
                std_dev = (reduce(lambda x, y: x + ((y - m) ** 2), sales, 0) / len(sales)) ** 0.5
                # Calculate Z score
                z = map(lambda x: (x - m) / std_dev, sales)
                # Prepare data structure to write in file
                new_data = [dict(row, z_score_sales=new_row) for row, new_row in zip(data, z)]
                # Open file for writing
                with open("ZNormalizedData.csv", "w") as new_csv_file:
                    data_writer = csv.DictWriter(new_csv_file, new_data[0].keys())
                    data_writer.writeheader()
                    data_writer.writerows(new_data)
            except TypeError as e:
                print(e)

