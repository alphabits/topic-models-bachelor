import json


article_counts = {}
output_file = 'course-pages/articlecounts.json'
input_file = 'course-pages/wordcounts.json'


with open(input_file, 'r') as f:
    word_counts = json.load(f)

for doc_key in word_counts:
    word_count_doc = word_counts[doc_key]
    for word in word_count_doc:
        if not word in article_counts:
            article_counts[word] = 0
        article_counts[word] += 1

with open(output_file, 'w') as f:
    json.dump(article_counts, f)
