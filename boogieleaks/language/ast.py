class ASTNode:
	def __eq__(self, other):
		if type(self) == type(other):
			return self.__dict__ == other.__dict__
		else:
			#print("Compare incomparable (%s, %s)" % (self, other))
			return False

class Program(ASTNode):
	def __init__(self, declarations):
		#print(declarations)
		self.declarations = declarations
		#TODO: sort declarations into type, procedure etc....
		pass

class Type(ASTNode):
	pass #TODO

class TypeConstructor(Type):
	pass #TODO

class TypeSynonym(Type):
	pass #TODO

class Constant(ASTNode):
	pass #TODO

class Function(ASTNode):
	pass #TODO

class Axiom(ASTNode):
	pass #TODO

class Var(ASTNode):
	pass #TODO

class Procedure(ASTNode):
	def __init__(self, id, body = None):
		#print("(procedure %s, %s)" % (id, body))
		self.id = id
		self.body = body

class Body(ASTNode):
	def __init__(self, statements = [], localvariables = []):
		#print("(body %s, %s)" % (statements, localvariables))
		self.statements = statements
		self.variables = {}
		for v in localvariables:
			self.variables[v.id] = v

class LocalVariable(ASTNode):
	def __init__(self, id, type):
		#print("(var %s, %s)" % (id, type))
		self.id = id
		self.type = type
	def __str__(self):
		return "(var %s %s)" % (self.id, self.type)

class Implementation(ASTNode):
	pass #TODO

class Attribute(ASTNode):
	pass #TODO

class Expression(ASTNode):
	pass #TODO
