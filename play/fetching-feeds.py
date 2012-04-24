import feedparser
import numpy as np
import re

def strip_html(html):
    cleaned = ''
    state = 0
    for char in html:
        if char == '<':
            state = 1
        elif char == '>':
            state = 0
            cleaned += ' '
        elif state == 0:
            cleaned += char
    return cleaned

_splitter = re.compile('\\W*')
def separate_words(text):
    return [s.lower() for s in _splitter.split(text) if len(s) > 3]

def get_feeds():
    with open('reuter-feeds.txt', 'r') as feed_file:
        feeds = feed_file.readlines()
    return feeds

def get_article_words(feeds):
    all_words = {}
    article_words = []
    article_titles = []
    entry_count = 0

    for feed in feeds:
        fp = feedparser.parse(feed)
        for e in fp.entries:
            if e.title in article_titles:
                continue
            txt = e.title.encode('utf8') + strip_html(e.description.encode('utf8'))
            words = separate_words(txt)
            article_titles.append(e.title)
            tmp_word_count = {}

            for word in words:
                all_words[word] = all_words.get(word, 0) + 1
                tmp_word_count[word] = tmp_word_count.get(word, 0) + 1

            article_words.append(tmp_word_count)
            entry_count += 1
    return all_words, article_words, article_titles

def make_matrix(all_words, article_words):
    word_list = []
    for word, count in all_words.items():
        if count > 3 and count < len(article_words)*0.6:
            word_list.append(word)
    word_matrix = [[f.get(word, 0) for word in word_list] for f in article_words]
    return word_matrix, word_list

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
