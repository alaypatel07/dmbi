def bin_equi_depth(records, no_of_bins):
    length = len(records)
    if length % no_of_bins != 0:
        raise Exception("length is not a multiple of number of bins")
    bin_size = length // no_of_bins
    sorted_records = sorted(records)
    bins = [sorted_records[i * bin_size:(i + 1) * bin_size] for i in range(no_of_bins)]
    return bins


def mean(records):
    return sum(records) / len(records)


def make_mean_bin(bin, bin_mean):
    for index, _ in enumerate(bin):
        bin[index] = bin_mean
    return bin


def bin_by_means(records, no_of_bins):
    bins = bin_equi_depth(records=records, no_of_bins=no_of_bins)
    return [make_mean_bin(bin, mean(bin)) for bin in bins]


def make_boundary_bin(bin, bin_mean):
    return [bin[-1] if record > bin_mean else bin[0] for record in bin]


def bin_by_boundaries(records, no_of_bins):
    bins = bin_equi_depth(records=records, no_of_bins=no_of_bins)
    return [make_boundary_bin(bin, mean(bin)) for bin in bins]
