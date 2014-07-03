import ply.yacc as yacc

from boogieleaks.language.ast import *

import boogieleaks.language.lexer
from boogieleaks.language.lexer import get_lexer
tokens = boogieleaks.language.lexer.tokens

def p_program(p):
	'''program :
	           | declist'''
	if len(p) == 2:
		p[0] = Program(p[1])
	else:
		p[0] = Program([])
	pass

def p_declist(p):
	'''declist : decl
	           | decl declist'''
	if(len(p) == 2):
		p[0] = [p[1]]
	else:
		p[0] = [p[1]] + p[2]

def p_decl(p):
	'''decl : TypeDecl
	        | ConstantDecl
	        | FunctionDecl
	        | AxiomDecl
	        | VarDecl
	        | ProcedureDecl
	        | ImplementationDecl'''
	p[0] = p[1]


def p_attrlist(p):
	'''attrlist : attr
	            | attr attrlist'''
	pass #TODO

def p_attr(p):
	'''attr : '{' ':' ID attrarg '}' '''
	pass #TODO

def p_attrarg(p):
	'''attrarg : expr
	           | STRING'''
	pass #TODO

def p_exprlist(p):
	''' exprlist : expr
	             | expr ',' exprlist'''
def p_expr(p):
	'''expr : E0'''
	pass #TODO

def p_E0(p):
	'''E0 : E1
	      | E1 OP_EQUIV E0'''
	if len(p) == 2:
		p[0] = p[1]
	else:
		pass #TODO

def p_E1(p):
	'''E1 : E2
	      | E2 OP_IMPL E1'''
	if len(p) == 2:
		p[0] = p[1]
	else:
		pass #TODO

def p_E2(p):
	'''E2 : E3
	      | E3 EOr
	      | E3 EAnd'''
	if len(p) == 2:
		p[0] = p[1]
	else:
		pass #TODO

def p_EOr(p):
	'''EOr : OP_OR E3
	       | OP_OR E3 EOr'''
	if len(p) == 3:
		pass #TODO Single OR
	else:
		pass #TODO Chain case

def p_EAnd(p):
	'''EAnd : OP_AND E3
	       | OP_AND E3 EAnd'''
	if len(p) == 3:
		pass #TODO Single And
	else:
		pass #TODO Chain case

def p_E3(p):
	'''E3 : E4
	      | E4 OP_REL E4'''
	if len(p) == 2:
		p[0] = p[1]
	else:
		pass #TODO

def p_E4(p):
	'''E4 : E5
	      | E4 OP_REL E5'''
	if len(p) == 2:
		p[0] = p[1]
	else:
		pass #TODO

def p_E5(p):
	'''E5 : E6
	      | E5 '+' E6
	      | E5 '-' E6'''
	if len(p) == 2:
		p[0] = p[1]
	else:
		pass #TODO

def p_E6(p):
	'''E6 : E7
	      | E6 '*' E7
	      | E6 '/' E7
	      | E6 '%' E7'''
	if len(p) == 2:
		p[0] = p[1]
	else:
		pass #TODO

def p_E7(p):
	''' E7 : E8
	       | '!' E7
	       | '-' E7'''

def p_E8(p):
	''' E8 : E9
	       | E9 '[' exprlist ']'
	       | E9 '[' exprlist ASSIGN expr ']'
	       | E9 '[' NUMBER ':' NUMBER ']' '''
	if len(p) == 2:
		p[0] = p[1]
	else:
		pass #TODO

def p_E9(p):
	''' E9 : FALSE
	       | TRUE
	       | NUMBER
	       | BITVECTOR
	       | ID
	       | ID '(' exprlist ')'
	       | OLD '(' expr ')'
	       | '(' FORALL typeargs idstype QSEP trigattr expr ')'
	       | '(' FORALL idstype QSEP trigattr expr ')'
	       | '(' EXISTS typeargs idstype QSEP trigattr expr ')'
	       | '(' EXISTS idstype QSEP trigattr expr ')'
	       | '(' expr ')' '''
	#TODO: continue...
	pass

def p_error(p):
	print("Parsing error: Syntax error in the input at '%s', line %d." % (p.value, p.lineno))

def get_parser():
	return yacc.yacc(debug = False, optimize = True, tabmodule = 'boogieleaks_yacctab')

def parse(text):
	lexer = get_lexer()
	parser = get_parser()
	return parser.parse(text, lexer = lexer)

