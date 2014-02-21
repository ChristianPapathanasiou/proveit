from hashlib import sha256

class Node():
	def __init__(self, value, hashdigest):
		self.value = value
		self.hashdigest = hashdigest
	
def NodeCombiner(left, right):
	newvalue = str(left.value + right.value)
	lefthash, righthash = left.hashdigest, right.hashdigest
	hashdigest = sha256(newvalue + lefthash + righthash).hexdigest()
	
	return Node(newvalue, hashdigest)
