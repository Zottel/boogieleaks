
import unittest

from boogieleaks.tests import captured_output

from boogieleaks.language.lexer import get_lexer

class LexerTest(unittest.TestCase):
	def setUp(self):
		self.lexer = get_lexer()
	
	# Expected tokens are given as an array of (type, value)
	def lexExpect(self, input, tokens):
		self.lexer.input(input)
		for token in self.lexer:
			expected = tokens.pop(0)
			self.assertEqual(token.type, expected[0])
			self.assertEqual(token.value, expected[1])
	
	def runTest(self):
		if hasattr(self, 'input') and hasattr(self, 'expect'):
			self.lexExpect(self.input, self.expect)
		else:
			raise Exception("Test case not properly setup.")

class SimpleTest(LexerTest):
	def __init__(self):
		super(SimpleTest, self).__init__()
		self.input = '''
			A := "asdf";
		'''
		self.expect = [
			('ID', 'A'),
			('ASSIGN', ':='),
			('STRING', 'asdf'),
			(';', ';')
		]

class NumberTest(LexerTest):
	def __init__(self):
		super(LexerTest, self).__init__()
		self.input = '''
			A := 123;
		'''
		self.expect = [
			('ID', 'A'),
			('ASSIGN', ':='),
			('NUMBER', 123),
			(';', ';')
		]

class BitVectTest(LexerTest):
	def __init__(self):
		super(LexerTest, self).__init__()
		self.input = '''
			12bv13
		'''
		self.expect = [
			('BITVECTOR', {'value': 12, 'size': 13}),
		]

class BitVectFailTest(LexerTest):
	def runTest(self):
		self.input = '''
			12bv2
		'''
		self.expect = [
			('BITVECTOR', {'value': 12, 'size': 2}),
		]
		#(ValueError, "Line 2: 12bv2, Bitvector value too big")
		with self.assertRaises(ValueError):
			self.lexExpect(self.input, self.expect)

class InvalidTokenTest(LexerTest):
	def runTest(self):
		input = '''
			A == true; ~
		'''
		
		expected = [
			('ID', 'A'),
			('OP_REL', '=='),
			('TRUE', 'true'),
			(';', ';')
		]
		
		with captured_output() as (out, err):
			self.lexExpect(input, expected)
		
		self.assertEqual(out.getvalue().strip(),
		                 "Parsing error: Illegal character '~'.",
		                 msg = "Did not get expected lexer error message")
		                 
		                 
class OperatorTest(LexerTest):
	def __init__(self):
		super(LexerTest, self).__init__()
		self.input = '''
			 A <==> B;
			 A ==> B;
			 A || B;
			 A && B;
			 A ++ B;
		'''
		self.expect = [
			('ID', 'A'),
			('OP_EQUIV', '<==>'),
			('ID', 'B'),
			(';', ';'),
			('ID', 'A'),
			('OP_IMPL', '==>'),
			('ID', 'B'),
			(';', ';'),
			('ID', 'A'),
			('OP_OR', '||'),
			('ID', 'B'),
			(';', ';'),
			('ID', 'A'),
			('OP_AND', '&&'),
			('ID', 'B'),
			(';', ';'),
			('ID', 'A'),
			('OP_CONCAT', '++'),
			('ID', 'B'),
			(';', ';')
		]

def createSuite():
	cases = []
	cases.append(SimpleTest())
	cases.append(NumberTest())
	cases.append(BitVectTest())
	cases.append(BitVectFailTest())
	cases.append(InvalidTokenTest())
	cases.append(OperatorTest())
	return unittest.TestSuite(cases)
