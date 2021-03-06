
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
		                   body = Body(statements = [Assertion(RelOperator('==',[Number(1),Number(2)]))],
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
		
class ParseMultiplication(ParseTest):
	def runTest(self):
		self.parseExpect('''
			procedure bla() {
				a := 1 * 3;
			}
		''',
		Program([Procedure(id = 'bla',
		                   body = Body(statements = [Assignment({'a': Multiplication(Number(1), Number(3))})],
		                               localvariables = []))])
		)

		
class ParseDivision(ParseTest):
	def runTest(self):
		self.parseExpect('''
			procedure bla() {
				a := 1 / 3;
			}
		''',
		Program([Procedure(id = 'bla',
		                   body = Body(statements = [Assignment({'a': Division(Number(1), Number(3))})],
		                               localvariables = []))])
		)
		
				
class ParseModulo(ParseTest):
	def runTest(self):
		self.parseExpect('''
			procedure bla() {
				a := 6 % 2;
			}
		''',
		Program([Procedure(id = 'bla',
		                   body = Body(statements = [Assignment({'a': Modulo(Number(6), Number(2))})],
		                               localvariables = []))])
		)
		
class ParseMinus(ParseTest):
	def runTest(self):
		self.parseExpect('''
			procedure bla() {
				a := -42;
			}
		''',
		Program([Procedure(id = 'bla',
		                   body = Body(statements = [Assignment({'a': Minus(Number(42))})],
		                               localvariables = []))])
		)
		
class ParseNot(ParseTest):
	def runTest(self):
		self.parseExpect('''
			procedure bla() {
				a := !b;
			}
		''',
		Program([Procedure(id = 'bla',
		                   body = Body(statements = [Assignment({'a': Not(Variable('b'))})],
		                               localvariables = []))])
		)
		
class ParseBoolean(ParseTest):
	def runTest(self):
		self.parseExpect('''
			procedure bla() {
				a := false;
				b := true;
			}
		''',
		Program([Procedure(id = 'bla',
		                   body = Body(statements = [Assignment({'a': Boolean('false')}),
		                                             Assignment({'b': Boolean('true')})],
		                               localvariables = []))])
		)

class ParseSpecs(ParseTest):
	def runTest(self):
		self.parseExpect('''
			procedure blub(x: int)
			ensures x > 1;
			requires x < 2;
			{
			}
		''',
		Program([Procedure(id = 'blub',
		                   specs = [Guarantee(RelOperator('>', [Variable('x'),Number(1)])),
		                            Requirement(RelOperator('<', [Variable('x'),Number(2)]))],
		                   body = Body())])
		)
		
class ParseOperator(ParseTest):
	def runTest(self):
		#TODO:And and Or need brackets for some reason
		self.parseExpect('''
			procedure bla() {
				assert(a <==> b);
				assert(a ==> b);
				assert(a <==> (b <==> c));
				assert((a || b) && c);
			}
		''',
		Program([Procedure(id = 'bla',
		                   body = Body(statements = [Assertion(Operator('equiv', [Variable('a'), Variable('b')])),
		                   													 Assertion(Operator('impl', [Variable('a'), Variable('b')])),
		                   													 Assertion(Operator('equiv', [Variable('a'), Operator('equiv', [Variable('b'), Variable('c')])])),
		                   													 Assertion(Operator('and', [Operator('or', [Variable('a'), Variable('b')]),Variable('c')]))],
		                               localvariables = []))])
		)

def createSuite():
	cases = []
	cases.append(ParseEmpty())
	cases.append(ParseProcedure())
	cases.append(ParseAssertion())
	cases.append(ParseAssignment())
	cases.append(ParseAssignment2())
	cases.append(ParseMultiplication())
	cases.append(ParseDivision())
	cases.append(ParseModulo())
	cases.append(ParseMinus())
	cases.append(ParseNot())
	cases.append(ParseBoolean())
	cases.append(ParseOperator())
	cases.append(ParseSpecs())
	return unittest.TestSuite(cases)
