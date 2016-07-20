import csv
from functools import reduce


def get_z_score(records):
    length = len(records)
    # Calculate mean
    m = sum(records)/length
    # Calculate standard deviation
    std_dev = (reduce(lambda x, y: x + ((y - m) ** 2), records, 0) / length) ** 0.5
    # Calculate Z score
    z = map(lambda x: (x - m) / std_dev, records)
    return z


if __name__ == '__main__':
    with open("Data.csv") as csvfile:
        data_iter = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        try:
            data = [row for row in data_iter]
            sales = [float(row["Sales"]) for row in data]

            # print(sales)

            z = get_z_score(sales)

            # Prepare data structure to write in file
            new_data = [dict(row, z_score_sales=new_row) for row, new_row in zip(data, z)]
            # Open file for writing
            with open("ZNormalizedData.csv", "w") as new_csv_file:
                data_writer = csv.DictWriter(new_csv_file, new_data[0].keys())
                data_writer.writeheader()
                data_writer.writerows(new_data)
        except TypeError as e:
            print(e)
