import os
import requests
from time import sleep

BASE_URL = 'http://www.kurser.dtu.dk'
SAVE_DIR = 'course-pages'
INPUT_FILE = 'course-urls.txt'
SHORT_DELAY = 0.5
LONG_DELAY = 4
ITERATIONS_BETWEEN_LONG_DELAYS = 15

i = 1

with open(INPUT_FILE, 'r') as f:
    for line in f.readlines():
        line = line.strip()
        url = os.path.join(BASE_URL, line)
        print 'Fetching ' + url
        r = requests.get(url)
        save_url = os.path.join(SAVE_DIR, line.replace('aspx', 'html'))
        with open(save_url, 'w') as sf:
            sf.write(r.text.encode('utf-8'))
        if (i % ITERATIONS_BETWEEN_LONG_DELAYS) == 0:
            print 'Sleeping'
            sleep(LONG_DELAY)
        else:
            sleep(SHORT_DELAY)
        i += 1
