from BeautifulSoup import BeautifulSoup, Tag, NavigableString
from glob import glob
import json
import re

def get_text_content(tag):
    to_return = []
    for content in tag.contents:
        if type(content) == NavigableString:
            to_return.append(content)
        else:
            to_return += get_text_content(content)
    return to_return

def get_word_count(word_list):
    count_dict = {}
    for word in word_list:
        if word not in count_dict:
            count_dict[word] = 0
        count_dict[word] += 1
    return count_dict


files = glob('course-pages/*.html')
output_file = 'course-pages/wordcounts.json'
splitter = re.compile('[\\s:(),.]*')
i = 0
wordcounts = {}

for filename in files:
    with open(filename, 'r') as f:
        text = f.read()

    soup = BeautifulSoup(text)

    print "Opened html file with title %s" % (soup.findAll('h2')[0].text,)
    print i

    textmatch = lambda txt: txt.startswith('Overordnede kursus')
    header = soup.findAll(text=textmatch)
    if header:
        table = header[0].findParent('table')
        if table:
            parsed_text = '\n'.join(get_text_content(table))
            words = [s.lower() for s in splitter.split(parsed_text) if len(s)>2]
            key = re.search(r'[0-9]+', filename).group(0)
            wordcounts[key] = get_word_count(words)
    i += 1

with open(output_file, 'w') as outfile:
    json.dump(wordcounts, outfile, indent=4)
