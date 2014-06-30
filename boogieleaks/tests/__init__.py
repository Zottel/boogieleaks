__all__ = ['language_lexer', 'language_parser', 'captured_output']

import os, unittest, re, sys


from contextlib import contextmanager
from StringIO import StringIO

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


import boogieleaks.tests.language_lexer
import boogieleaks.tests.language_parser

def createSuite():
	suites = []
	
	suites.append(boogieleaks.tests.language_lexer.createSuite())
	suites.append(boogieleaks.tests.language_parser.createSuite())
	
	
	# Use example files to ...
	examples = []
	example_path = os.path.realpath(os.path.dirname(__file__) + '/examples')
	
	# All examples are .bpl files
	boogiematch = re.compile('.+\.bpl$')
	for _, __, filenames in os.walk(example_path):
		examples += filter(boogiematch.match, filenames)
	
	#TODO: Create tests for examples
	
	return unittest.TestSuite(suites)
