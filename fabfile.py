from fabric.api import local
import os

joinpath = os.path.join

ROOT = os.path.dirname(__file__)

def docs():
    doc_folder = joinpath(ROOT, 'docs')
    web_output_folder = joinpath(doc_folder, 'web')
    web_index_file = joinpath(web_output_folder, 'index.html')
    local('sphinx-build {0} {1}'.format(doc_folder, web_output_folder))
    local('gnome-open {0} &'.format(web_index_file))
