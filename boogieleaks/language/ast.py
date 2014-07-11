
class Program:
	def __init__(self, declarations):
		self.declarations = declarations
		#TODO: sort declarations into type, procedure etc....
		pass
	
	def __eq__(self, other): 
		return self.__dict__ == other.__dict__

class Type:
	pass #TODO

class TypeConstructor(Type):
	pass #TODO

class TypeSynonym(Type):
	pass #TODO

class Constant:
	pass #TODO

class Function:
	pass #TODO

class Axiom:
	pass #TODO

class Var:
	pass #TODO

class Procedure:
	def __init__(self, body):
		self.body = body

class Body:
	def __init__(self, statements = [], localvariables = []):
		self.statements = statements
		self.variables = {}
		for v in localvariables:
			self.variables[v.id] = v

class LocalVariable:
	def __init__(self, id, type):
		self.id = id
		self.type = type
	def __str__(self):
		return "(VAR %s %s)" % (self.id, self.type)

class Implementation:
	pass #TODO

class Attribute:
	pass #TODO

class Expression:
	pass #TODO
