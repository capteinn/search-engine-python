"""
author rochanaph
September 4 2017
"""

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

## tokenisasi
def tokenize(string, separator=None):
    return string.split(separator)

## case folding
def fold(string):
    return string.lower()

## squeeze whitespace
def squeeze_whitespace(string):
    while '  ' in string: # dobel space
        string = string.replace('  ', ' ') # dobel space diganti 1 space
    return string

## remove punctuation
def remove_punctuation(string):
    punc = ["!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-",
            ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]",
            "^", "_", "`", "{", "|", "}", "~", "\""]
    for item in punc:
        string = string.replace(item, " ")
    return string.strip()

## remove stopwords
path_stopwords = "./stopwords.txt"
def remove_stopword(list_of_strings):
    with open(path_stopwords, 'r') as file:
        stopwords = file.readlines()
        stopwords = [item.rstrip('\n') for item in stopwords]
    list_of_strings = [item for item in list_of_strings if item not in stopwords and len(item)>1]
    return list_of_strings


def stemmer_fac(string):
    fac = StemmerFactory()
    stem_cr = fac.create_stemmer()
    return stem_cr.stem(string)

def preprotext(string):
    token = tokenize(squeeze_whitespace(string))
    cleantext = [fold(item) for item in token]
    cleantext = [remove_punctuation(item) for item in cleantext]
    cleantext = remove_stopword(cleantext)
    cleantext = [stemmer_fac(item) for item in cleantext]
    return " ".join(cleantext)

def prepro_base(string):
    token = tokenize(squeeze_whitespace(string))
    cleantext = [fold(item) for item in token]
    cleantext = [remove_punctuation(item) for item in cleantext]
    return " ".join(cleantext)

# path_uas = "./uas files/jawaban siswa.txt"

# with open(path_uas, 'r') as file:
# 	articles = preprotext(file.read())

# print articles