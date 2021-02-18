# module to read in a file and put the counts of each word in bins and export it to an excel sheet

import pandas as pd
import argparse
from collections import defaultdict

# parse argument line for file to bin
parser = argparse.ArgumentParser(
    description='Read in a file, bin the word counts, and export it to an excel sheet.')
parser.add_argument('file', metavar='S', type=str, nargs='+',
                    help='the file to read in')

# if the file name has no spaces it will be a string but if it does it will be in a list
input_file = parser.parse_args().file if type(
    parser.parse_args().file) == str else parser.parse_args().file[0]

# extract the text from the file given
f = open(input_file, encoding="utf8")
raw_text = f.read()
f.close()

# initialize word count dictionary
word_count_bins_dict = defaultdict(int)

# iterate through the raw text and
for word in sorted(raw_text.split()):
    word_count_bins_dict[word] += 1

# create series and export to excel sheet
word_count_bins_series = pd.Series(word_count_bins_dict)

# export to excel sheet
word_count_bins_series.to_csv('word_count_bins.csv', encoding='utf8')
