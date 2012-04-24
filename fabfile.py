from fabric.api import local

def test():
    print 'Testing'

def docs():
    local('sphinx-build -c sphinx/ . docs/web')
