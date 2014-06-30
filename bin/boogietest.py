#!/usr/bin/env python

# For development:
# Check if boogieleaks is installed.
# Otherwise: Add the parent directory of bin/ to the python path
import imp, sys, os
try:
	imp.find_module('boogieleaks')
except ImportError:
	boogiepath = os.path.realpath(os.path.dirname(__file__) + "/..")
	print("Inserting '%s' into system path" % boogiepath)
	sys.path.insert(0, boogiepath)

import unittest

from boogieleaks.tests import createSuite

if __name__ == '__main__':
	testrunner = unittest.TextTestRunner(verbosity = 2)
	testSuite = createSuite()
	testrunner.run(testSuite)

