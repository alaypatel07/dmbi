import csv
from functools import reduce


def mean(records):
    return sum(records)/len(records)


def get_std_dev(a, b):
    b = (b - m) ** 2
    return a + b


def get_z_score(v):
    return(v - m)/std_dev

if __name__ == '__main__':
    i = input()
    if i == "test":
        records = [1, 2, 3]
        m = mean(records)
        std_dev = (reduce(get_std_dev, records, 0)/len(records)) ** 0.5
        z = map(get_z_score, records)
        for i in z:
            print(i)
    else:
        with open("Data.csv") as csvfile:
            data_iter = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            try:
                data = [row for row in data_iter]
                sales = [float(row["Sales"]) for row in data]
                print(sales)
                m = mean(sales)
                std_dev = (reduce(get_std_dev, sales) / len(sales)) ** 0.5
                z = map(get_z_score, sales)
                new_data = [dict(row, z_score_sales=new_row) for row, new_row in zip(data, z)]
                with open("ZNormalizedData.csv", "w") as new_csv_file:
                    data_writer = csv.DictWriter(new_csv_file, new_data[0].keys())
                    data_writer.writeheader()
                    data_writer.writerows(new_data)
            except TypeError as e:
                print(e)

