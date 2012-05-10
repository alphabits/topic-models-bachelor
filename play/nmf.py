import numpy as np

def make_word_article_matrix(article_words, word_counts):
    word_vector = []
    num_articles = len(word_counts)
    for word, article_count in article_words.iteritems():
        if 2 < article_count < 0.6*num_articles:
            word_vector.append(word)
    matrix = []
    doc_vector = []
    for doc_key, doc in word_counts.iteritems():
        doc_vector.append(doc_key)
        matrix.append([doc[word] if word in doc else 0 for word in word_vector])
    return np.matrix(matrix), word_vector, doc_vector

def diff_cost(a, b):
    return np.sum(np.square(a - b))

def factorize(v, pc=10, iter=50):
    ic, fc = np.shape(v)

    w = np.matrix([list(np.random.uniform(size=pc)) for i in range(ic)])
    h = np.matrix([list(np.random.uniform(size=fc)) for i in range(pc)])

    for i in range(iter):
        wh = w*h

        cost = diff_cost(v, wh)

        if i % 10 == 0:
            print cost

        if cost == 0:
            break

        hn = np.transpose(w)*v
        hd = np.transpose(w)*w*h

        h = np.matrix(np.array(h)*np.array(hn)/np.array(hd))

        wn = v*np.transpose(h)
        wd = w*h*np.transpose(h)

        w = np.matrix(np.array(w)*np.array(wn)/np.array(wd))

    return w, h
