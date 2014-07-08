
class Program:
	def __init__(self, declarations):
		self.declarations = declarations
		#TODO: sort declarations into type, procedure etc....
		pass
	
	def __eq__(self, other): 
		return self.__dict__ == other.__dict__

class Type:
	pass

class Constant:
	pass

class Function:
	pass

class Axiom:
	pass

class Var:
	pass

class Procedure:
	pass

class Implementation:
	pass

class Attribute:
	pass

class Expression:
	pass
