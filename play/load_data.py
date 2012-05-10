import json


with open('course-pages/articlecounts.json', 'r') as f:
    article_counts = json.load(f)

with open('course-pages/wordcounts.json', 'r') as f:
    word_counts = json.load(f)
