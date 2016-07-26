# Normalization by decimal scaling: normalizes by moving the decimal point of values of feature X. The
# number of decimal points moved depends on the maximum absolute value of X. A modified value
# new_v corresponding to v is obtained using
# new_v = (v)/ (10 ^ c)
# where c is the smallest integer such that max(|new_v|) < 1.
# Example: suppose the range of attribute X is −500 to 45. The maximum absolute value of X is 500. To
# normalize by decimal scaling we will divide each value by 1,000 (c = 3). In this case, −500 becomes
# −0.5 while 45 will become 0.045.
import csv
from typing import Sequence, Union, Iterable


def get_range(records: Sequence[float]) -> Union[float, float]:
    return float(min(records)), float(max(records))


def get_scaling_power(range: Union[float, float]) -> int:
    min, max = int(abs(range[0])), int(abs(range[1]))
    c = len(str(max)) + 1 if max > min else len(str(min)) + 1
    return c


def decimal_scale(records: Sequence[float]) -> Iterable[float]:
    c = get_scaling_power(get_range(records=records))
    return map(lambda x: x/ (10 ** c), records)


if __name__ == '__main__':
    with open("../SampleData.csv") as csvfile:
        data_iter = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        try:
            data = [row for row in data_iter]
            sales = [float(row["Sales"]) for row in data]

            # print(sales)

            z = decimal_scale(sales)

            # Prepare data structure to write in file
            new_data = [dict(row, decimal_scale_sales=new_row) for row, new_row in zip(data, z)]
            # Open file for writing
            with open("DecimalScaleNormalizedData.csv", "w") as new_csv_file:
                data_writer = csv.DictWriter(new_csv_file, new_data[0].keys())
                data_writer.writeheader()
                data_writer.writerows(new_data)
        except TypeError as e:
            print(e)
