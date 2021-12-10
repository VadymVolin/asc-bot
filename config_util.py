import csv

from config_constants import WORDS_SCHEME_FILE
from config_constants import CHARACTERS_SCHEME

def get_words_scheme():
    words = []
    with open(WORDS_SCHEME_FILE, 'r', encoding='utf8') as csvfile:
        csvreader = csv.reader(csvfile)
        words = next(csvreader)
    return words

def get_characters_scheme():
    dict = {}
    with open(CHARACTERS_SCHEME, 'r', encoding='utf8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if (row):
                dict[row[0]] = row[1 : len(row)]

    return dict
