# http://blogs.gartner.com/martin-kihn/how-to-build-a-recommender-system-in-python/
from utils import *
from userbased import *
from itembased import *

def main():
	items = []
	users = createTestSamples()

	for u in users:
		u.printReviews()
		# u.createReviews2()
		# u.printDeviationReviews() 

	items = createItems(len(users[0].getReviews()))

	for i in items:
		i.createIgnoredReviews(users)
		i.printIgnored()

	# format: predicted rating, actual rating
	userBasedPreds = [] 
	itemBasedPreds = []

	for x in range(0, len(users)): #find the missing reviews for every user
		print("***********USER", users[x].id, "***********")
		itemBasedPreds.extend(itemBasedNN(users[x],x,users, items))
		userBasedPreds.extend(userBasedNN(users, x))

	uame = calculateAbsoluteMeanError(userBasedPreds)
	iame = calculateAbsoluteMeanError(itemBasedPreds)
	print("user based absolute mean error:", uame)
	print("item based absolute mean error:", iame)

	
main()