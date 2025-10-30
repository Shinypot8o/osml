class Attribute:
	def __init__(self, type, default, other):
		self.type = type
		self.default = default
		self.other = other

class Object:
	def __init__(self):
		self.attributes = {}

	def _add_attribute(self, name, attr: Attribute):
		self.attributes.update(name, attr)

class ObjectInstance:
	def __init__(self):
		self.type


class Scene:
	def __init__(self):
		pass