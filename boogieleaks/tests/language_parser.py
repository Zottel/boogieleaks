
import unittest

from boogieleaks.tests import captured_output

from boogieleaks.language.ast import *
from boogieleaks.language.parser import parse


class ParseTest(unittest.TestCase):
    def __init__(self, input, expected):
        self.input = input
        self.expected = expected

    def runTest(self):
        self.parseExpect(self.input, self.expected)

	def parseExpect(self, input, expected):
		parsed = parse(input)
		self.assertEqual(expected, parsed)
		#TODO: Recursive comparison of AST?
		# == should do the right thing, let's hope assertEqual does
		# the right thing.


class ParseEmpty(ParseTest):
	def runTest(self):
		self.parseExpect('//Empty program', Program([]))

def createSuite():
	cases = []
	cases.append(ParseEmpty())
	return unittest.TestSuite(cases)
