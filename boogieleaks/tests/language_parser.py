
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
		Program([Procedure(id = 'bla',
		                   body = Body(statements = [],
		                               localvariables = [LocalVariable('a', 'int'),
		                                                 LocalVariable('b', 'bv3'),
		                                                 LocalVariable('c', 'bv3'),
		                                                 LocalVariable('d', 'bv3')]))])
		)

class ParseAssertion(ParseTest):
	def runTest(self):
		self.parseExpect('''
			procedure bla() {
				assert(1 == 2);
			}
		''',
		Program([Procedure(id = 'bla',
		                   body = Body(statements = [Assertion(None)],
		                               localvariables = []))])
		)


class ParseAssignment(ParseTest):
	def runTest(self):
		self.parseExpect('''
			procedure bla() {
				a := 1;
			}
		''',
		Program([Procedure(id = 'bla',
		                   body = Body(statements = [Assignment({'a': Number(1)})],
		                               localvariables = []))])
		)

class ParseAssignment2(ParseTest):
	def runTest(self):
		self.parseExpect('''
			procedure bla() {
				a := 1 - 3;
			}
		''',
		Program([Procedure(id = 'bla',
		                   body = Body(statements = [Assignment({'a': Substraction(Number(1), Number(3))})],
		                               localvariables = []))])
		)


def createSuite():
	cases = []
	cases.append(ParseEmpty())
	cases.append(ParseProcedure())
	cases.append(ParseAssertion())
	cases.append(ParseAssignment())
	cases.append(ParseAssignment2())
	return unittest.TestSuite(cases)
