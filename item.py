class Item(object):
	def __init__(self, givenId):
		self.id = givenId
		self.reviewsToIgnore = []

	def setId(self, newid):
		self.id = newid

	def addReviewsToIgnore(self, toAdd):
		self.reviewsToIgnore.append(toAdd)

	def createIgnoredReviews(self, users):
		for u in users:
			if self.id in u.getReviewsToIgnore():
				self.addReviewsToIgnore(u.id - 1)


	def printIgnored(self):
		print("IGNORED INDICES FOR ITEM",self.id, ":", self.reviewsToIgnore)