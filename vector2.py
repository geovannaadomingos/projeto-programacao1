class Vector2(object):
	def FromList(list):
		return Vector2(list[0], list[1])

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def sqrMagnitude(self):
		return (self.x**2 + self.y**2)

	def magnitude(self):
		return self.sqrMagnitude()**0.5

	def normalize(self):
		return self / self.magnitude()

	def toTuple(self):
		return (self.x, self.y)

	def toList(self):
		return [self.x, self.y]

	def __add__(self, other):
		return Vector2(self.x+other.x, self.y+other.y)

	def __neg__(self):
		return Vector2(-self.x, -self.y)

	def __sub__(self, other):
		return Vector2(self.x-other.x, self.y-other.y)

	def __mul__(self, value):
		return Vector2(self.x * value, self.y * value)

	def __truediv__(self, value):
		return Vector2(self.x / value, self.y / value)

	def __eq__(self, other):
		if(other == None):
			return False
		return (self.x == other.x and self.y == other.y)

	def __repr__(self):
		return "(" + str(self.x) + ", " + str(self.y) + ")"

	def __len__(self):
		return 2

	def __getitem__(self, index):
		if(index == 0):
			return self.x
		else:
			return self.y