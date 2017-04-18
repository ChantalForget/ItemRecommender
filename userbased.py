import math
from utils import * 

def userBasedNN(users, count):
	print("-----USER BASED NEAREST NEIGHBOUR-----")
	similarities = []
	# get the similarity between user1 and every other user
	for x in range(0, len(users)):
		if count != x:
			similarities.append([users[x].id, calculateSimPearsons(users[count], users[x]) ])
	simils = getMostSimilar(similarities, 15)
	# print("Users most similar:", simils)

	preds = userPrediction(simils, users[count], users)
	
	if len(preds) == 0:
		print("no reviews to predict")

	return preds


# returns the pearsons similarity between 2 users
def calculateSimPearsons(user1, user2):
	ignoredIndices = []
	ignoredIndices.extend(user1.getReviewsToIgnore())
	ignoredIndices.extend(user2.getReviewsToIgnore())
	
	similarities = []
	user2its = []
	user1its = []
	count = 0


	# get the list of items you want to compare	
	while count != len(user1.getReviews()): # the number of items
		if count not in ignoredIndices: 
			user1its.append([count, user1.getReview(count)]) 
			user2its.append([count, user2.getReview(count)])
		
		count += 1

	# calculate the pearsons similarity
	user1mean = user1.mean
	user2mean = user2.mean
	topCalc = 0
	bottom1Calc = 0
	bottom2Calc = 0

	for x in range(0, len(user1its)):
		topCalc += (user1its[x][1] - user1mean) * (user2its[x][1] - user2mean)
		bottom1Calc += ((user1its[x][1] - user1mean) ** 2)
		bottom2Calc += ((user2its[x][1] - user2mean) ** 2)

	bottom1Calc = math.sqrt(bottom1Calc)
	bottom2Calc = math.sqrt(bottom2Calc) 

	bottom = bottom1Calc * bottom2Calc

	return topCalc/bottom


def userPrediction(similarities, user1, users):
	predictions = []
	for ignored in range(0, len(user1.getReviewsToIgnore())):
		topCalc = 0
		bottomCalc = 0
		pred = 0
		# index of the ignored review you want to find. 
		index = user1.getReviewsToIgnore()[ignored]	

		for x in range(0, len(similarities)):
			user2 = users[similarities[x][0] - 1]
			# make sure user2 actually has a review for the ignored val. 
			# skip them in the calculation if they don't have a review.
			if index in user2.getReviewsToIgnore(): 
				# print("woops can't use user", user2.id, "they didn't review item", index)
				t = 0 # just put there here bc I want that print statement.
			else:
				topCalc += 	(similarities[x][1] * (user2.getReview(index) - user2.mean) )
				bottomCalc += similarities[x][1]


		pred = round(user1.mean + (topCalc/bottomCalc), 4)

		wouldRecommend(pred, index, user1.getReview(index))

		predictions.append([pred, user1.getReview(index)])

	return predictions

