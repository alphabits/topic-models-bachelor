import json


def load_data():
    data_dicts = []
    for fn in ['wordcounts.json', 'articlecounts.json']:
        with open('course-pages/'+fn, 'r') as f:
            data_dicts.append(json.load(f))
    return data_dicts

def make_vocabulary(wordcounts, articlecounts):
    num_articles = len(articlecounts)
    vocabulary = []
    for word, num_articles_containg_word in articlecounts.iteritems():
        if 2 < num_articles_containg_word < 0.6*num_articles:
            vocabulary.append(word)
    return vocabulary

def get_document_in_blei_format(document, vocabulary):
    entries = []
    for word, count in document.items():
        try:
            entry = '{0}:{1}'.format(vocabulary.index(word)+1, count)
            entries.append(entry)
        except ValueError:
            pass
    return '{0} {1}'.format(len(entries), ' '.join(entries))

def get_document_in_blei_format_dict(document, vocabulary):
    blei_document = {}
    for word, count in document.items():
        try:
            key = str(vocabulary.index(word)+1)
            blei_document[key] = count
        except ValueError:
            pass
    return blei_document


def get_corpus_in_blei_format(corpus, vocabulary):
    lines = []
    document_keys = list(corpus)
    document_keys.sort()
    for document_key in document_keys:
        doc_output = get_document_in_blei_format(corpus[document_key], vocabulary)
        lines.append(doc_output)
    return '\n'.join(lines)

def save_vocabulary(base_filename, vocabulary):
    s = "\n".join(w.encode('utf-8') for w in vocabulary)
    with open(base_filename+'.lda-c.vocab', 'w') as f:
        f.write(s)

def save_corpus_in_blei_format(base_filename, corpus, vocabulary):
    save_vocabulary(base_filename, vocabulary)
    with open(base_filename+'.lda-c', 'w') as f:
        f.write(get_corpus_in_blei_format(corpus, vocabulary))
