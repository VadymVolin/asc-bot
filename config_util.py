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
    print('TODO:add implementation here')
