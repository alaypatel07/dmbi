import csv


def min_max(records, lower, upper, new_lower, new_upper):
    return [((((a - lower) / (upper - lower)) * (new_upper - new_lower)) + new_lower) for a in records]


if __name__ == '__main__':
    with open("Data.csv") as csvfile:
        data_iter = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        try:
            data = [row for row in data_iter]
            sales = [float(row["Sales"]) for row in data]
            low = min(sales)
            upp = max(sales)
            # print(low, upp)
            answer = min_max(sales, low, upp, 0, 1)
            new_data = [dict(row, Normalized_Sales=new_row) for row, new_row in zip(data, answer)]
            with open("NormalizedData.csv", "w") as new_csv_file:
                data_writer = csv.DictWriter(new_csv_file, new_data[0].keys())
                data_writer.writeheader()
                data_writer.writerows(new_data)
            print("Done")
        except TypeError as e:
            print(e)
