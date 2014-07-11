
import unittest

from boogieleaks.tests import captured_output

from boogieleaks.language.ast import *
from boogieleaks.language.parser import parse


class ParseTest(unittest.TestCase):
	
	def parseExpect(self, input, expected):
		parsed = parse(input)
		self.assertEqual(expected, parsed)
		#TODO: Recursive comparison of AST?
		# == should do the right thing, let's hope assertEqual does
		# the right thing.

class ParseTestGiven(ParseTest):
	def __init__(self, input, expected):
		self.input = input
		self.expected = expected
	
	def runTest(self):
		self.parseExpect(self.input, self.expected)

class ParseEmpty(ParseTest):
	def runTest(self):
		self.parseExpect('//Empty program', Program([]))

class ParseProcedure(ParseTest):
	def runTest(self):
		self.parseExpect('''
			procedure bla() {
				var a: int,
				    b, c, d: bv3;
			}
		''',
		Program([None]))

def createSuite():
	cases = []
	cases.append(ParseEmpty())
	cases.append(ParseProcedure())
	return unittest.TestSuite(cases)
