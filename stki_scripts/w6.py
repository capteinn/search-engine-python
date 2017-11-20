"""
author rochanaph
November 5 2017
"""
import w3, w4

def make_vector(wordQuery, vocab_all):
    """

    :param wordQuery:
    :param vocab_all:
    :return:
    """

    # pre-processing kueri dengan perlakuan yg sama dengan corpus
    clean_query = w3.prepro_base(wordQuery)
    token_query = clean_query.split()

    # membuat vektor dengan panjang vocab all dan nilai awal 0 semua
    vector = [0]* len(vocab_all)

    # mengisikan nilai vektor kueri sesuai jumlah kemunculan kata dalam kueri
    for word in token_query:
        if word in vocab_all:
            vector[vocab_all.index(word)] +=1

    vector = w4.l2_normalizer(vector)
    return vector
    