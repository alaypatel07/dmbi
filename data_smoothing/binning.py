def bin_equi_depth(records, no_of_bins):
    length = len(records)
    if length % no_of_bins != 0:
        raise Exception("length is not a multiple of number of bins")
    bin_size = length // no_of_bins
    sorted_records = sorted(records)
    bins = [sorted_records[i * bin_size:(i + 1) * bin_size] for i in range(no_of_bins)]
    return bins
