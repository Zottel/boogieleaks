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

class Statement(ASTNode):
	def __init__(self):
		pass
	
	def __str__(self):
		return "(statement %s)" % (self.__dict__)

class Assertion(Statement):
	def __init__(self, condition):
		self.condition = condition
	
	def __str__(self):
		return "(assertion %s)" % (self.condition)


class Assumption(Statement):
	def __init__(self, condition):
		self.condition = condition
	
	def __str__(self):
		return "(assumption %s)" % (self.condition)

class Assignment(Statement):
	def __init__(self, assignments = {}):
		self.assignments = assignments
	
	def __str__(self):
		return "(assignment %s)" % (self.assignments)

class Implementation(ASTNode):
	pass #TODO

class Attribute(ASTNode):
	pass #TODO

class Expression(ASTNode):
	pass #TODO

class Addition(Expression):
	def __init__(self, op1, op2):
		self.op1 = op1
		self.op2 = op2
	
	def __repr__(self):
		return "(+ %s %s)" % (self.op1, self.op2)

class Substraction(Expression):
	def __init__(self, op1, op2):
		self.op1 = op1
		self.op2 = op2
	
	def __repr__(self):
		return "(- %s %s)" % (self.op1, self.op2)
		
class Multiplication(Expression):
	def __init__(self, op1, op2):
		self.op1 = op1
		self.op2 = op2
	
	def __repr__(self):
		return "(* %s %s)" % (self.op1, self.op2)
		
class Division(Expression):
	def __init__(self, op1, op2):
		self.op1 = op1
		self.op2 = op2
	
	def __repr__(self):
		return "(/ %s %s)" % (self.op1, self.op2)
		
class Modulo(Expression):
	def __init__(self, op1, op2):
		self.op1 = op1
		self.op2 = op2
	
	def __repr__(self):
		return "(% %s %s)" % (self.op1, self.op2)
		
class Not(Expression):
	def __init__(self, op):
		self.op = op
	
	def __repr__(self):
		return "(! %s %s)" % (self.op)
		
class Minus(Expression):
	def __init__(self, op):
		self.op = op
	
	def __repr__(self):
		return "(- %s %s)" % (self.op)		

class Number(Expression):
	def __init__(self, value):
		self.value = value

class Variable(Expression):
	def __init__(self, name):
		self.name = name
	
	def __repr__(self):
		return "(variable %s)" % (self.name)
		
class Boolean(Expression):
	def __init__(self, value):
		self.value = value
	
	def __repr__(self):
		return "(boolean %s)" % (self.value)

