import re
import ply.lex as lex

reserved = {
	'assert' : 'ASSERT',
	'assume' : 'ASSUME',
	'axiom' : 'AXIOM',
	'bool' : 'BOOL',
	'break' : 'BREAK',
	'call' : 'CALL',
	'complete' : 'COMPLETE',
	'const' : 'CONST',
	'else' : 'ELSE',
	'ensures' : 'ENSURES',
	'exists' : 'EXISTS',
	'false' : 'FALSE',
	'finite' : 'FINITE',
	'forall' : 'FORALL',
	'free' : 'FREE',
	'function' : 'FUNCTION',
	'goto' : 'GOTO',
	'havoc' : 'HAVOC',
	'if' : 'IF',
	'implementation' : 'IMPLEMENTATION',
	'int' : 'INT',
	'invariant' : 'INVARIANT',
	'modifies' : 'MODIFIES',
	'old' : 'OLD',
	'procedure' : 'PROCEDURE',
	'requires' : 'REQUIRES',
	'return' : 'RETURN',
	'returns' : 'RETURNS',
	'true' : 'TRUE',
	'type' : 'TYPE',
	'unique' : 'UNIQUE',
	'var' : 'VAR',
	'where' : 'WHERE',
	'while' : 'WHILE'
}

literals = "*{}=[]();:,+-!%*/<>"

tokens = [
	'BITVECTOR',
	'STRING'
	# Operators
	'OP_EQUIV',
	'OP_IMPL',
	'OP_OR',
	'OP_AND',
	'ASSIGN',
	'NUMBER',
	'OP_REL',
	'OP_CONCAT',
	'OP_ADD',
	'OP_QSEP'
] + list(reserved.values())

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	t.type = reserved.get(t.value, 'ID')
	return t

# TODO: Unicode maybe?
t_OP_EQUIV = r'<==>'
t_OP_IMPL = r'==>'
t_OP_OR = r'\|\|'
t_OP_AND = r'\&\&'
t_ASSIGN = r':='
t_NUMBER = r'\d'

t_OP_REL = r'==|!=|<=|>=|<:'

t_OP_CONCAT = '\+\+'
t_OP_ADD = '\+'

t_QSEP = '::'


def t_STRING(t):
	r'"[^"]*"'
	t.value = t.value[1:-1]
	return t

bitvect_pattern = re.compile('(\d+)bv(\d+)')
def t_BITVECTOR(t):
	r'\d+bv\d+'
	matched = bitvect_pattern.match(t.value)
	t.value = {'value': int(matched.group(1)), 'size': int(matched.group(2))}
	return t

t_ignore = ' \t'
t_ignore_COMMENT = r'\/\/.*'

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_error(t):
	print("Parsing error: Illegal character '%s'." % t.value[0])
	t.lexer.skip(1)


def get_lexer():
	return lex.lex(optimize = True, lextab = 'boogieleaks_lextab')

if __name__ == '__main__':
	data = '''
		// RUN: %boogie -noinfer "%s" > "%t"
		// RUN: %diff "%s.expect" "%t"
		var {:phase 1} g:int;
		
		procedure {:yields} {:phase 1} PB()
		{
			yield;
			call Incr();
			yield;
		}
		
		procedure {:yields} {:phase 0,1} Incr();
		ensures {:atomic}
		|{A:
			g := g + 1; return true;
		}|;
		
		procedure {:yields} {:phase 0,1} Set(v: int);
		ensures {:atomic}
		|{A:
			g := v; return true;
		}|;
		
		procedure {:yields} {:phase 1} PC()
		ensures {:phase 1} g == 3;
		{
			yield;
			call Set(3);
			yield;
			assert {:phase 1} g == 3;
		}
		
		procedure {:yields} {:phase 1} PE()
		{
			call PC();
		}
		
		procedure {:yields} {:phase 1} PD()
		{
			call PC();
			assert {:phase 1} g == 3;
		}
		
		procedure {:yields} {:phase 1} Main()
		{
			yield;
			while (*)
			{
				yield;
				async call PB();
				yield;
				async call PE();
				yield;
				async call PD();
				yield;
			}
		}
	'''
	lexer = get_lexer()
	lexer.input(data)
	for token in lexer:
		print(token)
