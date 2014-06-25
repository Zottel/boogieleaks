from distutils.core import setup

setup(
    name = 'boogieleaks',
    version = '0.1',
    description = 'Open source BoogiePL to z3',
    author = 'Julius Roob',
    author_email = 'julius@juliusroob.de',
    maintainer = 'Julius Roob',
    maintainer_email = 'julius@juliusroob.de',
    url = 'http://plv.mpi-sws.org/',
    package_dir = {'boogieleaks': 'boogieleaks'},
    packages = ['boogieleaks'],
    requires = ['ply']
)
