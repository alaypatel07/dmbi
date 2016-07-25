# Normalization by decimal scaling: normalizes by moving the decimal point of values of feature X. The
# number of decimal points moved depends on the maximum absolute value of X. A modified value
# new_v corresponding to v is obtained using
# new_v = (v)/ (10 ^ c)
# where c is the smallest integer such that max(|new_v|) < 1.
# Example: suppose the range of attribute X is −500 to 45. The maximum absolute value of X is 500. To
# normalize by decimal scaling we will divide each value by 1,000 (c = 3). In this case, −500 becomes
# −0.5 while 45 will become 0.045.

from typing import Sequence, Union


def get_range(records: Sequence[float]) -> Union[float, float]:
    return float(min(records)), float(max(records))
