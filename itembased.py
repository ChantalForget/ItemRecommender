import math
from utils import *

def getAdjustedCosSimil(item1, item2):
	topCalc = 0
	bottom1Calc = 0
	bottom2Calc = 0

	for x in range(0, len(item1)):
		topCalc += round(item1[x][1] * item2[x][1], 2) #it passes in the calculated deviation review, no need to do that here. 
		bottom1Calc += (item1[x][1] ** 2)
		bottom2Calc += (item2[x][1] ** 2)

	bottom1Calc = math.sqrt(bottom1Calc)
	bottom2Calc = math.sqrt(bottom2Calc)

	bottom = round(bottom1Calc * bottom2Calc, 4)
	return round(topCalc/bottom, 4)


def prediction(ratedItems, users, userIndex, itemIndex):
	topCalc = 0
	bottomCalc = 0
	absoluteError = 0

	mostSimiliarItems = []
	rawRated = 0

	# get the id of all the similar items used to predict
	for x in range(0, len(ratedItems)):
		mostSimiliarItems.append(ratedItems[x][0])

	user = users[userIndex]
	# gets the raw review of the similar items for the user
	# add them together
	for i in range(0, len(ratedItems)):
		rawRated += user.getReview(i)
	# then divide to get the weighted raw review
	rawRated = rawRated/len(mostSimiliarItems)

	# now do calculation for predicting!
	for x in range(0, len(ratedItems)): 
		if (x != userIndex):
			topCalc += (ratedItems[x][1] * rawRated )
			bottomCalc += ratedItems[x][1]

	return round(topCalc/bottomCalc, 4)


# you take in user bc you want to find the ignored vals
# for each user
def itemBasedNN(user, userIndex, users, items):
	print("-----ITEM BASED NEAREST NEIGHBOUR-----")
	predictions = []

	for ignored in range(0, len(user.getReviewsToIgnore())):
		# index of the ignored review you want to find. 
		index = user.getReviewsToIgnore()[ignored] 

		similarities = []
		count = 0

		# now compute the similarities between the ignored item and every other item
		while count != len(items): # the number of items
			ignoredIndices = []
			if count != index: # we don't want to compare the same object
				ignoredIndices.extend(items[index].reviewsToIgnore) 
				ignoredIndices.extend(items[count].reviewsToIgnore)
				item1 = []
				item2 = []
				for x in range(0,len(users)): #create the 2 items,cycle through users to get their reviews
					if x not in ignoredIndices: 
						item1.append([users[x], users[x].getDeviationReview(index)]) 
						item2.append([users[x], users[x].getDeviationReview(count)])

				sim = getAdjustedCosSimil(item1, item2)
				similarities.append([count, sim]) #item similar, similarity
			
			count += 1

		simils = getMostSimilar(similarities, 20) 	

		# print("Items most similar:", simils)
		pred = prediction(simils, users, userIndex, index)
		predictions.append([pred, users[userIndex].getReview(index)])

		wouldRecommend(pred, index, users[userIndex].getReview(index))

	if len(predictions) == 0:
		print('no reviews to predict')	

	return predictions
