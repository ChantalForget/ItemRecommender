import math
import pdb
import random
from user import *	
from item import * 


def createTestSamples():
	users = []
	items = []
	with open("moreusersmorereviews.csv", "r") as filestream:
		for line in filestream:
			currentline = line.split(",")
			count = 0
			user = User()
			for x in currentline:
				try:
					if count == 0:
						user.setId(int(x)) # the first row in the csv has the userid 
					else:
						user.addReview(int(x))
					count += 1
				except: 
					pass

			user.calculateMean()
			user.calculateReviewDeviation()
			users.append(user)

	createIgnoredRatings(users)

	return users

# Adds ignored ratings for users
def createIgnoredRatings(users):
	count = 0
	with open("toignore.csv", "r") as filestream:
		for line in filestream:
			currentline = line.split(",")
			
			cuser = users[count]
			for x in currentline:
				try:
					cuser.addReviewsToIgnore(int(x))

				except:
					pass
			count += 1

def createItems(numItems):
	items = []
	for x in range(0, numItems):
		items.append(Item(x))
	return items

def wouldRecommend(userPred, itemIndex, actual):
	if userPred < 3:
		print("NOT RECOMMENDED, we think user would rate item", itemIndex ,"as:", userPred, "(actual:", actual, ")")
	else:
		print("RECOMMENDED, we think user would rate item", itemIndex ,"as:", userPred, "(actual:", actual, ")")


# Only returns positive numbers (zero inclusive)
def getMostSimilar(similarities, numWanted):
	similarities.sort(key=lambda tup: tup[1], reverse=True)

	simi = similarities[0:numWanted]

	toRemove = []

	# finds negative similarities
	for x in range(0, numWanted):
		if (simi[x][1] < 0):
			toRemove.append( simi[x])

	# removes negative similarities
	for x in range(0, len(toRemove)):
		simi.remove(toRemove[x])

	return simi

# the lower the result, the more accurate it is.
def calculateAbsoluteMeanError(predictions):
	result = 0
	for p in predictions:
		result += abs(p[0] - p[1])

	return result/len(predictions)
