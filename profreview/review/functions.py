
# Function to Evaluate the Prof Net Ratings
def net_rating(r):
	# r is dictionary that store all rating for prof/course
	l=int(r.count())
	s=0
	# total number of ratings for him
	for i in r:
		s+=int(i.rating1)
	if l!=0 :

		return (s/l)
	else :
		return 0.0
