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
	'''decl : typedecl
	        | constantdecl
	        | functiondecl
	        | axiomdecl
	        | vardecl
	        | proceduredecl
	        | implementationdecl'''
	p[0] = p[1]

def p_typedecl(p):
	'''typedecl : typeconstructor
	            | typesynonym'''
	p[0] = p[1]

def p_typeconstructor(p):
	'''typeconstructor : TYPE ID ';'
	                   | TYPE ID idlist ';'
	                   | TYPE FINITE ID ';'
	                   | TYPE FINITE ID idlist ';'
	                   | TYPE attrlist ID ';'
	                   | TYPE attrlist ID idlist ';'
	                   | TYPE attrlist FINITE ID ';'
	                   | TYPE attrlist FINITE ID idlist ';' '''
	#TODO
	pass

def p_typesynonym(p):
	'''typesynonym : TYPE ID '=' type ';'
	               | TYPE ID idlist '=' type ';'
	               | TYPE attrlist ID '=' type ';'
	               | TYPE attrlist ID idlist '=' type ';' '''
	#TODO
	pass

def p_type(p):
	'''type : typeatom
	        | maptype '''
	p[0] = p[1]

def p_type_id(p):
	'''type : ID
	        | ID typectorargs'''
	#TODO: don't ignore typectorargs
	p[0] = p[1]

def p_typeatom(p):
	'''typeatom : BOOL
	            | INT
	            | BITVECT_TYPE '''
	p[0] = p[1]

def p_typeatom_braces(p):
	'''typeatom : '(' type ')' '''
	pass #TODO

def p_maptype(p):
	'''maptype : '[' typelist ']' type
	           | typeargs '[' typelist ']' type'''
	#TODO
	pass

def p_typeargs(p):
	'''typeargs : '<' idlist '>' '''
	#TODO
	pass

def p_typectorargs(p):
	'''typectorargs : typeatom
	                | typeatom typectorargs
	                | ID
	                | ID typectorargs
	                | maptype'''
	#TODO
	pass

def p_constantdecl(p):
	'''constantdecl : CONST idstype orderspec ';'
	                | CONST UNIQUE idstype orderspec ';'
	                | CONST attrlist idstype orderspec ';'
	                | CONST attrlist UNIQUE idstype orderspec ';' '''
	#TODO
	pass

def p_idstype(p):
	'''idstype : idlist ':' type'''
	p[0] = (p[1], p[3])

def p_functiondecl(p):
	'''functiondecl : FUNCTION ID fsig ';'
	                | FUNCTION attrlist ID fsig ';'
	                | FUNCTION ID fsig '{' expr '}'
	                | FUNCTION attrlist ID fsig '{' expr '}' '''
	#TODO
	pass

def p_fsig(p):
	'''fsig : '(' ')' RETURNS '(' farg ')'
	        | '(' farglist ')' RETURNS '(' farg ')'
	        | typeargs '(' ')' RETURNS '(' farg ')'
	        | typeargs '(' farglist ')' RETURNS '(' farg ')' '''
	#TODO
	pass

def p_farg(p):
	''' farg : type
	         | ID ':' type '''
	#TODO
	pass

def p_farglist(p):
	''' farglist : farg
	             | farg ',' farglist '''
	if(len(p) == 2):
		p[0] = [p[1]]
	else:
		p[0] = [p[1]] + p[3]

def p_idstypelist(p):
	''' idstypelist : idstype
	                | idstype ',' idstypelist '''
	if(len(p) == 2):
		p[0] = [p[1]]
	else:
		p[0] = [p[1]] + p[3]

def p_typelist(p):
	'''typelist : type
	            | type ',' typelist'''
	if(len(p) == 2):
		p[0] = [p[1]]
	else:
		p[0] = [p[1]] + p[3]

def p_idlist(p):
	'''idlist : ID
	          | ID ',' idlist'''
	if(len(p) == 2):
		p[0] = [p[1]]
	else:
		p[0] = [p[1]] + p[3]


def p_attrlist(p):
	'''attrlist : attr
	            | attr attrlist'''
	if(len(p) == 2):
		p[0] = [p[1]]
	else:
		p[0] = [p[1]] + p[2]

def p_attr(p):
	'''attr : '{' ':' ID '}'
	        | '{' ':' ID attrarglist '}' '''
	pass #TODO

def p_attrarglist(p):
	'''attrarglist : attrarg
	               | attrarg ',' attrarglist '''
	if(len(p) == 2):
		p[0] = [p[1]]
	else:
		p[0] = [p[1]] + p[3]

def p_attrarg(p):
	'''attrarg : expr
	           | STRING'''
	pass #TODO

def p_exprlist(p):
	''' exprlist : expr
	             | expr ',' exprlist'''
	pass #TODO

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
	      | E4 OP_REL E4
	      | E4 PARSEP E4'''
	if len(p) == 2:
		p[0] = p[1]
	else:
		pass #TODO

def p_E4(p):
	'''E4 : E5
	      | E4 OP_CONCAT E5'''
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
	       | ID '(' ')'
	       | ID '(' exprlist ')'
	       | OLD '(' expr ')'
	       | '(' FORALL typeargs idstypelist QSEP expr ')'
	       | '(' FORALL idstypelist QSEP expr ')'
	       | '(' EXISTS typeargs idstypelist QSEP expr ')'
	       | '(' EXISTS idstypelist QSEP expr ')'
	       | '(' FORALL typeargs idstypelist QSEP trigattr expr ')'
	       | '(' FORALL idstypelist QSEP trigattr expr ')'
	       | '(' EXISTS typeargs idstypelist QSEP trigattr expr ')'
	       | '(' EXISTS idstypelist QSEP trigattr expr ')'
	       | '(' expr ')' '''
	#TODO: Split (QUANTOR ...) maybe?
	#TODO
	pass

def p_trigattr(p):
	'''trigattr : trigger
	            | attr'''
	pass #TODO

def p_axiomdecl(p):
	'''axiomdecl : AXIOM expr ';'
	             | AXIOM attrlist expr ';' '''
	pass #TODO

def p_vardecl(p):
	'''vardecl : VAR idstypewherelist ';'
	           | VAR attrlist idstypewherelist ';' '''
	pass #TODO

def p_idstypewherelist(p):
	'''idstypewherelist : idstypewhere
	                    | idstypewhere ',' idstypewherelist'''
	if(len(p) == 2):
		p[0] = [p[1]]
	else:
		p[0] = [p[1]] + p[3]

def p_idstypewhere(p):
	'''idstypewhere : idstype
	                | idstype whereclause'''
	# TODO: The "whereclause" is ignored
	p[0] = p[1]

def p_proceduredecl(p):
	'''proceduredecl : PROCEDURE ID psig ';'
	                 | PROCEDURE ID psig ';' speclist
	                 | PROCEDURE ID psig body
	                 | PROCEDURE ID psig speclist body '''
	if p[4] == ';':
		pass #TODO
	else:
		p[0] = Procedure(p[2], body = p[len(p) - 1])

def p_proceduredeclattr(p):
	'''proceduredecl : PROCEDURE attrlist ID psig ';'
	                 | PROCEDURE attrlist ID psig ';' speclist
	                 | PROCEDURE attrlist ID psig body
	                 | PROCEDURE attrlist ID psig speclist body'''
	if p[5] == ';':
		pass #TODO
	else:
		p[0] = Procedure(p[3].value, body = p[len(p) - 1])


def p_psig(p):
	'''psig : '(' ')'
	        | '(' ')' outparameters
	        | '(' idstypewherelist ')'
	        | '(' idstypewherelist ')' outparameters
	        | typeargs '(' ')'
	        | typeargs '(' ')' outparameters
	        | typeargs '(' idstypewherelist ')'
	        | typeargs '(' idstypewherelist ')' outparameters '''
	pass #TODO

def p_outparameters(p):
	'''outparameters : RETURNS '(' ')'
	                 | RETURNS '(' idstypewherelist ')' '''
	pass #TODO

def p_speclist(p):
	'''speclist : spec
	            | spec speclist'''
	if(len(p) == 2):
		p[0] = [p[1]]
	else:
		p[0] = [p[1]] + p[2]

def p_spec(p):
	'''spec : REQUIRES expr ';'
	        | FREE REQUIRES expr ';'
	        | MODIFIES ';'
	        | MODIFIES idlist ';'
	        | FREE MODIFIES ';'
	        | FREE MODIFIES idlist ';'
	        | ENSURES expr ';'
	        | FREE ENSURES expr ';' '''
	pass #TODO

def p_implementationdecl(p):
	'''implementationdecl : IMPLEMENTATION ID isig
	                      | IMPLEMENTATION ID isig bodylist
	                      | IMPLEMENTATION attrlist ID isig
	                      | IMPLEMENTATION attrlist ID isig bodylist '''
	pass #TODO

def p_isig(p):
	'''isig : '(' ')'
	        | '(' ')' outparameters
	        | '(' idstypelist ')'
	        | '(' idstypelist ')' outparameters
	        | typeargs '(' ')'
	        | typeargs '(' ')' outparameters
	        | typeargs '(' idstypelist ')'
	        | typeargs '(' idstypelist ')' outparameters '''
	pass #TODO

def p_bodylist(p):
	'''bodylist : body
	            | body bodylist'''
	if(len(p) == 2):
		p[0] = [p[1]]
	else:
		p[0] = [p[1]] + p[2]
	
def p_body(p):
	'''body : '{' stmtlist '}'
	        | '{' localvardecllist stmtlist '}' '''
	if len(p) == 4:
		p[0] = Body(statements = p[2])
	else:
		p[0] = Body(statements = p[3], localvariables = p[2])

def p_localvardecllist(p):
	'''localvardecllist : localvardecl
	                    | localvardecl localvardecllist '''
	if(len(p) == 2):
		p[0] = p[1]
	else:
		p[0] = p[1] + p[2]

def p_localvardecl(p):
	'''localvardecl : VAR idstypewherelist ';'
	                | VAR attrlist idstypewherelist ';' '''
	p[0] = []
	idstypewherelist = p[len(p) - 2]
	for type in idstypewherelist:
		for var in type[0]:
			p[0].append(LocalVariable(var, type[1]))

def p_stmtlist(p):
	'''stmtlist :
	            | lempty
	            | lstmtlist
	            | lstmtlist lempty'''
	#TODO: We ignore lempty - since it's probably only required when working with GOTO
	p[0] = p[1] if len(p) > 1 else []

def p_lstmtlist(p):
	'''lstmtlist : lstmt
	             | lstmt lstmtlist'''
	if(len(p) == 2):
		p[0] = [p[1]]
	else:
		p[0] = [p[1]] + p[2]

def p_lstmt(p):
	'''lstmt : stmt
	         | ID ':' lstmt '''
	p[0] = p[len(p) - 1]

def p_lempty(p):
	'''lempty : ID ':'
	          | ID ':' lempty'''
	#TODO: We ignore lempty - since it's probably only required when working with GOTO
	p[0] = []

def p_stmt(p):
	'''stmt : ASSERT expr ';'
	        | ASSUME expr ';'
	        | HAVOC idlist ';'
	        | lhslist ASSIGN exprlist ';'
	        | CALL ID '(' ')' ';'
	        | CALL ID '(' exprlist ')' ';'
	        | CALL idlist ASSIGN ID '(' ')' ';'
	        | CALL idlist ASSIGN ID '(' exprlist ')' ';'
	        | CALL FORALL ID '(' ')' ';'
	        | CALL FORALL ID '(' wildcardexprlist ')' ';'
	        | ifstmt
	        | WHILE '(' wildcardexpr ')' blockstmt
	        | WHILE '(' wildcardexpr ')' loopinvlist blockstmt
	        | BREAK ';'
	        | BREAK ID ';'
	        | RETURN ';'
	        | GOTO idlist ';' '''
	pass #TODO

def p_lhslist(p):
	'''lhslist : lhs
	           | lhs ',' lhslist'''
	if(len(p) == 2):
		p[0] = [p[1]]
	else:
		p[0] = [p[1]] + p[3]

def p_lhs(p):
	''' lhs : ID
	        | ID mapselectlist'''
	pass #TODO

def p_mapselectlist(p):
	'''mapselectlist : '[' exprlist ']'
	                 | '[' exprlist ']' mapselectlist '''
	#TODO: lol nope
	if(len(p) == 4):
		p[0] = [p[2]]
	else:
		p[0] = [p[2]] + p[4]

def p_wildcardexprlist(p):
	'''wildcardexprlist : wildcardexpr
	                    | wildcardexpr ',' wildcardexprlist'''
	if(len(p) == 2):
		p[0] = [p[1]]
	else:
		p[0] = [p[1]] + p[3]

def p_wildcardexpr(p):
	'''wildcardexpr : expr
	                | '*' '''
	pass #TODO

def p_blockstmt(p):
	'''blockstmt : '{' stmtlist '}' '''
	pass #TODO

def p_ifstmt(p):
	'''ifstmt : IF '(' wildcardexpr ')' blockstmt
	          |  IF '(' wildcardexpr ')' blockstmt else '''
	pass #TODO

def p_else(p):
	'''else : ELSE blockstmt
	        | ELSE ifstmt '''
	pass #TODO

def p_loopinvlist(p):
	'''loopinvlist : loopinv
	               | loopinv loopinvlist'''
	if(len(p) == 2):
		p[0] = [p[1]]
	else:
		p[0] = [p[1]] + p[2]

def p_loopinv(p):
	'''loopinv : INVARIANT expr ';'
	           | FREE INVARIANT expr ';' '''
	pass #TODO

def p_orderspec(p):
	'''orderspec :
	             | COMPLETE
	             | parentinfo
	             | parentinfo COMPLETE '''
	pass #TODO

def p_parentinfo(p):
	'''parentinfo : PARSEP
	              | PARSEP parentedgelist '''
	pass #TODO

def p_parentedgelist(p):
	'''parentedgelist : parentedge
	                  | parentedge ',' parentedgelist'''
	if(len(p) == 2):
		p[0] = [p[1]]
	else:
		p[0] = [p[1]] + p[3]

def p_parentedge(p):
	'''parentedge : ID
	              | UNIQUE ID'''
	pass #TODO

def p_whereclause(p):
	'''whereclause : WHERE expr'''
	pass #TODO

def p_trigger(p):
	'''trigger : '{' exprlist '}' '''
	pass #TODO

def p_error(p):
	print("Parsing error: Syntax error in the input at '%s', line %d." % (p.value, p.lineno))

def get_parser():
	return yacc.yacc(debug = False, optimize = True, tabmodule = 'boogieleaks_yacctab')

def parse(text):
	lexer = get_lexer()
	parser = get_parser()
	return parser.parse(text, lexer = lexer)

