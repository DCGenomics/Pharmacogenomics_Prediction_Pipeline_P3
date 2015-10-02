from tools import pipeline_helpers
import pandas as pd

def run1(infile, features_label, output_label):
    """
    Handle variant data by only keeping rows where 10-90% of samples have
    variants.

    For CNV data, don't do any filtering.

    Otherwise, simply remove rows with zero variance.
    """
    if (features_label == 'exome_variants' or 'variants' in output_label):
        d = pipeline_helpers.remove_nfrac_variants(infile, nfrac=0.1)
    elif features_label == 'cnv':
        return pd.read_table(infile, index_col=0)
    else:
        d = pipeline_helpers.remove_zero_variance(infile)
    return d
