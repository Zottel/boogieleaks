from distutils.core import setup

setup(
	name = 'boogieleaks',
	version = '0.1',
	
	license = 'LICENSE'
	
	url = 'http://plv.mpi-sws.org/', #TODO: change to something helpful maybe?
	description = 'Open source Boogie to z3 verification tool',
	long_description=open('README').read(),
	
	author = 'Julius Roob',
	author_email = 'julius@juliusroob.de',
	maintainer = 'Julius Roob',
	maintainer_email = 'julius@juliusroob.de',
	
	scripts=['bin/boogieleaks.py'],
	#package_dir = {'boogieleaks': 'boogieleaks'},
	packages = ['boogieleaks'],
	requires = ['ply']
	
	# Package data, ...
	package_data = {
		'': ['*.bpl']
	}
	# ... to be included in the source directories for easy access
	include_package_data = True,
)
