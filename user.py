class User(object):
	def __init__(self):
		self.id = 0
		self.reviews = []
		self.reviewsToIgnore = []
		self.reviewsDeviation = []
		self.mean = 0

	def setId(self, newid):
		self.id = newid

	def getId(self):
		return self.id

	def addReview(self,toAdd):
		self.reviews.append(toAdd)

	def getReview(self, index): 
		return self.reviews[index]

	# used for item based similarity
	def getDeviationReview(self, index):
		return self.reviewsDeviation[index]

	def getReviews(self):
		return self.reviews

	def getReviewsToIgnore(self):
		return self.reviewsToIgnore

	def addReviewsToIgnore(self, toAdd):
		self.reviewsToIgnore.append(toAdd)

	def printReviews(self):
		temp = []
		vals = []
		for x in range(0, len(self.reviews)):
			if x in self.reviewsToIgnore:
				temp.append("?")
				vals.append(self.reviews[x])
			else:
				temp.append("{0}".format(self.reviews[x]))
		print(self.id, temp) #, "ignored vals", vals, "mean:", self.mean)

	def printDeviationReviews(self):
		print(self.id, self.reviewsDeviation)

	def calculateMean(self):
		mean = 0
		for x in range(0, len(self.reviews)):
			if x not in self.reviewsToIgnore: # don't include "unknown" reviews in the mean
				mean += self.reviews[x]

		self.mean = (mean/(len(self.reviews) - len(self.reviewsToIgnore) ))

	# this creates the deviation from the average rating
	def calculateReviewDeviation(self):
		if self.mean == 0:
			return
		else:
			# self.createReviews2()
			for x in range(0, len(self.reviews)):
				t = self.reviews[x] - self.mean
				self.reviewsDeviation.append(round(t, 4))