"""
author rochanaph
October 23 2017"""

import w3,w4,w5, os

def findSim(pathfile, pathcorpus):
    """
    mencari jarak/similarity antara suatu file dengan sekumpulan file/corpus dalam folder.
    :param pathfile: path tempat artikel yg dicari
    :param pathcorpus: path tempat folder
    :return: nama file, jarak terdekat
    """

    this_path = os.path.split(__file__)[0]
    pathcorpus = os.path.join(this_path, pathcorpus)
    pathfile = os.path.join(this_path, pathfile)
    # membaca sekaligus pre-processing semua artikel corpus simpan ke dictionary
    articles = {}
    for item in os.listdir(pathcorpus):
        if item.endswith(".txt"):
            with open(pathcorpus + "/" + item, 'r') as file:
                articles[item] = w3.prepro_base(file.read())

    # tambahkan artikel yg dicari ke dictionary
    findname = pathfile.split("/")[-1]
    try:
        articles[findname]
    except:
        with open(pathfile, 'r') as file:
            articles[findname] = w3.prepro_base(file.read())

    # representasi bow
    list_of_bow = []
    for key, value in articles.items():
        list_token = value.split()
        dic = w4.bow(list_token)
        list_of_bow.append(dic)

    # matrix
    matrix_akhir = w4.matrix(list_of_bow)

    # jarak
    id_file = articles.keys().index(findname)    # index findname dalam articles.keys() = index dalam matrix
    jarak = {}
    for key, vektor in zip(articles.keys(), matrix_akhir):
        if key != findname:
            jarak[key] = w5.euclidean(matrix_akhir[id_file], vektor)

    return w4.sortdic(jarak, descending=False)

# print findSim('./text files/ot_2.txt','./text files')

def findBow(pathfile, pathcorpus):
    """
    mencari bow pada suatu file dengan sekumpulan file/corpus dalam folder.
    :param pathfile: path tempat artikel yg dicari
    :param pathcorpus: path tempat folder
    :return: kata, jumlah kata
    """

    this_path = os.path.split(__file__)[0]
    pathfile = os.path.join(this_path, pathcorpus, pathfile)

    with open(pathfile, 'r') as file:
        articles = w3.prepro_base(file.readline())    # representasi bow

    list_token = articles.split()
    dic = w4.bow(list_token)

    return w4.sortdic(dic, descending=True) 

path_uas = "./uas files/hasil uas prepro.txt"
with open(path_uas, 'r') as file:
    articles = file.read()
list_token = articles.split()
dic = w4.bow(list_token)
sortdic = w4.sortdic(dic, descending=True)
for v in sortdic:
    print str(v[0]) + " : " + str(v[1])

def findHoax(artikel, pathcorpus):
    """
    mencari jarak/similarity antara suatu kalimat inputan dengan sekumpulan file/corpus (artikel HOAX) dalam folder.
    :param pathfile: inputan artikel/kalimat/content
    :param pathcorpus: path tempat folder
    :return: nama file, jarak terdekat, readline/baris pertama dokumen
    """

    this_path = os.path.split(__file__)[0]
    pathcorpus = os.path.join(this_path, pathcorpus)

    # membaca sekaligus pre-processing semua artikel corpus simpan ke dictionary
    articles = {}
    # artikel origin yang full belum dilakukan pre-processing
    articles_origin = []

    for item in os.listdir(pathcorpus):
        if item.endswith(".txt"):
            with open(pathcorpus + "/" + item, 'r') as file:
                articles[item] = w3.prepro_base(file.read())

    # tambahkan artikel yg dicari ke dictionary
    # tandai key index dari artikel dengan "input"
    findname = "input"

    try:
        articles[findname]
    except:
        articles[findname] = w3.prepro_base(artikel)

    # representasi bow
    list_of_bow = []

    for key, value in articles.items():
        list_token = value.split()
        dic = w4.bow(list_token)
        list_of_bow.append(dic)

    # matrix
    matrix_akhir = w4.matrix(list_of_bow)

    # jarak
    id_file = articles.keys().index(findname)    # index findname dalam articles.keys() = index dalam matrix
    
    jarak = {}
    for key, vektor in zip(articles.keys(), matrix_akhir):
        if key != findname:
            jarak[key] = w5.cosine(matrix_akhir[id_file], vektor)

    data = w4.sortdic(jarak, descending=True, n=4)

    # membaca baris pertama dari setiap hasil dokumen
    for v in data:
        for item in os.listdir(pathcorpus):
            if item.endswith(".txt"):
                with open(pathcorpus + "/" + item, 'r') as file:
                    # apabila setiap nama_file == v[0] yakni nama file yang ada di data maka ditampilkan readline-nya
			if item == v[0]:
				articles_origin.append(file.readline())

    return zip(data, articles_origin)
