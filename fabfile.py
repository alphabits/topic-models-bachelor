from fabric.api import local
import os

from utils.bibparse import parse_bib


joinpath = os.path.join

ROOT = os.path.dirname(__file__)
DOC_FOLDER = joinpath(ROOT, 'docs')
WEB_OUTPUT_FOLDER = joinpath(DOC_FOLDER, 'web')
WEB_INDEX_FILE = joinpath(WEB_OUTPUT_FOLDER, 'index.html')

def docs():
    local('sphinx-build {0} {1}'.format(DOC_FOLDER, WEB_OUTPUT_FOLDER))

def opendocs():
    local('gnome-open {0}'.format(WEB_INDEX_FILE))

def generate_doc_bibliography():
    bib = parse_bib(joinpath(ROOT, 'bibliography.bib'))
    lines = ['Bibliography', '============', '']
    for entry in bib:
        lines.append('.. [{0}] *{1}*, {2}, {3} edition {4}'.format(entry.key, entry.data['title'], 
                entry.data['author'], entry.data['edition'], entry.data['year']))
    with open(joinpath(DOC_FOLDER, 'bibliography.rst'), 'w') as f:
        f.write("\n".join(lines))
