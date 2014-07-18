import boogieleaks.language.ast as ast
import z3

class VerificationVariable:
	def __init__(self, type, name, position):
		self.name = name
		self.position = position
		self.type = type
	
	def getZ3Var(self):
		instance_name = '%s_%d' % (self.name, self.position)
		
		if self.type == 'int':
			return z3.Bool(instance_name)
		elif self.type == 'bool':
			return z3.Bool(instance_name)
	
	def __repr__(self):
		return "%s_%d" % (self.name, self.position)

class Environment:
	def __init__(self, conditions = [], variables = {}, parent_env = None):
		self.conditions = conditions
		self.variables = variables
		self.parent_env = parent_env
		
		# The topmost Environment is responsible for enumerating the variables
		if parent_env == None:
			self.variable_count = {}
			for n in self.variables:
				self.variable_count[n] = 0
	
	def getSubEnv(self, conditions):
		return Environment(conditions = self.conditions + conditions,
		                   variables = self.variables,
		                   parent_env = self)
	
	def newVariableInstance(self, name):
		top_env = self
		while top_env.parent_env != None:
			top_env = top_env.parent_env
		
		old_var = self.variables[name]
		
		top_env.variable_count[name] += 1
		new_pos = top_env.variable_count[name]
		
		return VerificationVariable(old_var.type, name, new_pos)


def verifyProgram(program):
	for proc in program.procedures:
		verifyProcedure(proc)

def verifyProcedure(procedure):
	# Cannot work without statements.
	if procedure.body == none:
		return
	
	variables = {}
	for name, var in procedure.body.variables.iteritems():
		variables[name] = VerificationVariable(var.type, var.id, 0)
	
	proc_env = Environment(variables = variables)
	pass

def verifyStatementList(env, stmtlist):
	return env

def applyStatement(env, stmt):
	return env

def evaluateExpression(env, expr):
	pass
